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

        // Process the received data and perform actions
        data.forEach(action => {
		  console.log(action)
          if (action.type == 'scrollable') {
			console.log("it's scrollable")
            const scrollableElement = document.evaluate(action.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (scrollableElement) {
              scrollElementToTop(scrollableElement);
              setTimeout(() => {
                scrollableElement.click(); // Click the element after scrolling to it
              }, 500); // Delay the click action by 500ms to allow scrolling to complete
            }
          }
          if (action.type == 'dropdown') {
			console.log("it's a dropdown")
            const dropdownElement = document.evaluate(action.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (dropdownElement) {
              dropdownElement.click();
            }
          }
        });
      } catch (error) {
        console.error('Error fetching product categories:', error);
      }
    } else {
      console.warn('Product Name and Description must be provided');
    }
  });
});

function scrollElementToTop(element) {
  const elementRect = element.getBoundingClientRect();
  const absoluteElementTop = elementRect.top + window.pageYOffset;
  const middle = absoluteElementTop - (window.innerHeight / 2);
  window.scrollTo({
    top: middle,
    behavior: 'smooth'
  });
}