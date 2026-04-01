chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "SCAN_URL") {

    fetch("https://jarvis-c-phishing-detector.onrender.com/scan", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: request.url })
    })
    .then(res => res.json())
    .then(data => {
      sendResponse(data); // ✅ send data back
    })
    .catch(err => {
      console.error("ERROR:", err);
      sendResponse({ error: true });
    });

    return true; // required for async
  }
});