document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-btn").addEventListener("click", function() {
    const url = 'http://127.0.0.1:5000/login';  // API endpoint URL
    const myEmail = document.getElementById("email").value;
    const myPassword = document.getElementById("password").value;

    const data = {
    email: myEmail,
    password: myPassword,
    };

    const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    };

    fetch(url, options)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not OK');
        }
        return response.json();
    })
    .then(data => {
        // Handle the response data
        console.log(data);
        if (data.success) {
            // Redirect to the desired page
            window.location.href = '/whatweoffer'; // Replace with your desired page URL
        }
    })
    .catch(error => {
        // Handle network or server-related errors
        console.error(error);
    });
});
});
