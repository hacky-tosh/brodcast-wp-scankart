$(document).ready(function () {
    // Your code here
    const url = "http://127.0.0.1:4000/api/"
    console.log("🚀 ~ Line 3 ~  :  ");

    $('#login').on('click', function (event) {
       event.preventDefault();
        var email = $('#email').val();
        var password = $('#password').val();
        $.ajax({
            url: url + 'login',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ email: email, password: password }),
            success: function (response) {
                console.log("🚀 ~ Line 25 ~  : response ", response);
                let token = response.token;
                document.cookie = 'Authorization=' + encodeURIComponent(token) + '; path=/';
                localStorage.setItem("token", response.token);
                localStorage.setItem("email", response.email);
                window.location.href = '/user/list-customers';
            },
            error: function (response) {
                console.log("🚀 ~ Line 212 ~  : response ", response);
            }
        });
    });


    $('#signup-btn').on('click', function (event) {

        event.preventDefault();

        var name = $('#signup-name').val();
        var email = $('#signup-email').val();
        var password = $('#signup-password').val();

        $.ajax({
            url: url + 'signup',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ name: name, email: email, password: password }),
            success: function (response) {
                window.location.href = '/user/login';
            }
        });

    });




});