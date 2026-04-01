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

      // 🔴 PHISHING → FULL BLOCK PAGE
      if (response.risk_score >= 50) {
        showRedPage(response);
      } 
      // 🟢 SAFE → SMALL POPUP
      else {
        showGreenPopup(response);
      }

    }
  );

  // 🔴 RED FULL PAGE
  function showRedPage(data) {
    document.body.innerHTML = `
      <div style="
        height:100vh;
        width:100%;
        background:#d32f2f;
        color:white;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        font-family:Arial;
        text-align:center;
      ">
        <h1>⚠ Deceptive Site Ahead</h1>
        <h2 style="color:#ffcccb;">JARVIS-C Security Shield</h2>

        <p style="max-width:600px;">
          Attackers on this website may try to steal your information
        </p>

        <div style="margin-top:20px;">
          <p><b>Risk Score:</b> ${data.risk_score}</p>
          <p><b>SSL:</b> ${data.ssl}</p>
          <p><b>Domain Age:</b> ${data.domain_age}</p>
        </div>

        <button onclick="window.history.back()" style="
          margin-top:30px;
          padding:10px 20px;
          background:black;
          color:white;
          border:none;
          cursor:pointer;
        ">
          Go Back to Safety
        </button>
      </div>
    `;
  }

  // 🟢 GREEN POPUP
  function showGreenPopup(data) {

    const box = document.createElement("div");

    box.innerHTML = `
      <b>🛡 SAFE WEBSITE</b><br>
      Risk: ${data.risk_score}<br>
      SSL: ${data.ssl}<br>
      Age: ${data.domain_age}
    `;

    box.style.position = "fixed";
    box.style.bottom = "20px";
    box.style.right = "20px";
    box.style.background = "#2e7d32";
    box.style.color = "white";
    box.style.padding = "12px";
    box.style.borderRadius = "8px";
    box.style.zIndex = "999999";
    box.style.fontSize = "14px";
    box.style.boxShadow = "0 0 10px rgba(0,0,0,0.3)";

    document.body.appendChild(box);

    // auto hide after 5 sec
    setTimeout(() => {
      box.remove();
    }, 5000);
  }

})();