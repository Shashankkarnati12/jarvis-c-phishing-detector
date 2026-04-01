(function () {

  const currentURL = window.location.href;

  chrome.runtime.sendMessage(
    {
      type: "SCAN_URL",
      url: currentURL
    },
    (response) => {
      if (!response || response.error) {
        console.log("Scan failed");
        return;
      }

      console.log("Scan result:", response);

      // OPTIONAL: show popup badge on screen
      showResult(response);
    }
  );

  function showResult(data) {
    const box = document.createElement("div");

    box.innerText = `
SAFE: ${data.final_result}
Risk: ${data.risk_score}
SSL: ${data.ssl}
Age: ${data.domain_age}
    `;

    box.style.position = "fixed";
    box.style.bottom = "20px";
    box.style.right = "20px";
    box.style.background = "green";
    box.style.color = "white";
    box.style.padding = "10px";
    box.style.zIndex = "999999";

    document.body.appendChild(box);
  }

})();