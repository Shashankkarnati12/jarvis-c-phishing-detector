(function () {

  const currentURL = window.location.href;

  chrome.runtime.sendMessage(
    {
      type: "SCAN_URL",
      url: currentURL
    },
    (response) => {

      if (!response || response.error) return;

      if (response.risk_score >= 50) {
        showPremiumRed(response);
      } else {
        showPremiumGreen(response);
      }

    }
  );

  // 🔴 PREMIUM RED PAGE
  function showPremiumRed(data) {
    document.body.innerHTML = `
      <div style="
        height:100vh;
        width:100%;
        background: linear-gradient(135deg, #b71c1c, #d32f2f);
        color:white;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        font-family:Segoe UI, sans-serif;
        text-align:center;
        animation: fadeIn 0.5s ease-in;
      ">

        <h1 style="font-size:40px;">⚠ Deceptive Site Ahead</h1>

        <h2 style="opacity:0.8;">JARVIS-C Security Shield</h2>

        <p style="max-width:600px; margin-top:10px;">
          This website is flagged as dangerous. Attackers may try to steal your data.
        </p>

        <div style="
          margin-top:25px;
          background: rgba(255,255,255,0.1);
          padding:20px;
          border-radius:12px;
          backdrop-filter: blur(10px);
        ">
          <p>🔥 Risk Score: <b>${data.risk_score}</b></p>
          <p>🧠 AI Confidence: <b>${data.probability}%</b></p>
          <p>🔒 SSL: <b>${data.ssl}</b></p>
          <p>🌐 Domain Age: <b>${data.domain_age} days</b></p>
        </div>

        <button onclick="window.history.back()" style="
          margin-top:30px;
          padding:12px 25px;
          font-size:16px;
          border:none;
          border-radius:8px;
          background:black;
          color:white;
          cursor:pointer;
          transition:0.3s;
        "
        onmouseover="this.style.background='#333'"
        onmouseout="this.style.background='black'">
          Go Back to Safety
        </button>

        <style>
          @keyframes fadeIn {
            from { opacity:0; transform: scale(0.95); }
            to { opacity:1; transform: scale(1); }
          }
        </style>

      </div>
    `;
  }

  // 🟢 PREMIUM GREEN POPUP
  function showPremiumGreen(data) {

    const box = document.createElement("div");

    box.innerHTML = `
      <div style="
        backdrop-filter: blur(12px);
        background: rgba(46,125,50,0.9);
        color:white;
        padding:15px;
        border-radius:12px;
        font-family:Segoe UI;
        box-shadow:0 5px 20px rgba(0,0,0,0.3);
        animation: slideUp 0.5s ease;
      ">
        <b>🛡 SAFE WEBSITE</b><br><br>
        Risk: ${data.risk_score}<br>
        SSL: ${data.ssl}<br>
        Age: ${data.domain_age}
      </div>

      <style>
        @keyframes slideUp {
          from { transform: translateY(50px); opacity:0; }
          to { transform: translateY(0); opacity:1; }
        }
      </style>
    `;

    box.style.position = "fixed";
    box.style.bottom = "20px";
    box.style.right = "20px";
    box.style.zIndex = "999999";

    document.body.appendChild(box);

    setTimeout(() => {
      box.remove();
    }, 5000);
  }

})();