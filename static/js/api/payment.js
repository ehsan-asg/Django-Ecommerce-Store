const couponButton = document.getElementById("button-coupon");
couponButton.addEventListener("click", function() {
    const couponCode = document.getElementById("code-coupon").value;
    const apiUrl = get_url_home() + "/api/coupon/check/" + couponCode + "/";
    console.log(apiUrl)

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
