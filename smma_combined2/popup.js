const scrollPath = "/html/body/div[3]/div[13]/div/div[2]/div/div[3]/lazy-plugin/div/dynamic-component/campaign-audiences/material-expansionpanel/div/div[2]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div[1]/div[2]/div/div/subcategory-tree/div/div/div/subcategory-renderer/div[2]/div/tree-list/div[1]/tree-list[2]/div[1]/div";

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

        // Get the current active tab and inject the script
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          if (tabs[0] && tabs[0].id) {
            chrome.scripting.executeScript({
              target: { tabId: tabs[0].id },
              func: processActions,
              args: [data, scrollPath]
            }, () => {
              if (chrome.runtime.lastError) {
                console.error('Script injection failed: ', chrome.runtime.lastError.message);
              }
            });
          } else {
            console.error('No active tab found.');
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

function processActions(data, scrollPath) {
  console.log(data.keywords)
  data.commands.forEach(action => {
    if (action.type === 'scrollable') {
      const scrollElement = document.evaluate(scrollPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      const clickElement = document.evaluate(action.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      
      console.log('Processing scrollable action:', action);
      console.log('Scroll Element:', scrollElement);
      console.log('Click Element:', clickElement);
  
      if (clickElement && scrollElement) {
        clickElement.click();
        scrollElementToTop(clickElement, scrollElement);
        console.log('It is supposed to have done the click and scroll');
      } else {
        console.warn('Elements not found:', { clickElement, scrollElement });
      }
    } else if (action.type === 'dropdown') {
      const dropdownElement = document.evaluate(action.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      
      console.log('Processing dropdown action:', action);
      console.log('Dropdown Element:', dropdownElement);
  
      if (dropdownElement) {
        dropdownElement.click();
        console.log('It is supposed to have done the click');
      } else {
        console.warn('Dropdown element not found:', action.xpath);
      }
    }
  });
}

function scrollElementToTop(element, windowElement) {
  const elementRect = element.getBoundingClientRect();
  const windowRect = windowElement.getBoundingClientRect();
  const elementTop = elementRect.top - windowRect.top;
  const startPosition = windowElement.scrollTop;
  const distance = elementTop - startPosition;
  const duration = 75; // Duration in milliseconds (0.075 seconds)

  function animateScroll(currentTime) {
    if (!startTime) startTime = currentTime;
    const elapsedTime = currentTime - startTime;
    const scrollProgress = Math.min(elapsedTime / duration, 1);
    windowElement.scrollTop = startPosition + distance * scrollProgress;
    if (elapsedTime < duration) {
      window.requestAnimationFrame(animateScroll);
    }
  }

  let startTime = null;
  window.requestAnimationFrame(animateScroll);
}
