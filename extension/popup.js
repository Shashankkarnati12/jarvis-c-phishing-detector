document.getElementById("scanBtn").addEventListener("click", async () => {

    const [tab] = await chrome.tabs.query({active: true, currentWindow: true});

    const url = tab.url;

    const response = await fetch("https://jarvisc-phishing-backend.onrender.com/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    });

    const data = await response.json();

    let resultText = `
Website Status: ${data.final_result}

Risk Score: ${data.risk_score}
ML Probability: ${data.probability}%

Security Checks:
✔ SSL Certificate: ${data.ssl_status}
⚠ VirusTotal Malicious: ${data.vt_malicious}
⚠ Domain Age: ${data.domain_age_days} days
`;

    document.getElementById("result").innerText = resultText;

});