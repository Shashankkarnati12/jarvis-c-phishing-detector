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
        showGreenPopup(response);
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
 function showGreenPopup(data) {

  const popup = document.createElement("div");

  popup.style.position = "fixed";
  popup.style.bottom = "20px";
  popup.style.right = "20px";
  popup.style.width = "300px";
  popup.style.background = "linear-gradient(135deg, #22c55e, #16a34a)";
  popup.style.color = "white";
  popup.style.padding = "18px";
  popup.style.borderRadius = "12px";
  popup.style.zIndex = "999999";
  popup.style.boxShadow = "0 8px 25px rgba(0,0,0,0.3)";
  popup.style.fontFamily = "Segoe UI";

  popup.innerHTML = `
    <h3>✅ Safe Website</h3>
    <p style="opacity:0.9;">JARVIS-C Security Shield</p>

    <div style="
      margin-top:10px;
      background: rgba(255,255,255,0.15);
      padding:10px;
      border-radius:8px;
    ">
      <p>⚠ Risk: ${data.risk_score}</p>
      <p>📊 Confidence: ${data.probability}%</p>
      <p>🔒 SSL: ${data.ssl}</p>
      <p>🌐 Age: ${data.domain_age} days</p>
    </div>

    <button id="closePopup" style="
      margin-top:12px;
      width:100%;
      padding:8px;
      background:black;
      color:white;
      border:none;
      border-radius:6px;
      cursor:pointer;
    ">Close</button>
  `;

  document.body.appendChild(popup);

  document.getElementById("closePopup").onclick = () => popup.remove();

  // Auto close after 5 sec
  setTimeout(() => popup.remove(), 5000);
}

})();