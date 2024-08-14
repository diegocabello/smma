// Content script
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'processProductData') {
    const { data } = request;
    data.forEach(action => {
      if (action.type === 'scrollable') {
        const scrollableElement = document.evaluate(action.path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (scrollableElement) {
          scrollElementToTop(scrollableElement);
          scrollableElement.click(); // Click the element after scrolling to it
        }
      }
      if (action.type === 'dropdown') {
        const dropdownElement = document.evaluate(action.path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (dropdownElement) {
          dropdownElement.click();
        }
      }
    });
  }
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
