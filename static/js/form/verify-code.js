const button_code = document.getElementById("submit-code")
function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}
button_code.addEventListener("click",function(){
    const otpcode = document.getElementById("otp-code").value
    const url = get_url_home() + "/accounts/api/verify-code/";
    const Http = new XMLHttpRequest();
    const formData = new FormData();
    formData.append('code', otpcode);
    Http.open("POST", url);
    Http.send(formData);
    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4) {
            if (Http.status == 201) {
                window.location.replace(get_url_home()+"/accounts/address/create/");
            } else {
                console.error("Failed to register:", Http.responseText);
            }
        }
    }
})