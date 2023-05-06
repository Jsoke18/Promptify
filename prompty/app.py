from flask import Flask, render_template, request, redirect, url_for, jsonify, session, g
from pymongo import MongoClient
import json
from functools import wraps
import os

# Supabase
from supabase_py import create_client, Client

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://joshsoke:Freddy141823@prompt.wexmajs.mongodb.net/?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = "adgdVbBf2FGdhfgjhzxjklkl4dfsd35df34efdfaw4nsbdrtwafcerACSZH"

mongo = MongoClient(app.config["MONGO_URI"])
db = mongo.prompts_db

# Supabase configuration
SUPABASE_URL = "https://jlowomwkcdikzdgyuouv.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impsb3dvbXdrY2Rpa3pkZ3l1b3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODMzNDU2NTcsImV4cCI6MTk5ODkyMTY1N30.A0sPRme3fG0EKcQfyA_WbDHfRBqEuIwjV_j2o965XgY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Supabase login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = g.user
        if user is None:
            return redirect(url_for("index", next=request.url))
        return f(*args, **kwargs)

    return decorated_function

# Supabase user loader
@app.before_request
def load_user():
    user = None
    session_cookie = request.cookies.get("sb:session")
    if session_cookie:
        user = supabase.auth.api.get_user(session_cookie)
    g.user = user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search_query']
        tag_filter = request.form['tag_filter']

        search_conditions = {
            "$or": [
                {"title": {"$regex": search_query, "$options": "i"}},
                {"text": {"$regex": search_query, "$options": "i"}},
                {"tags": {"$regex": search_query, "$options": "i"}}
            ]
        }

        if tag_filter:
            search_conditions["tags"] = {"$regex": tag_filter, "$options": "i"}

        prompts = db.prompts.find(search_conditions)
        return render_template('results.html', prompts=prompts)

    return render_template('index.html')

@app.route('/add_prompt', methods=['GET', 'POST'])
@login_required
def add_prompt():
    if request.method == 'POST':
        prompt_title = request.form['prompt_title']
        prompt_text = request.form['prompt_text']
        prompt_tags = request.form['prompt_tags'].split(',')

        new_prompt = {
            "title": prompt_title,
            "text": prompt_text,
            "tags": [tag.strip() for tag in prompt_tags]
        }

        from flask import Flask, render_template, request, redirect, url_for, jsonify, session, g
from pymongo import MongoClient
import json
from functools import wraps
import os

# Supabase
from supabase_py import create_client, Client

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://joshsoke:Freddy141823@prompt.wexmajs.mongodb.net/?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = "adgdVbBf2FGdhfgjhzxjklkl4dfsd35df34efdfaw4nsbdrtwafcerACSZH"

mongo = MongoClient(app.config["MONGO_URI"])
db = mongo.prompts_db

# Supabase configuration
SUPABASE_URL = "https://jlowomwkcdikzdgyuouv.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impsb3dvbXdrY2Rpa3pkZ3l1b3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODMzNDU2NTcsImV4cCI6MTk5ODkyMTY1N30.A0sPRme3fG0EKcQfyA_WbDHfRBqEuIwjV_j2o965XgY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Supabase login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = g.user
        if user is None:
            return redirect(url_for("index", next=request.url))
        return f(*args, **kwargs)

    return decorated_function

# Supabase user loader
@app.before_request
def load_user():
    user = None
    session_cookie = request.cookies.get("sb:session")
    if session_cookie:
        user = supabase.auth.api.get_user(session_cookie)
    g.user = user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search_query']
        tag_filter = request.form['tag_filter']

        search_conditions = {
            "$or": [
                {"title": {"$regex": search_query, "$options": "i"}},
                {"text": {"$regex": search_query, "$options": "i"}},
                {"tags": {"$regex": search_query, "$options": "i"}}
            ]
        }

        if tag_filter:
            search_conditions["tags"] = {"$regex": tag_filter, "$options": "i"}

        prompts = db.prompts.find(search_conditions)
        return render_template('results.html', prompts=prompts)

    return render_template('index.html')

@app.route('/add_prompt', methods=['GET', 'POST'])
@login_required
def add_prompt():
    if request.method == 'POST':
        prompt_title = request.form['prompt_title']
        prompt_text = request.form['prompt_text']
        prompt_tags = request.form['prompt_tags'].split(',')

        new_prompt = {
            "title": prompt_title,
            "text": prompt_text,
            "tags": [tag.strip() for tag in prompt_tags]
        }

        db.prompts.insert_one(new_prompt)
        return redirect(url_for('index'))
    
    return render_template('add_prompt.html')



@app.route('/tags', methods=['GET'])
def get_tags():
    tags = set()
    for prompt in db.prompts.find():
        tags.update(prompt["tags"])

    return jsonify(sorted(tags))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    result = supabase.auth.sign_in(email=email, password=password)

    if 'error' in result:
        return jsonify({"error": result['error']['message']})
    else:
        session['user'] = result['data']
        response = jsonify({"message": "Logged in successfully."})
        response.set_cookie("sb:session", result['data']['access_token'])
        return response

@app.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        del session['user']
        response = jsonify({"message": "Logged out successfully."})
        response.delete_cookie("sb:session")
        return response
    else:
        return jsonify({"error": "No user is currently logged in."})

if __name__ == '__main__':
    app.run(debug=True)