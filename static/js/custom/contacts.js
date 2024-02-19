var url = "http://localhost:4000/api/";
var user_email = localStorage.getItem("email");
$(document).ready(function () {

    displayUserData();






    $('#pid-all').on('change', function () {
        // Get the state of the "Select All" checkbox
        var isChecked = $(this).prop('checked');

        // Set the state of all other checkboxes accordingly
        $('[id^="pid-"]').prop('checked', isChecked);
    });

    $('#singleContactUpload').on('click', function (event) {

        event.preventDefault(); 
        if (validateForm()) {
            console.log("Form is valid. Proceed with further actions.");
        } else {
            console.log("Form validation failed. Please correct errors.");
            return;
        }


        let name = $('#contact-form-name').val();
        let number = $('#contact-form-number').val();
        let email = user_email

        let data = {
            "name": name,
            "number": number,
            "user_email": email
        }



        console.log(data);
        $.ajax({
            url: url + 'add-contact',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {

                displayUserData();
                $('#singleContactForm').modal('hide');
                alert("Contact added successfully");
            },
            error: function (err) {
                console.log(err);
                alert("Error in adding contact", err.message);
            }
        });

    });

    $('#upload-contact-btn').on('click', function () {

        let file = $('#excel-file-upload').prop('files')[0];
        if (!file) {
            alert("Please select a file to upload.");
            return;
        }
        if (!file.name.endsWith('.xlsx')) {
            alert("Please select a valid Excel file with .xlsx extension.");
            return;
        }
        let email = user_email;
        let formData = new FormData();
        formData.append('file', file);
        formData.append('user_email', email);
        console.log(formData);

        $.ajax({
            url: url + 'upload-contacts',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function (response) {

                displayUserData();
                $('#modalForm').modal('hide');
                alert("Contacts uploaded successfully");

            },
            error: function (err) {
                console.log(err);
                alert("Error in uploading contacts");
            }
        });
    });

    $('#dashSignout').on('click', function (event) {
        localStorage.clear();
        document.cookie = "Authorization" + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        window.location.href = '/user/login';
    });



});


function displayUserData() {
    $.ajax({
        url: url + 'get-contacts',
        type: 'GET',
        dataType: 'json',
        data: {
            "email": user_email
        },
        success: function (response) {
            console.log("🚀🚀🚀 ~ displayUserData ~ response:", response)

            
            if (response.length == 0) {
                $('#contacts-table').append('<tr ><td colspan="5">No contacts found</td></tr>');
                return;
            } else {
                $('#contacts-table').empty();
                
                let html = '';
                for (let i = 0; i < response.length; i++) {
                    html += `
                        <tr class="nk-tb-item">
                            <td class="nk-tb-col nk-tb-col-check">
                                <div class="custom-control custom-control-sm custom-checkbox notext">
                                    <input type="checkbox" class="custom-control-input" id="pid-0${i + 1}">
                                    <label class="custom-control-label" for="pid-0${i + 1}"></label>
                                </div>
                            </td>
                            <td class="nk-tb-col">
                                <div class="project-title">
                                    <div class="user-avatar sq bg-purple">
                                        <span>${response[i].name.slice(0, 2)}</span>
                                    </div>
                                    <div class="project-info">
                                        <h6 class="title">${response[i].name}</h6>
                                    </div>
                                </div>
                            </td>
                            <td class="nk-tb-col tb-col-lg"><span>${response[i].number}</span></td>
                            <td class="nk-tb-col"><span>${response[i].source}</span></td>
                            <td class="nk-tb-col"><span>${response[i].date_added.slice(0, 17)}</span></td>
                        </tr>
                    `;
                }

                $('#contacts-table').append(html);

            }

        },
    });

        

}


function validateForm() {
    let name = $('#contact-form-name').val();
    let number = $('#contact-form-number').val();

    // Clear previous error messages
    $('.error-message').remove();

    // Validation
    let isValid = true;
    if (!name) {
        $('#contact-form-name').after('<div class="error-message">Please enter your name</div>');
        isValid = false;
    }
    if (!number) {
        $('#contact-form-number').after('<div class="error-message">Please enter your whatsapp number</div>');
        isValid = false;
    }

    // Custom phone number validation
    if (number && !(/^\d+$/.test(number) && number.length >= 10 && number.length <= 13)) {
        $('#contact-form-number').after('<div class="error-message">Please enter a valid phone number between 10 and 13 digits.</div>');
        isValid = false;
    }

    return isValid;
}