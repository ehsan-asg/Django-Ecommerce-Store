function displayCartProductItems() {

    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const cartTableBody = document.querySelector('.table-cart tbody');
    const checkout_summary_price = document.querySelector('.checkout-summary-price-value-amount')
    let totalAmount = 0;
    let sum_item = 0;
    cartItems.forEach(cartItems_length=>{
        sum_item += cartItems_length.quantity
        totalAmount +=  cartItems_length.price
      })

    if (sum_item > 0) {
        document.querySelector(".checkout-summary-summary li span").textContent = `مبلغ کل (${sum_item} کالا)`
        document.querySelector(".price-all").textContent = formatPrice(totalAmount)
        document.querySelector(".checkout-summary-price-value-amount").textContent = formatPrice(totalAmount)
        document.querySelector(".fs-sm").textContent = `(${sum_item} کالا)`
    }else{
        window.location.replace(get_url_home());
    }
    cartItems.forEach(cartItems=>{
        document.querySelector(".card-body .box .row").innerHTML += `<div class="col-lg-3 col-md-4 col-sm-6 col-12">
        <div class="product-box-container">
            <div class="product-box product-box-compact">
                <a class="product-box-img">
                    <img src="${cartItems.image}">
                </a>
                <div class="product-box-title">
                   ${cartItems.name}
                </div>
            </div>
        </div>
    </div>`
    })

}
function formatPrice(price) {
    return price.toLocaleString() + ' تومان';
}
function Summaryofproducts(productitem){

}
window.addEventListener('DOMContentLoaded', displayCartProductItems);
