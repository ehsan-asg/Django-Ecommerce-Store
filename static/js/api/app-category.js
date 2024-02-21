
function getCategorySlugFromURL() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/');
    const categorySlug = parts[parts.length - 2]; 
    return categorySlug;
}

function get_url_home(){
    main_url = window.location.protocol
    main_url += "//"+window.location.host
    return main_url
}

const categorySlug = getCategorySlugFromURL();
function fetchCategoryProducts(category_slug,page) {
    fetch(`http://127.0.0.1:8000/api/product-category/${category_slug}/?page=${page}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayCategoryProducts(data.results);
            createPaginationControls(data.count, page);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}
function displayCategoryProducts(data){
    let product_category = '';

    for (let x in data) {
        const html = `<div class="col-lg-3 col-md-4 col-sm-6 col-12 px-10 mb-1 px-res-0">
                                            <div class="product-card mb-2 mx-res-0">
                                                <a class="product-thumb" href="${get_url_home()+"/product"+"/"+data[x]['slug']}">
                                                    <img src="${data[x]['image']}" alt="Product Thumbnail">
                                                </a>
                                                <div class="product-card-body" style="
                                                display: flex;
                                                flex-direction: column;
                                            ">
                                                    <h5 class="product-title">
                                                        <a href="${get_url_home()+"/product"+"/"+data[x]['slug']}">${data[x]['name']}</a>
                                                    </h5>
                                                    <span class="product-price">${data[x]['feature'][0]['price']} تومان</span>
                                                </div>
                                            </div>
        </div>`;
        product_category += html;
    }
    const productsContainer = document.getElementById('product-category');
    productsContainer.innerHTML = product_category;
}
function createPaginationControls(totalItems, currentPage) {
    const totalPages = Math.ceil(totalItems / 3); 

    const paginationContainer = document.getElementById('pagination-container');
    paginationContainer.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.textContent = i;
        pageButton.classList.add('page-number');
        pageButton.dataset.page = i;
        if (i === currentPage) {
            pageButton.classList.add('active');
        }
        pageButton.addEventListener('click', function() {
            const page = parseInt(this.dataset.page);
            fetchCategoryProducts(categorySlug, page);
        });
        paginationContainer.appendChild(pageButton);
    }
}
fetchCategoryProducts(categorySlug,1)