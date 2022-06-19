// let form = document.querySelector('.js_form'),
//     formInputs = document.querySelectorAll('.js_input'),
//     inputEmail = document.querySelector('.js_input_email'),
//     submitBtn = document.querySelector('form_btn');

//     let popUp = document.getElementById('pop_up'),
//     popupToggle = document.getElementById('validate'),
//     popupClose = document.querySelector('.close'),
//     span = document.querySelector('.empty_mes');


// function validateEmail(email) {
//     const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     return re.test(email.toLowerCase());
// }

// inputEmail.onblur = function() {
//     if(!validateEmail(inputEmail.value)) {
//         console.log('email not valid');
//         inputEmail.classList.add('error');
//         popUp.style.display = "grid";
//         setTimeout(() => {
//             popUp.style.display = "none";
//         }, 2000);
//         return false;
//     } else {
//         inputEmail.classList.remove('error');
//     }
// };





// form.onsubmit = function() {
//     // submitBtn.onsubmit.preventDefault();


//     popupClose.onclick = function() {
//         popUp.style.display = "none";
//     };

//     let emailVal = inputEmail.value,
//         emptyInputs = Array.from(formInputs).filter(input => input.value === '');


//     formInputs.forEach(function(input) {
//         if(input.value === ''){
//             input.classList.add("error");
//             document.getElementById('span_one').style.display = "block";
//             document.getElementById('span_two').style.display = "block";
//             document.getElementById('span_three').style.display = "block";
//             document.getElementById('span_four').style.display = "block";

//         } else {
//             console.log("filled");

//             input.classList.remove("error");
//             document.getElementById('span_one').style.display = "none";
//             document.getElementById('span_two').style.display = "none";
//             document.getElementById('span_three').style.display = "none";
//             document.getElementById('span_four').style.display = "none";

//         }
//     });

//     if(emptyInputs.length !== 0){
//         console.log("inputs not filled");
//         return false;
//     }

//     if(!validateEmail(emailVal)) {

//         console.log('email not valid');
//         inputEmail.classList.add('error');
//         popUp.style.display = "grid";

//         setTimeout(() => {
//             popUp.style.display = "none";
//         }, 2000);

//         return false;

//     } else {
//         inputEmail.classList.remove('error');
//         span.style.display = "none";
//     }



// };





// function Init () {
//     let submitBtn = document.getElementById('validate');
//     submitBtn.addEventListener( 'onclick', afterSubmit, false );
// }

// function afterSubmit(evt) {
//     evt.preventDefault();

//     $(document).ajaxStart(function () {
//         $("#validate").attr("disabled", true);
//     });
//     $(document).ajaxComplete(function () {
//         $("#validate").attr("disabled", false);
//     });

// }




function surname_imput() {
    if (document.getElementById("surname_imput").value == '') {
        document.getElementById("surname_imput").style.background = "rgba(255, 40, 40, 0.4)";
        // document.getElementById("surname_imput").style.color = "#fff";
        document.getElementById("surname_imput").placeholder = '*Обов\'язкове поле*';
        document.getElementById("text_mistake_surname").style.display = 'none';
        return false;
    }
    if (!document.getElementById("surname_imput").value.match(/[0-9]/)) {
        document.getElementById("surname_imput").style.background = "white";
        document.getElementById("surname_imput").placeholder = '';
        document.getElementById("text_mistake_surname").style.display = 'none';
        return true;
    }
    // if(document.getElementById("surname_imput").value.match(/[0-9]/)){
    //     document.getElementById("text_mistake_surname").style.display = 'block';

    // }
    document.getElementById("surname_imput").style.background = "rgba(255, 40, 40, 0.4)";
    document.getElementById("text_mistake_surname").style.display = 'inline';
    return false;
}
function name_imput() {
    if (document.getElementById("name_imput").value == '') {
        document.getElementById("name_imput").style.background = "rgba(255, 40, 40, 0.4)";
        document.getElementById("name_imput").placeholder = '*Обов\'язкове поле*';
        document.getElementById("text_mistake_name").style.display = 'none';
        return false;
    }
    if (!document.getElementById("name_imput").value.match(/[0-9]/)) {
        document.getElementById("name_imput").style.background = "white";
        document.getElementById("name_imput").placeholder = '';
        document.getElementById("text_mistake_name").style.display = 'none';
        return true;
    }
    document.getElementById("name_imput").style.background = "rgba(255, 40, 40, 0.4)";
    document.getElementById("text_mistake_name").style.display = 'inline';
    return false;
}
function patronymic_imput() {
    if (!document.getElementById("patronymic_imput").value.match(/[0-9]/)) {
        document.getElementById("text_mistake_patronymic").style.display = 'none';
        return true;
    }
    document.getElementById("text_mistake_patronymic").style.display = 'inline';
    return false;
}
function phone_imput() {
    if (document.getElementById("phone_imput").value == '') {
        document.getElementById("phone_imput").style.background = "#fff";
        document.getElementById("phone_imput").placeholder = '*Обов\'язкове поле*';
        document.getElementById("text_mistake_phone").style.display = 'none';
        return false;
    }
    if (!document.getElementById("phone_imput").value.match(/[A-Z]/) &&
        !document.getElementById("phone_imput").value.match(/[a-z]/) &&
        !document.getElementById("phone_imput").value.match(/[А-Я]/) &&
        !document.getElementById("phone_imput").value.match(/[а-я]/)) {
        document.getElementById("phone_imput").style.background = "white";
        document.getElementById("phone_imput").placeholder = '';
        document.getElementById("text_mistake_phone").style.display = 'none';
        return true;
    }
    document.getElementById("phone_imput").style.background = "rgba(255, 40, 40, 0.4)";
    document.getElementById("text_mistake_phone").style.display = 'inline';
    return false;
}
function date_imput() {
    if (document.getElementById("date_imput").value == '') {
        document.getElementById("date_imput").style.background = "rgba(255, 40, 40, 0.4)";
        return false;
    }
    document.getElementById("date_imput").style.background = "white";
    return true;
}
function time_imput() {
    if (document.getElementById("time_imput").value == '') {
        document.getElementById("time_imput").style.background = "rgba(255, 40, 40, 0.4)";
        document.getElementById("time_imput").placeholder = '*Обов\'язкове поле*';
        return false;
    }
    document.getElementById("time_imput").style.background = "white";
    document.getElementById("time_imput").placeholder = '';
    return true;
}
function service_imput() {
    if (document.getElementById("service_imput").value == '') {
        document.getElementById("service_imput").style.background = "rgba(255, 40, 40, 0.4)";
        document.getElementById("service_imput").placeholder = '*Обов\'язкове поле*';
        return false;
    }
    document.getElementById("service_imput").style.background = "white";
    document.getElementById("service_imput").placeholder = '';
    return true;
}

var accept = true;

console.log(accept == true);

function reset(){
    document.getElementById("surname_imput").style.background = "white";
    document.getElementById("surname_imput").placeholder = '';
    document.getElementById("surname_imput").value = '';
    document.getElementById("text_mistake_surname").style.display = 'none';

    document.getElementById("name_imput").style.background = "white";
    document.getElementById("name_imput").placeholder = '';
    document.getElementById("name_imput").value = '';
    document.getElementById("text_mistake_name").style.display = 'none';

    document.getElementById("patronymic_imput").value = '';
    document.getElementById("text_mistake_patronymic").style.display = 'none';

    document.getElementById("phone_imput").style.background = "white";
    document.getElementById("phone_imput").placeholder = "8-800-555-35-35";
    document.getElementById("phone_imput").value = '';
    document.getElementById("text_mistake_phone").style.display = 'none';

    document.getElementById("date_imput").style.background = "white";
    document.getElementById("date_imput").value = '';

    document.getElementById("time_imput").style.background = "white";
    document.getElementById("time_imput").placeholder = "Виберіть час заселення";
    document.getElementById("time_imput").value = '';

    document.getElementById("service_imput").style.background = "white";
    document.getElementById("service_imput").placeholder = "Виберіть кімнату";
    document.getElementById("service_imput").value = '';

    if(accept == true){
        window.localStorage.clear();
    }

}

function cheak_info() {
    if(surname_imput() && name_imput() && patronymic_imput() && phone_imput()
    && date_imput() && time_imput() && service_imput()) {
        document.getElementById("hidden").style.display = 'block';
        document.getElementById("hidden_window").style.display = 'block';
    }

    if(accept == true){
        if (window.sessionStorage && window.localStorage){
          localStorage.setItem("surname", document.getElementById("surname_imput").value);
          localStorage.setItem("name", document.getElementById("name_imput").value);
          localStorage.setItem("patronymic", document.getElementById("patronymic_imput").value);
          localStorage.setItem("phone", document.getElementById("phone_imput").value);
          localStorage.setItem("time", document.getElementById("time_imput").value);
          localStorage.setItem("service", document.getElementById("service_imput").value);
        }
        else{
          alert("Локальное хранилище не доступно!");
        }

    }
}

function close_window() {
    document.getElementById("hidden").style.display = 'none';
    document.getElementById("hidden_window").style.display = 'none';

    document.getElementById("submit_1").style.display = 'none';
    document.getElementById("submit_2").style.display = 'none';

    document.getElementById("surname_imput").disabled="disabled";
    document.getElementById("name_imput").disabled="disabled";
    document.getElementById("patronymic_imput").disabled="disabled";
    document.getElementById("phone_imput").disabled="disabled";
    document.getElementById("date_imput").disabled="disabled";
    document.getElementById("time_imput").disabled="disabled";
    document.getElementById("service_imput").disabled="disabled";
}

window.addEventListener("load", function(event){
    accept=confirm("Сторінка використовує локальне сховище для зберігання останньої інформації про бронювання. Дозволити?");
    if(accept == true){
        if (localStorage.getItem("surname") != null)
            document.getElementById("surname_imput").placeholder = localStorage.getItem("surname");
        if (localStorage.getItem("name") != null)
            document.getElementById("name_imput").placeholder = localStorage.getItem("name");
        if (localStorage.getItem("patronymic") != null)
            document.getElementById("patronymic_imput").placeholder = localStorage.getItem("patronymic");
        if (localStorage.getItem("phone") != null)
            document.getElementById("phone_imput").placeholder = localStorage.getItem("phone");
        if (localStorage.getItem("time") != null)
            document.getElementById("time_imput").placeholder = localStorage.getItem("time");
        if (localStorage.getItem("service") != null)
            document.getElementById("service_imput").placeholder = localStorage.getItem("service");
    }
});
