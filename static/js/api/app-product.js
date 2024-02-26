const title = document.querySelector(".product-title h1")
const produc_gallery = document.querySelector('.product-gallery')
const options_color = document.querySelector(".product-variants")
const title_descriptions = document.querySelector(".product-title h1.text-title")
const descriptions = document.querySelector(".description-product .container p")
const button_add_cart = document.querySelector(".btn-primary-cm ")

function getCategorySlugFromURL() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/');
    const categorySlug = parts[parts.length - 2]; 
    return categorySlug;
}


function fetchProductData(product_slug) {
    fetch(`http://127.0.0.1:8000/api/product/${product_slug}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
           title.innerText = data['name']
           produc_gallery.innerHTML +=` 
           <a class="d-flex justify-content-center " href="${data['image']}">
               <img src="${data['image']}" alt="Product">
           </a>`;
           for (let x in data['feature']) {
                if (x==0){
                    var check="active-label"
                    
                }else{
                    check = ""
                }                 
                let html = `                                        
            <li class="ui-variant">
                <label data-price="${data['feature'][x]["price"]}" data-feature="${data['feature'][x]['id']}" onclick="updatePrice(this)"  class="ui-variant ui-variant--color">
                    <span class="ui-variant-shape" style="background-color: ${data['feature'][x]["value"]}"></span>
                    <input type="radio" value="1" name="color" class="variant-selector"
                        checked>
                    <span class="ui-variant--check ${check}" >${data['feature'][x]["name"]}</span>
                </label>
            </li>`
             
            options_color.innerHTML+=html
            }
            document.getElementById('feature-price').textContent = data['feature'][0]['price'] + " تومان"
            title_descriptions.innerText = data['name']
            descriptions.innerText = data['description']
            document.getElementById("add-to-cart-single").innerHTML = `<button href="#" class="btn-primary-cm btn-with-icon" onclick="buttonaddcart(this)"  data-feature="${data['feature'][0]['id']}">
            <img src="img/theme/shopping-cart.png"  alt="">
            افزودن به سبد خرید
        </button>`
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
  }
function updatePrice(box) {
    const lis = document.querySelectorAll('.product-variants li');
    lis.forEach(li => {
        li.querySelector('.ui-variant--check').classList.remove('active-label');
    });

    const clickedLi = event.currentTarget;
    clickedLi.querySelector('.ui-variant--check').classList.add('active-label');
    const price = box.getAttribute('data-price');
    document.getElementById('feature-price').textContent = price + ' تومان';
    document.getElementById("add-to-cart-single")
    document.querySelector(".btn-primary-cm ").dataset.feature = box.getAttribute('data-feature')
}
fetchProductData(getCategorySlugFromURL())

if (document.querySelector('.count').textContent==="0"){
    document.querySelector('.count').style.display = "none"
}
function addToCart(product_slug, feature_id) {
    fetch(`http://127.0.0.1:8000/api/product/${product_slug}/`)
        .then(response => response.json())
        .then(data => {
            const featureById = {};
            feature_data = data.feature;
            data.feature.forEach(feature_data => {
                featureById[feature_data.id] = {
                    name: feature_data.name,
                    value: feature_data.value,
                    price: feature_data.price,
                    feature_id: feature_data.id
                };
            });

            const cartItem = {
                id: data.id,
                name: data.name,
                slug:data.slug,
                image: data.image,
                price: featureById[feature_id].price,
                feature_name: featureById[feature_id].name,
                feature_color: featureById[feature_id].value,
                feature_data: feature_id,
                quantity: 1,
                first_price:featureById[feature_id].price,
            };

            // Get existing cart items from localStorage
            const existingCartItems = JSON.parse(localStorage.getItem('cart')) || [];

            // Check if the item already exists in the cart
            const existingCartItemIndex = existingCartItems.findIndex(item => item.id === cartItem.id && item.feature_data === cartItem.feature_data);
            if (existingCartItemIndex !== -1) {
                // If the item already exists, increase its quantity
                existingCartItems[existingCartItemIndex].quantity += 1;
                existingCartItems[existingCartItemIndex].price = featureById[feature_id].price * existingCartItems[existingCartItemIndex].quantity;
            } else {
                // If the item does not exist, add it to the cart
                existingCartItems.push(cartItem);
            }

            // Save the updated cart items back to localStorage
            localStorage.setItem('cart', JSON.stringify(existingCartItems));

            // Refresh the cart display
            displayCartItems();
        })
        .catch(error => console.error('Error:', error));
}

function removeFromCart(index, feature_index) {
    // Get existing cart items from localStorage
    let existingCartItems = JSON.parse(localStorage.getItem('cart')) || [];

    // Find the index of the item with the corresponding id and feature_index
    const existingCartItemIndex = existingCartItems.findIndex(item => item.id === index && item.feature_data == feature_index);
    
    if (existingCartItemIndex !== -1) {
        // Decrease the quantity of the item by 1
        existingCartItems[existingCartItemIndex].quantity -= 1;
        existingCartItems[existingCartItemIndex].price= existingCartItems[existingCartItemIndex].quantity * existingCartItems[existingCartItemIndex].first_price
        
        // If the quantity becomes zero, remove the item from the cart
        if (existingCartItems[existingCartItemIndex].quantity <= 0) {
            existingCartItems.splice(existingCartItemIndex, 1);
        }
        
        // Save the updated cart items back to localStorage
        localStorage.setItem('cart', JSON.stringify(existingCartItems));
    }

    // Refresh the cart display
    displayCartItems();
}



function displayCartItems() {
    const cartItemsList = document.getElementById('cart-items-list');
    const cartTotalAmount = document.getElementById('cart-total-amount');
    let totalAmount = 0;

    // Clear the existing cart items
    cartItemsList.innerHTML = '';

    // Retrieve cart items from localStorage
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    sum_item = 0
    cartItems.forEach(cartItems_length=>{
        sum_item += cartItems_length.quantity
      })
    // Update the cart item count
    document.getElementById('cart-item-count').textContent = sum_item + ' کالا';


    if(sum_item > 0){
        document.querySelector('.header-cart-info').style.display = "block"
        document.querySelector('.count').textContent = sum_item
        document.querySelector('.count').style.display = "block"
        cartItems.forEach((item, index) => {
            const newCartItem = document.createElement('li');
            newCartItem.classList.add('cart-item');
            newCartItem.innerHTML = `
                <a href="#" class="header-basket-list-item">
                    <div class="header-basket-list-item-image">
                        <img src="${item.image}" alt="">
                    </div>
                    <div class="header-basket-list-item-content">
                        <p class="header-basket-list-item-title">${item.name}</p>
                        <div class="header-basket-list-item-footer">
                            <div class="header-basket-list-item-props">
                                <span class="header-basket-list-item-props-item">x ${item.quantity}</span>
                                <span class="header-basket-list-item-props-item">
                                    <div class="header-basket-list-item-color-badge" style="background:${item.feature_color}"></div>
                                </span>
                            </div>
                            <button class="header-basket-list-item-remove" data-index="${item.id}" data-feature="${item.feature_data}"  onclick="removeFromCart(${item.id},${item.feature_data})">
                                <i class="far fa-trash-alt"></i>
                            </button>
                        </div>
                    </div>
                </a>
            `;
        
            cartItemsList.appendChild(newCartItem);
            totalAmount += item.price;
        });
    }else{
        document.querySelector('.header-cart-info').style.display = "none"
        document.querySelector('.count').style.display = "none"
    }


    // Update the total amount
    cartTotalAmount.querySelector('.header-cart-info-total-amount-number').textContent = totalAmount.toLocaleString() + ' تومان';
}

// Call displayCartItems on page load
window.addEventListener('DOMContentLoaded', displayCartItems);


function buttonaddcart(box){
    addToCart(getCategorySlugFromURL(),box.dataset.feature)
}

