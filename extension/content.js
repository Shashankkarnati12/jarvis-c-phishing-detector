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

      showResult(response);
    }
  );

  function showResult(data) {

    // 🚨 Only block dangerous sites
    if (data.risk_score < 50) return;

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
          (passwords, messages, credit card details).
        </p>

        <div style="margin-top:20px; font-size:18px;">
          <p><b>Risk Score:</b> ${data.risk_score}</p>
          <p><b>ML Probability:</b> ${data.probability}%</p>
          <p><b>SSL Status:</b> ${data.ssl}</p>
          <p><b>Domain Age:</b> ${data.domain_age} days</p>
        </div>

        <button onclick="window.history.back()" style="
          margin-top:30px;
          padding:10px 20px;
          font-size:16px;
          border:none;
          background:black;
          color:white;
          cursor:pointer;
        ">
          Go Back to Safety
        </button>

      </div>
    `;
  }

})();