// var url = "http://localhost:4000/api/";
var url = window.location.origin + '/api/';
var user_email = localStorage.getItem("email");

$(document).ready(function () {

    displayUserData();

    console.log("User email: ", user_email);
    console.log("URL: ", url);

    $('#saveCampaignBtn').on('click', function (event) {

        console.log("🚀 ~ Line 14 ~  :  ");

        event.preventDefault();
        event.stopPropagation();


        var cname = $('#campaign-name').val();
        var message = $('#campaign-message').val();
        var contactsArray = getSelectedNumbers();

        console.log("🚀 ~ Line 23 ~ contactsArray", contactsArray)
        console.log("🚀 ~ Line 23 ~ message", message)
        console.log("🚀 ~ Line 23 ~ cname", cname)


        if (cname == '' || message == '' || contactsArray.length == 0) {
            alert('Please fill all the fields');
            return;
        }
        else {

            $.ajax({
                url: url + 'send_bulk_sms',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    "email": user_email,
                    "name": cname,
                    "message": message,
                    "numbers": contactsArray
                }),
                success: function (response) {
                    console.log("🚀🚀🚀 ~ response", response)
                    alert('message sent successfully');
                    $('#campaign-name').val('');
                    $('#campaign-message').val('');
                    $('#pid-all').prop('checked', false);
                    $('[id^="pid-"]').prop('checked', false);

                },
                error: function (error) {
                    console.log("🚀🚀🚀 ~ error", error)
                    alert('Error sending message');
                }
            });



        }




    })

    $('#pid-all').on('change', function () {
        // Get the state of the "Select All" checkbox
        var isChecked = $(this).prop('checked');

        // Set the state of all other checkboxes accordingly
        $('[id^="pid-"]').prop('checked', isChecked);



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
                           
                        </tr>
                    `;
                }

                $('#contacts-table').append(html);

            }

        },
    });
}

function getSelectedNumbers() {
    var selectedNumbers = [];
    $('[id^="pid-"]').each(function () {
        // Check if the checkbox is checked
        if ($(this).prop('checked')) {
            // Extract the number from the corresponding span element
            var number = $(this).closest('tr').find('.nk-tb-col.tb-col-lg span').text();

            // Add the number to the array
            if (number.length >= 10) {

                selectedNumbers.push(number);
            }
        }
    });
    return selectedNumbers;
}