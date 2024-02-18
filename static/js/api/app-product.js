const title = document.querySelector(".product-title h1")

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
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
  }
fetchProductData(getCategorySlugFromURL())