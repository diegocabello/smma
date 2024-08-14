document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('actionButton').addEventListener('click', async function () {
    const productName = document.getElementById('productName').value;
    const productDescription = document.getElementById('productDescription').value;

    if (productName && productDescription) {
      console.log('Product Name:', productName);
      console.log('Product Description:', productDescription);

      try {
        const response = await fetch('https://u13fk4lvuk.execute-api.us-east-1.amazonaws.com/default/testpythonopenaithingy', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ product: productName, 'product description': productDescription })
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error('Network response was not ok: ' + response.statusText + ' - ' + errorText);
        }

        const data = await response.json();
        console.log('Received data:', data);

        chrome.storage.local.set({ productData: data }, function () {
          chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { action: 'processProductData', data }, function(response) {
              if (chrome.runtime.lastError) {
                console.error("Error sending message:", chrome.runtime.lastError.message);
              }
            });
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
