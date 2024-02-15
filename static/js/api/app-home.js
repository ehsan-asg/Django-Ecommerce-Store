const carousel_laptop = document.getElementById('laptop-carousel')
const carousel_mobile = document.getElementById('mobile-carousel')
const carousel_mouse = document.getElementById('mouse-carousel')
async function fetchData() {
  try {
      const response = await fetch('http://127.0.0.1:8000/api/HomeProductView/');
      
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      
      const data = await response.json();
      
      const laptop = data['laptop_products'];
      const mobile = data['mobile_products'];
      const mouse = data['mouse_products'];
      
      for (let x in laptop) {
          const data_input = laptop[x];
          const html = `
              <div class="item">
                  <div class="product-card">
                      <a class="product-thumb" href="shop-single.html">
                          <img src="${data_input['image']}" alt="Product Thumbnail">
                      </a>
                      <div class="product-card-body">
                          <h5 class="product-title">
                              <a href="shop-single.html">${data_input['name']}</a>
                          </h5>
                          <span class="product-price">${data_input['feature'][0]['price']} تومان</span>
                      </div>
                  </div>
              </div>`;
          carousel_laptop.insertAdjacentHTML('beforeend', html);
      }
      for (let x in mobile) {
        const data_input = mobile[x];
        const html = `
            <div class="item">
                <div class="product-card">
                    <a class="product-thumb" href="shop-single.html">
                        <img src="${data_input['image']}" alt="Product Thumbnail">
                    </a>
                    <div class="product-card-body">
                        <h5 class="product-title">
                            <a href="shop-single.html">${data_input['name']}</a>
                        </h5>
                        <span class="product-price">${data_input['feature'][0]['price']} تومان</span>
                    </div>
                </div>
            </div>`;
            carousel_mobile.insertAdjacentHTML('beforeend', html);
      }
      for (let x in mouse) {
        const data_input = mouse[x];
        const html = `
            <div class="item">
                <div class="product-card">
                    <a class="product-thumb" href="shop-single.html">
                        <img src="${data_input['image']}" alt="Product Thumbnail">
                    </a>
                    <div class="product-card-body">
                        <h5 class="product-title">
                            <a href="shop-single.html">${data_input['name']}</a>
                        </h5>
                        <span class="product-price">${data_input['feature'][0]['price']} تومان</span>
                    </div>
                </div>
            </div>`;
            carousel_mouse.insertAdjacentHTML('beforeend', html);
      }
  } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
  }
}
  fetchData();
