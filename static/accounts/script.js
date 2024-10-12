const form = document.querySelector('form');
const emailField = form.querySelector('input[name="email"]');
const passwordField = form.querySelector('input[name="password"]');

form.addEventListener('submit', (event) => {
    const email = emailField.value;
    const password = passwordField.value;

    if (!validateEmail(email) || password.length < 6) {
        event.preventDefault(); // Prevent form submission if validation fails
        alert('Invalid email or password should be at least 6 characters.');
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}