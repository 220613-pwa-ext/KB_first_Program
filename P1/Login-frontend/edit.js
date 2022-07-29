let idInput = document.getElementById('id-input');
let ratingInput = document.getElementById('rating-input');
let updateSubmitButton = document.getElementById('update-btn');


updateSubmitButton.addEventListener('click', async () =>{ 
    let res = await fetch(`http://127.0.0.1:5050/employee_reimbs/${idInput.value}/${ratingInput.value}`, {
        'credentials': 'include',
        'method': 'PUT',
        })
        let data = await res.json();
    if(res.status==200){
        window.location.href = 'reimbsf.html';
    }});
