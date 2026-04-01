const currentUrl = window.location.href;

function autoScan() {

    fetch("https://jarvis-c-phishing-backend.onrender.com/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: currentUrl
        })
    })

    .then(response => response.json())

    .then(data => {

        console.log("Auto Scan Result:", data);

        if(data.final_result === "PHISHING WEBSITE"){

            showPhishingWarning(data);

        } else {

            showSafeNotification(data);

        }

    })

    .catch(error => {
        console.error("Scan Error:", error);
    });

}



function showPhishingWarning(data){

    const overlay = document.createElement("div");

    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100%";
    overlay.style.height = "100%";
    overlay.style.background = "#b71c1c";
    overlay.style.color = "white";
    overlay.style.zIndex = "999999";
    overlay.style.display = "flex";
    overlay.style.flexDirection = "column";
    overlay.style.justifyContent = "center";
    overlay.style.alignItems = "center";
    overlay.style.textAlign = "center";
    overlay.style.fontFamily = "Arial";

    overlay.innerHTML = `
        <h1 style="font-size:40px;">⚠ Deceptive Site Ahead</h1>

        <p style="font-size:18px; max-width:600px;">
        Attackers on this website may try to steal your information 
        (like passwords, messages, or credit card details).
        </p>

        <p style="margin-top:20px;">
        <b>Risk Score:</b> ${data.risk_score} <br>
        <b>ML Probability:</b> ${data.probability}% <br>
        <b>SSL Status:</b> ${data.ssl_status} <br>
        <b>Domain Age:</b> ${data.domain_age_days} days
        </p>

        <button id="leaveSite"
        style="
        margin-top:30px;
        padding:12px 20px;
        font-size:16px;
        border:none;
        background:black;
        color:white;
        cursor:pointer;
        ">
        Go Back to Safety
        </button>
    `;

    document.body.appendChild(overlay);

    document.getElementById("leaveSite").onclick = function(){
        window.history.back();
    };

}



function showSafeNotification(data){

    const safeBox = document.createElement("div");

    safeBox.innerHTML = `
    ✅ SAFE WEBSITE<br>
    Risk Score: ${data.risk_score}<br>
    SSL: ${data.ssl_status}<br>
    Domain Age: ${data.domain_age_days} days
    `;

    safeBox.style.position = "fixed";
    safeBox.style.bottom = "20px";
    safeBox.style.right = "20px";
    safeBox.style.background = "green";
    safeBox.style.color = "white";
    safeBox.style.padding = "12px";
    safeBox.style.borderRadius = "8px";
    safeBox.style.zIndex = "9999";
    safeBox.style.fontSize = "14px";
    safeBox.style.fontFamily = "Arial";

    document.body.appendChild(safeBox);

    setTimeout(() => {
        safeBox.remove();
    }, 5000);

}



// Run automatically when page loads
window.addEventListener("load", autoScan);