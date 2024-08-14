// Popup script
window.addEventListener('DOMContentLoaded', function () {
  // Retrieve the stored input values from Chrome storage
  chrome.storage.local.get(['clickXPath', 'scrollXPath'], function (result) {
    document.getElementById('clickXPath').value = result.clickXPath || '';
    document.getElementById('scrollXPath').value = result.scrollXPath || '';
  });

  // Send message to content script when the popup is opened
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'popupOpened' });
  });

  document.getElementById('actionButton').addEventListener('click', function () {
    var clickXPath = document.getElementById('clickXPath').value;
    var scrollXPath = document.getElementById('scrollXPath').value;
    console.log('Click XPath:', clickXPath);
    console.log('Scroll XPath:', scrollXPath);

    // Store the input values in Chrome storage
    chrome.storage.local.set({ clickXPath: clickXPath, scrollXPath: scrollXPath }, function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'performAction', clickXPath: clickXPath, scrollXPath: scrollXPath });
      });
    });
  });
});

// Content script
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'popupOpened') {
    // Perform any necessary initialization or setup when the popup is opened
    console.log('Popup opened');
  } else if (request.action === 'performAction') {
    var clickXPath = request.clickXPath;
    var scrollXPath = request.scrollXPath;
    if (clickXPath && scrollXPath) {
      var clickElement = document.evaluate(clickXPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      var scrollElement = document.evaluate(scrollXPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      if (clickElement && scrollElement) {
        clickElement.click();
        scrollElementToTop(clickElement, scrollElement);
      }
    }
  }
});

function scrollElementToTop(clickedElement, scrollWindow) {
  if (scrollWindow && scrollWindow.scrollHeight > scrollWindow.clientHeight) {
    var elementTop = clickedElement.getBoundingClientRect().top - scrollWindow.getBoundingClientRect().top;
    var startPosition = scrollWindow.scrollTop;
    var distance = elementTop - startPosition;
    var startTime = null;
    var duration = 75; // Duration in milliseconds (0.075 seconds)

    function animateScroll(currentTime) {
      if (startTime === null) {
        startTime = currentTime;
      }
      var elapsedTime = currentTime - startTime;
      var scrollProgress = Math.min(elapsedTime / duration, 1);
      scrollWindow.scrollTop = startPosition + distance * scrollProgress;
      if (elapsedTime < duration) {
        window.requestAnimationFrame(animateScroll);
      }
    }

    window.requestAnimationFrame(animateScroll);
  }
}