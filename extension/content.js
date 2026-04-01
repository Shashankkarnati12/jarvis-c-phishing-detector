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

  // 🔊 VOICE ALERT (ADD HERE)
  const msg = new SpeechSynthesisUtterance(
    "Warning! This website is dangerous. Please go back immediately."
  );
  speechSynthesis.speak(msg);

  // 🔴 RED PAGE UI
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
    ">

      <h1 style="font-size:40px;">⚠ Deceptive Site Ahead</h1>
      <h2>JARVIS-C Security Shield</h2>

      <p>This website is flagged as dangerous.</p>

      <div style="
        margin-top:20px;
        padding:20px;
        background:rgba(255,255,255,0.1);
        border-radius:10px;
      ">
        <p>⚠ Risk Score: <b>${data.risk_score}</b></p>
<p>🤖 ML Probability: <b>${data.probability}%</b></p>
<p>🔐 SSL Status: <b>${data.ssl}</b></p>
<p>🌐 Domain Age: <b>${data.domain_age} days</b></p>
      </div>

      <button onclick="window.location.href='https://google.com'"
        style="
          margin-top:20px;
          padding:10px 20px;
          background:black;
          color:white;
          border:none;
          border-radius:5px;
          cursor:pointer;
        ">
        Go Back to Safety
      </button>

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