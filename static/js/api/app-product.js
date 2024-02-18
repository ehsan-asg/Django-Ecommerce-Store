const title = document.querySelector(".product-title h1")
const produc_gallery = document.querySelector('.product-gallery')
const options_color = document.querySelector(".product-variants")
const title_descriptions = document.querySelector(".product-title h1.text-title")
const descriptions = document.querySelector(".description-product .container p")
console.log(descriptions)

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
                let html = `                                        
            <li class="ui-variant">
                <label class="ui-variant ui-variant--color">
                    <span class="ui-variant-shape" style="background-color: ${data['feature'][x]["value"]}"></span>
                    <input type="radio" value="1" name="color" class="variant-selector"
                        checked>
                    <span class="ui-variant--check">${data['feature'][x]["name"]}</span>
                </label>
            </li>`
             
            options_color.innerHTML+=html
            }
            title_descriptions.innerText = data['name']
            descriptions.innerText = data['description']
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
  }
fetchProductData(getCategorySlugFromURL())