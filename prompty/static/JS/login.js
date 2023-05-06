
const supabaseUrl = "https://jlowomwkcdikzdgyuouv.supabase.co";
const supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impsb3dvbXdrY2Rpa3pkZ3l1b3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODMzNDU2NTcsImV4cCI6MTk5ODkyMTY1N30.A0sPRme3fG0EKcQfyA_WbDHfRBqEuIwjV_j2o965XgY";
const supabase = createClient(supabaseUrl, supabaseAnonKey);

async function login(email, password) {
    const { user, error } = await supabase.auth.signIn({ email, password });
    if (error) {
        console.error("Error logging in:", error.message);
        alert("Failed to log in: " + error.message);
    } else {
        console.log("Logged in as:", user.email);
        location.reload();
    }
}

document.getElementById("login-submit").addEventListener("click", async (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    await login(email, password);
});

// Code to open the login modal
document.getElementById("login-toggle").addEventListener("click", () => {
  document.getElementById("login-modal").classList.add("is-active");
});

// Code to close the login modal
document.getElementById("login-modal-close").addEventListener("click", () => {
  document.getElementById("login-modal").classList.remove("is-active");
});

document.getElementById("login-cancel").addEventListener("click", () => {
  document.getElementById("login-modal").classList.remove("is-active");
});
