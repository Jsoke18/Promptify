document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('#theme-toggle');
  
    themeToggle.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');
      themeToggle.classList.toggle('is-light');
      themeToggle.classList.toggle('is-dark');
    });
  });
  