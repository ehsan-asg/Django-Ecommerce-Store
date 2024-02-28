cart_count = document.querySelector(".count-cart")
function get_url_home(){
    main_url = window.location.protocol
    main_url += "//"+window.location.host
    return main_url
}

function getCategorySlugFromURL() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/');
    const categorySlug = parts[parts.length - 2]; 
    return categorySlug;
}
if (getCategorySlugFromURL() === "cart"){
    document.getElementById("cart-button-open").style.display = "none"
}
function displayCartProductItems() {

    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const cartTableBody = document.querySelector('.table-cart tbody');
    const checkout_summary_price = document.querySelector('.checkout-summary-price-value-amount')
    let totalAmount = 0;
    let sum_item = 0;
    cartItems.forEach(cartItems_length=>{
        sum_item += cartItems_length.quantity
        console.log(cartItems)
      })


    cartTableBody.innerHTML = '';

    if (sum_item > 0) {
        cart_count.textContent = sum_item
        document.getElementById("sidebar-bill").style.display = "block"

        cartItems.forEach((item, index) => {
            const row = document.createElement('tr');
            row.classList.add('checkout-item', 'border-bottom');

            row.innerHTML = `
                <td>
                    <img style="width:150px;"  src="${item.image}" alt="">
                    <button class="checkout-btn-remove" onclick="removeCartItem(${index})">×</button>
                </td>
                <td class="text-right">
                    <a href="${get_url_home()+'/product/'+item.slug}">
                        <h3 class="checkout-title">${item.name}</h3>
                    </a>
                    <div class="checkout-variant checkout-variant--color">
                        <span class="checkout-variant-title">رنگ :</span>
                        <span class="checkout-variant-value">
                            ${item.feature_name}
                            <div class="checkout-variant-shape" style="background-color:${item.feature_color}"></div>
                        </span>
                    </div>
                </td>
                <td>
                    <p class="mb-0">تعداد</p>
                    <div class="number-input">
                        <button onclick="decreaseQuantity(${index})"></button>
                        <input class="quantity" min="0" name="quantity" value="${item.quantity}" type="number">
                        <button onclick="increaseQuantity(${index})" class="plus"></button>
                    </div>
                </td>
                <td><strong>${formatPrice(item.price)}</strong></td>
            `;
            cartTableBody.appendChild(row);
            totalAmount += item.price;
            console.log(totalAmount)
            document.getElementById("price-bill-product").textContent = `مبلغ کل (${sum_item} کالا)‍`

            sum_item += item.quantity;
        });
    } else {
        cart_count.style.display = "none"
        document.getElementById("cart-content-full").classList.remove("col-xl-9")
        document.getElementById("cart-content-full").classList.add("col-xl-12")
        document.getElementById("cart-content").classList.remove("col-xl-9")
        document.getElementById("cart-content").classList.add("col-xl-12")
        document.getElementById("sidebar-bill").style.display = "none"
        cartTableBody.innerHTML = `
        <div class="cart-page cart-empty">
        <div class="circle-box-icon">
            <i class="mdi mdi-cart-remove"></i>
        </div>
        <p class="cart-empty-title">سبد خرید شما خالیست!</p> 
    </div>
        `;
        
    }

    document.getElementById("all-price-product").textContent = formatPrice(totalAmount)
    checkout_summary_price.textContent = formatPrice(totalAmount)

}


function decreaseQuantity(index) {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    if (cartItems[index].quantity > 0) {
        cartItems[index].quantity -= 1;
        localStorage.setItem('cart', JSON.stringify(cartItems));
        displayCartProductItems();
    }
}


function increaseQuantity(index) {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    cartItems[index].quantity += 1;
    localStorage.setItem('cart', JSON.stringify(cartItems));
    displayCartProductItems();
}


function removeCartItem(index) {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    cartItems.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cartItems));
    displayCartProductItems();
}


function formatPrice(price) {
    return price.toLocaleString() + ' تومان';
}


window.addEventListener('DOMContentLoaded', displayCartProductItems);



