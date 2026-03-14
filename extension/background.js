chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

    if (changeInfo.status === "complete" && tab.url) {

        fetch("https://jarvisc-phishing-backend.onrender.com/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: tab.url })
        })
        .then(response => response.json())
        .then(data => {

            console.log("Auto Scan Result:", data);

            if (data.final_result === "PHISHING WEBSITE") {

                chrome.tabs.sendMessage(tabId, {
                    action: "phishingWarning",
                    result: data
                });

            }

        })
        .catch(err => console.log("Auto Scan Error:", err));

    }

});