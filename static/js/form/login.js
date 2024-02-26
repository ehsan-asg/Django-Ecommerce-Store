
function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}

const currentUrl = window.location.href;
if (get_url_home() + "/accounts/login/" == currentUrl){
    const button_login = document.getElementById("button-login")
    button_login.addEventListener("click",function(){
        const phone = document.getElementById("phone_number").value
        const password = document.getElementById("password-account").value
        const url = get_url_home() + "/accounts/token/";

        const formData = new FormData();
        formData.append('phone_number', phone);
        formData.append('password', password);
    });
}
