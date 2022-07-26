let user_id = localStorage.getItem("id");

document.addEventListener('DOMContentLoaded', async () =>{ 
    let res = await fetch(`http://127.0.0.1:5050/employee_reimbs/${user_id}`, {
        'credentials': 'include',
        'method': 'GET'}).then(res=>{
            return res.json();
        }).then(dat=>{
            for(let l=0; l<dat['reimbs'].length;l++){
                addReimbToTable(JSON.parse(JSON.stringify(dat['reimbs'][l])))
            }
        });

     if (res.status ==400){
        let loginErrorMessage = document.getElementById('login-error-messages')
        loginErrorMessage.innerHTML = '';
        let errorMessages = data2.messages;
        for(let errorMessage of errorMessages) {
            let errorElement = document.createElement('p');
            errorElement.innerHTML = errorMessage;
            errorElement.style.color = 'red';
            errorElement.style.fontweight = 'bold';
            loginErrorMessage.appendChild(errorElement);
            }
        }
    });


function addReimbToTable(reimb){
    let reimbTbodyElement = document.querySelector('#table tbody');

    let row = document.createElement('tr');
    let amount = document.createElement('td');
    amount.innerText = reimb.reimb_amount;
    let time_submit = document.createElement('td');
    time_submit.innerHTML = reimb.submitted;
    let time_resolved = document.createElement('td');
    if(reimb.resolved==null){
        time_resolved.innerHTML = "n/a"
    }else{
        time_resolved.innerHtml = reimb.resolved;
    }
    let statu = document.createElement('td');
    statu.innerHTML = reimb.status;
    let ty = document.createElement('td');
    ty.innerHTML = reimb.type;
    let descr = document.createElement('td');
    descr.innerHTML = reimb.description;
    let receipt = document.createElement('td');
    if(reimb.receipt==null){
        receipt.innerHTML = "N/A";
    }else{
        receipt.innerHTML = reimb.receipt;
    }
    let auth = document.createElement('td');
    auth.innerHTML = reimb.reimb_author;
    let resol = document.createElement('td');
    if(reimb.reimb_resolver==null){
        resol.innerHTML = "n/a";
    }else{
        resol.innerHTML = reimb.reimb_resolver;
    }
    row.appendChild(amount);
    row.appendChild(time_submit);
    row.appendChild(time_resolved);
    row.appendChild(statu);
    row.appendChild(ty);
    row.appendChild(descr);
    row.appendChild(receipt);
    row.appendChild(auth);
    row.appendChild(resol);
    reimbTbodyElement.appendChild(row);
}