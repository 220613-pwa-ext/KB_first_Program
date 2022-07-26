let usernameInput = document.getElementById('username-input');
let passwordInput = document.getElementById('password-input');
let firstNameInput = document.getElementById('firstName-input');
let lastNameInput = document.getElementById('lastName-input');
let phoneInput = document.getElementById('phone-input');
let emailInput = document.getElementById('email-input');
let genderButtons = document.getElementById('input[name="gender"]');
let roleButtons = document.getElementById('input[name="role"]');
let registrationSubmitButton = document.getElementById('register-submit-btn');


registrationSubmitButton.addEventListener('click', async () =>{ 

    let selectedBtn;
    for(let radioBtn of genderButtons){
        if (radioBtn.checked){
            selectedBtn = radioBtn
            break;
        }
    }

    let selectedBtn2;
    for(let radioBtn of roleButtons){
        if (radioBtn.checked){
            selectedBtn2 = radioBtn
            break;
        }
    }

    let res = await fetch('http://127.0.0.1:5500/Login-frontend/registration', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'},
            'body': JSON.stringfyi({
                "username": usernameInput.value,
                "password": passwordInput.value,
                "firstName": firstNameInput.value,
                "lastName": lastNameInput.value,
                "phone_number": phoneInput.value,
                "gender": selectedBtn.value,
                "email": emailInput.value,
                "role": selectedBtn2.value,
            })
        })
        if(res.status==201){
            window.location.href = 'homepage.html'
        }else if (res.status ==400){
            let data = await res.json();

            let registrationErrorMessage = ducoment.getElementById('registration-error-messages')
            registrationErrorMessage.innerHTML = '';

            let errorMessages = data.messages;
            for(let errorMessage of errorMessages) {
                let errorElement = document.createElement('p');
                errorElement.innerHTML = errorMessage;
                errorElement.style.color = 'red';
                errorElement.style.fontweight = 'bold';

                registrationErrorMessage.appendChild(errorElement);
            }
        }
    });
