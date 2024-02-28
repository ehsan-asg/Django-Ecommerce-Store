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
    }else{
        window.location.replace(get_url_home());
    }

}
function formatPrice(price) {
    return price.toLocaleString() + ' تومان';
}
window.addEventListener('DOMContentLoaded', displayCartProductItems);
