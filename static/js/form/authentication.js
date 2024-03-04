function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}
function getCategorySlugFromURL() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/');
    const categorySlug = parts[parts.length - 2]; 
    return categorySlug;
}
const storedTokens = localStorage.getItem('tokens'); 
function authenticat(callback) {
    if (storedTokens) {
        const tokens = JSON.parse(storedTokens);
        const token_access = tokens.access;
        const token_refresh = tokens.refresh;
        const url = get_url_home() + "/accounts/api/user";

        const xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.setRequestHeader("Authorization", "Bearer " + token_access);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    const formResponse = {
                        phone: response.phone_number,
                        email: response.email,
                        full_name: response.full_name,
                        address: response.address
                    };
                    const formResponseString = JSON.stringify(formResponse);
                    localStorage.setItem('user_data', formResponseString);
                    callback(true);
                } else {
                    const url_refresh = get_url_home() + "/accounts/token/refresh/";
                    const xhr_refresh = new XMLHttpRequest(); 
                    const formDatarefresh = new FormData();
                    formDatarefresh.append('refresh', token_refresh);
                    xhr_refresh.open("POST", url_refresh);   
                    xhr_refresh.onreadystatechange = function() {
                        if(xhr_refresh.readyState === XMLHttpRequest.DONE && xhr_refresh.status === 200){
                            const response = JSON.parse(xhr_refresh.responseText);
                            const newAccessToken = response.access;
                            const newRefreshToken = response.refresh;
                            localStorage.setItem('tokens', JSON.stringify({ access: newAccessToken, refresh: newRefreshToken }));
                            authenticat(callback);
                        } else {
                            localStorage.removeItem("tokens");
                            localStorage.removeItem("user_data");
                            callback(false);
                        }
                    };
                    xhr_refresh.send(formDatarefresh);
                }
            }
        };
        xhr.send();
    }else{
        if (window.location.href !== get_url_home() + "/accounts/login/"){
            window.location.replace(get_url_home() + "/accounts/login");
        }
        

    }
}
function getCategorySlugFromURL() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/');
    const categorySlug = parts[parts.length - 2]; 
    return categorySlug;
}
if (window.location.href === get_url_home() + "/accounts/login/") {
    authenticat(function(success) {
        if (success) {
            window.location.replace(get_url_home() + "/accounts/profile");
        }
    });
}else if(window.location.href === get_url_home() + "/accounts/register/"){
    if (storedTokens){
        authenticat(function(success) {
            if (success) {
                window.location.replace(get_url_home() + "/accounts/profile");
            }
        });
    }
}else if(window.location.href === get_url_home() + "/accounts/login/?next=/accounts/logout/"){
    localStorage.removeItem("tokens");
    localStorage.removeItem("user_data");
    window.location.replace(get_url_home());
}else if(getCategorySlugFromURL() === "profile"){
    console.log(getCategorySlugFromURL)
    authenticat(function(success) {
        if (!success) {
            window.location.replace(get_url_home() + "/accounts/login");
        }
    });
}