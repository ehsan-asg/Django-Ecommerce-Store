
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

        axios.post(url, formData)
            .then(response => {
                const tokenData = response.data;
                localStorage.setItem('access_token', tokenData.access);
                localStorage.setItem('refresh_token', tokenData.refresh);
                
                const access_token = localStorage.getItem('access_token');
                const refresh_token = localStorage.getItem('refresh_token');
                
                const headers = {
                  'Content-Type': 'application/json',
                  Authorization: `Bearer ${access_token}`,
                };
                
                axios.get('http://127.0.0.1:8000/accounts/api/user', { headers })
                  .then(response => console.log(response.data))
                  .catch(error => console.log(error));
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
}
