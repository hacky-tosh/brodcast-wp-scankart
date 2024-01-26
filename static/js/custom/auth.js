$(document).ready(function () {
    // Your code here
    const url = "http://127.0.0.1:4000/api/"
    console.log("🚀 ~ Line 3 ~  :  ");

    $('#login').on('click', function () {
        var email = $('#email').val();
        var password = $('#password').val();
        $.ajax({
            url: url + 'login',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ email: email, password: password }),
            success: function (response) {
                console.log("🚀 ~ Line 25 ~  : response ", response);
                localStorage.setItem("token", response.token);
                localStorage.setItem("email", response.email);
                window.location.href = '/dashboard';


            }, error: function (response) {
                console.log("🚀 ~ Line 212 ~  : response ", response);

            }
        });

    });

    $('#signup-btn').on('click', function (event) {

        var name = $('#signup-name').val();
        var email = $('#signup-email').val();
        var password = $('#signup-password').val();

        $.ajax({

            url: url + 'signup',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ name: name, email: email, password: password }),
            success: function (response) {
                console.log("🚀 ~ Line 25 ~  : response ", response);
                // windows.location.href = '/user/login';
                event.preventDefault();
                event.stopPropagation();
                event.stopImmediatePropagation();       
            }
        });

    });

});