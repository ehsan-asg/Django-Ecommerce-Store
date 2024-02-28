function get_url_home() {
    let main_url = window.location.protocol;
    main_url += "//" + window.location.host;
    return main_url;
}
const storedTokens = localStorage.getItem('tokens'); 
const tokens = JSON.parse(storedTokens);
const token_access = tokens.access;

if (window.location.href === get_url_home() + "/shopping/") {
    var responseObject = {}
    const url = get_url_home() + "/api/address/detail/";
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.setRequestHeader("Authorization", "Bearer " + token_access); 
    xhr.send();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                 responseObject = JSON.parse(xhr.responseText);
                //address-section
                const fullNameElement = document.querySelector(".full-name");
                const mobilePhoneElement = document.querySelector(".mobile-phone");
                const postCodeElement = document.querySelector(".post-code");
                const stateElement = document.querySelector(".state");
                const cityElement = document.querySelector(".city");
                const addressPartElement = document.querySelector(".address-part");
                //checkout-address-row
                  const checkout_address = document.querySelector(".page-content ")
                //loop address

                if (Object.keys(responseObject).length == 0){
                    window.location.replace(get_url_home()+"/accounts/profile/address");
                }else{

                    document.querySelector(".address-section").innerHTML = `<div class="checkout-contact dt-sn dt-sn--box border px-0 pt-0 pb-0">
                    <div class="checkout-contact-content">
                        <ul class="checkout-contact-items">
                            <li class="checkout-contact-item">
                                گیرنده:
                                <span class="full-name">${responseObject[0]['user']['full_name']}</span>
                            </li>
                            <li class="checkout-contact-item">
                                <div class="checkout-contact-item checkout-contact-item-mobile">
                                    شماره تماس:
                                    <span class="mobile-phone">${responseObject[0]['user']['phone_number']}</span>
                                </div>
                                <div class="checkout-contact-item-message">
                                    کد پستی:
                                    <span class="post-code">${responseObject[0]['zip_code']}</span>
                                </div>
                                <br>
                                استان
                                <span class="state">${responseObject[0]['state']}</span>
                                ، &zwnj;شهر
                                <span class="city">${responseObject[0]['city']}</span>
                                ،
                                <span class="address-part">${responseObject[0]['street']}</span>
                            </li>
                        </ul>
                        <div class="checkout-contact-badge">
                            <i class="mdi mdi-check-bold"></i>
                        </div>
                    </div>
                    <div class="checkout-address dt-sn px-0 pt-0 pb-0" id="user-address-list-container">
                        <div class="checkout-address-content">
                            <div class="checkout-address-headline">آدرس مورد نظر خود را جهت تحویل
                                انتخاب فرمایید:</div>
                            <div class="checkout-address-row new-address">
                                <div class="checkout-address-col">
                                    <a href="/accounts/profile/address/" class="checkout-address-location">
                                        <strong>ایجاد آدرس جدید</strong>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <button class="checkout-address-cancel" id="cancel-change-address-btn"></button>
                    </div>
                    </div>`

                }


                for (let x in responseObject){
                    checkout_address.innerHTML +=`                                            <div class="checkout-address-row w-100 m-0">
                    <div class="checkout-address-col">
                        <div class="checkout-address-box is-selected">
                            <h5 class="checkout-address-title">${responseObject[x]['user']['full_name']}</h5>
                            <p class="checkout-address-text">
                                <span>${responseObject[x]['street']}</span>
                            </p>
                            <ul class="checkout-address-list">
                                <li>
                                    <ul class="checkout-address-contact-info">
                                        <li class="">کدپستی: <span class="zip_code">${responseObject[x]['zip_code']}</span></li>
                                        <li>شماره همراه: <span class="phone_number">${responseObject[x]['user']['phone_number']}</span>
                                        </li>
                                    </ul>
                                </li>
                                <li>
                                    <ul>
                                        <li>
                                            <a href="http://127.0.0.1:8000/accounts/profile/address/" class="checkout-address-btn-edit">ویرایش</a>
                                        </li>
                                        <li>
                                            <button data-id="${responseObject[x]['id']}" onclick="deleteaddress(this)" function class="checkout-address-btn-remove">حذف</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                            <button class="checkout-address-btn-submit" onclick="changeAddress(this)" data-id="${responseObject[x]["id"]}">سفارش به این آدرس
                                ارسال شود.</button>
                        </div>
                    </div>
                </div>`
                }

            } else {
                console.error("Failed to fetch address details:", xhr.responseText);
            }
        }
    };
    function deleteaddress(button) {
        const addressId = button.getAttribute("data-id");
        console.log(addressId) 
        const url = get_url_home() + "/api/address/delete/" + addressId;
        const request = new XMLHttpRequest();
        request.open("DELETE", url);
        request.setRequestHeader("Authorization", "Bearer " + token_access); 
    
        request.onreadystatechange = function() {
            location.reload();
        };
    
        request.send();
    }

    function changeAddress(button) {
        const addressId = parseInt(button.getAttribute("data-id"));
        const result = responseObject.find( obj => obj.id === addressId)
        const activeButton = document.querySelector(".checkout-address-btn-submit.is-select");
        if (activeButton !== null) {
            activeButton.classList.remove("is-select");
            activeButton.textContent = "سفارش به این آدرس ارسال می‌شود";
        }
        button.classList.add("is-select");
        button.textContent = "سفارش به این آدرس ارسال می شود"
        document.querySelector(".address-section").innerHTML = `<div class="checkout-contact dt-sn dt-sn--box border px-0 pt-0 pb-0">
        <div class="checkout-contact-content">
            <ul class="checkout-contact-items">
                <li class="checkout-contact-item">
                    گیرنده:
                    <span class="full-name">${result['user']['full_name']}</span>
                </li>
                <li class="checkout-contact-item">
                    <div class="checkout-contact-item checkout-contact-item-mobile">
                        شماره تماس:
                        <span class="mobile-phone">${result['user']['phone_number']}</span>
                    </div>
                    <div class="checkout-contact-item-message">
                        کد پستی:
                        <span class="post-code">${result['zip_code']}</span>
                    </div>
                    <br>
                    استان
                    <span class="state">${result['state']}</span>
                    ، &zwnj;شهر
                    <span class="city">${result['city']}</span>
                    ،
                    <span class="address-part">${result['street']}</span>
                </li>
            </ul>
            <div class="checkout-contact-badge">
                <i class="mdi mdi-check-bold"></i>
            </div>
        </div>
        <div class="checkout-address dt-sn px-0 pt-0 pb-0" id="user-address-list-container">
            <div class="checkout-address-content">
                <div class="checkout-address-headline">آدرس مورد نظر خود را جهت تحویل
                    انتخاب فرمایید:</div>
                <div class="checkout-address-row new-address">
                    <div class="checkout-address-col">
                        <a href="/accounts/profile/address/" class="checkout-address-location">
                            <strong>ایجاد آدرس جدید</strong>
                        </a>
                    </div>
                </div>
            </div>
            <button class="checkout-address-cancel" id="cancel-change-address-btn"></button>
        </div>
        </div>`

    
    }
    

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

