const url = "http://localhost:4000/api/";
const user_email = localStorage.getItem("email");
$(document).ready(function () {
    displayUserData();



    $('#pid-all').on('change', function () {
        // Get the state of the "Select All" checkbox
        var isChecked = $(this).prop('checked');

        // Set the state of all other checkboxes accordingly
        $('[id^="pid-"]').prop('checked', isChecked);
    });

    $('#singleContactUpload').on('click', function () {
        let name = $('#contact-form-name').val();
        let number = $('#contact-form-number').val();
        let user_email = "bankashu74@gmail.com"
        if (!name || !number) {
            alert("Please enter all the fields");
            return;
        }
        let data = {
            "name": name,
            "number": number,
            "user_email": user_email
        }
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
        let user_email = "bankashu74@gmail.com";
        let formData = new FormData();
        formData.append('file', file);
        formData.append('user_email', user_email);
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

});


function displayUserData() {
    $.ajax({
        url: url + 'get-contacts',
        type: 'GET',
        dataType: 'json',
        data: {
            "email": "bankashu74@gmail.com"
        },
        success: function (response) {
            console.log(response);
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
        },
    });
}