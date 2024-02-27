function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}
const storedTokens = localStorage.getItem('tokens'); 
const tokens = JSON.parse(storedTokens);
const token_access = tokens.access;

if (window.location.href === get_url_home() + "/shopping/") {
    const url = get_url_home() + "/api/address/detail/";
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.setRequestHeader("Authorization", "Bearer " + token_access); 
    xhr.send();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                const responseObject = JSON.parse(xhr.responseText);
                
                const fullNameElement = document.querySelector(".full-name");
                const mobilePhoneElement = document.querySelector(".mobile-phone");
                const postCodeElement = document.querySelector(".post-code");
                const stateElement = document.querySelector(".state");
                const cityElement = document.querySelector(".city");
                const addressPartElement = document.querySelector(".address-part");
                console.log(responseObject)
                for (let x in responseObject) {
                fullNameElement.textContent = responseObject[x]['city'];
                }
            } else {
                console.error("Failed to fetch address details:", xhr.responseText);
            }
        }
    };
}

document.getElementById("submit-button-address").addEventListener("click", function() {
    const state = document.getElementById("state").value;
    const city = document.getElementById("city").value;
    const street = document.getElementById("street").value;
    const zip_code = document.getElementById("zip_code").value;
    const plate = document.getElementById("plate").value;
    const unit = document.getElementById("unit").value;

    const forminputData = {
        state: state,
        city: city,
        street: street,
        zip_code: zip_code,
        plate: plate,
        unit: unit
    };

    const formData = new FormData();
    formData.append('state', forminputData['state']);
    formData.append('street', forminputData['street']);
    formData.append('city',forminputData['city']);
    formData.append('zip_code',forminputData['zip_code']);
    formData.append('plate',forminputData['plate']);
    formData.append('unit',forminputData['unit'])
    const url = get_url_home() + "/api/address/create";
    const Http = new XMLHttpRequest();
    Http.open("POST", url);
    Http.setRequestHeader("Authorization", "Bearer " + token_access); 
    Http.send(formData);
    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4) {
            if (Http.status == 201) {
                console.log("success");
            } else {
                console.error("Failed to register:", Http.responseText);
            }
        }
    };

    
});

