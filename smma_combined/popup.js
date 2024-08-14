document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('actionButton').addEventListener('click', async function () {
    const productName = document.getElementById('productName').value;
    const productDescription = document.getElementById('productDescription').value;

    if (productName && productDescription) {
      console.log('Product Name:', productName);
      console.log('Product Description:', productDescription);

      try {
        const response = await fetch('http://localhost:3000/getProductCategories', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ productName, productDescription })
        });
        
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        
        const data = await response.json();
        console.log('Received data:', data);

        chrome.storage.local.set({ productData: data }, function () {
          chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { action: 'processProductData', data });
          });
        });
      } catch (error) {
        console.error('Error fetching product categories:', error);
      }
    } else {
      console.warn('Product Name and Description must be provided');
    }
  });
});
