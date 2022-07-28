let usernameInput = document.getElementById('username-input');
let passwordInput = document.getElementById('password-input');
let loginSubmitButton = document.getElementById('login-btn');


if(usernameInput){
    loginSubmitButton.addEventListener('click', async () =>{ 
        let res = await fetch('http://127.0.0.1:5050/login', {
            'credentials': 'include',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'
            },
                'body': JSON.stringify({
                    "username": usernameInput.value,
                    "password": passwordInput.value
                })
            })
            let data = await res.json();
        if(res.status==200){
            localStorage.setItem("id", data['u_id']);
            window.location.href = 'reimbs.html';
        }})};