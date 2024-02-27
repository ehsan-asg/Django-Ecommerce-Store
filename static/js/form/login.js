const currentUrl = window.location.href;
function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}
if (get_url_home() + "/accounts/login/" == currentUrl){
    const button_login = document.getElementById("button-login")
    button_login.addEventListener("click",function(){
        const phone = document.getElementById("phone_number").value
        const password = document.getElementById("password-account").value
        const url = get_url_home() + "/accounts/token/";
          console.log(url)
        axios.post(url, {
            phone_number: phone,
            password: password
        })
        .then(response => {
            localStorage.setItem('tokens', JSON.stringify(response.data));
            authenticat()
            window.location.replace(get_url_home()+"/accounts/profile");
        })
    });
}
