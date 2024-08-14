// Content script
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'processProductData') {
    const { data } = request;
    data.forEach(action => {
      if (action.dropdown) {
        const dropdownElement = document.evaluate(action.dropdown, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (dropdownElement) {
          dropdownElement.click();
        }
      }
      if (action.selectable) {
        const selectableElement = document.evaluate(action.selectable, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (selectableElement) {
          scrollElementToTop(selectableElement, document.body);
          selectableElement.click();
        }
      }
    });
  }
});

function scrollElementToTop(clickedElement, scrollWindow) {
  if (scrollWindow && scrollWindow.scrollHeight > scrollWindow.clientHeight) {
    const elementTop = clickedElement.getBoundingClientRect().top - scrollWindow.getBoundingClientRect().top;
    const startPosition = scrollWindow.scrollTop;
    const distance = elementTop - startPosition;
    const duration = 75; // Duration in milliseconds

    function animateScroll(startTime) {
      const currentTime = performance.now();
      const elapsedTime = currentTime - startTime;
      const scrollProgress = Math.min(elapsedTime / duration, 1);
      scrollWindow.scrollTop = startPosition + distance * scrollProgress;
      if (elapsedTime < duration) {
        requestAnimationFrame(() => animateScroll(startTime));
      }
    }

    requestAnimationFrame(animateScroll);
  }
}
