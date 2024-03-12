const couponButton = document.getElementById("button-coupon");
const payButton = document.getElementById("button-payment")
couponButton.addEventListener("click", function() {
    const couponCode = document.getElementById("code-coupon").value;
    const apiUrl = get_url_home() + "/api/coupon/check/" + couponCode + "/";

    fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token_access}`
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {

        if(localStorage.getItem('coupon')){
            alert("تخفیف قبلا اعمل شده");
        }else{
            localStorage.setItem('coupon', JSON.stringify(data));
            const cartData = JSON.parse(localStorage.getItem('cart'));
            cartData.forEach(element => {
                discount_price = element.price * data.discount / 100
                element.price = element.price - discount_price
            });
            localStorage.setItem('cart', JSON.stringify(cartData));
            displayCartProductItems()
        }

        })
    .catch(error => {
        console.error('There was a problem with your fetch operation:', error);
    });
});
payButton.addEventListener("click",function(){
    const apiorderUrl = get_url_home() + "/api/order/";
    const coupon = JSON.parse(localStorage.getItem('coupon'));
    const cart = JSON.parse(localStorage.getItem('cart'));
    const formData = new FormData();

    formData.append('discount', (coupon) ? coupon['discount'] :0); 
    formData.append('list-order', JSON.stringify(cart)); 

    fetch(apiorderUrl, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token_access}`
        },
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        localStorage.removeItem("cart");
        localStorage.removeItem("coupon");
        window.location.replace(get_url_home()+"/shopping/complete-order/");
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

})