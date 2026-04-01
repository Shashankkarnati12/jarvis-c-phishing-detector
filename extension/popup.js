document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("scanBtn").addEventListener("click", () => {

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {

      const url = tabs[0].url;

      chrome.runtime.sendMessage(
        {
          type: "SCAN_URL",
          url: url
        },
        (data) => {

          if (!data || data.error) {
            document.getElementById("result").innerText = "Error fetching data";
            return;
          }

          document.getElementById("result").innerText =
`Result: ${data.final_result}
Risk Score: ${data.risk_score}
SSL: ${data.ssl}
Domain Age: ${data.domain_age}`;

        }
      );

    });

  });

});