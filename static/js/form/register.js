const button = document.getElementById("submit-button");

function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}

button.addEventListener("click", function() {
    const phone = document.getElementById("phone_number").value;
    const name = document.getElementById("full_name").value;
    const passw = document.getElementById("password").value;

    const url = get_url_home() + "/accounts/api/register/";

    const formData = new FormData();
    formData.append('phone_number', phone);
    formData.append('full_name', name);
    formData.append('password', passw);

    const Http = new XMLHttpRequest();
    Http.open("POST", url);
    Http.send(formData);

    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4) {
            if (Http.status == 201) {
                window.location.replace(get_url_home()+"/accounts/verify");
            } else {
                console.error("Failed to register:", Http.responseText);
            }
        }
    }
});
