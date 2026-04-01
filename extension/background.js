(async () => {
    try {
        const response = await fetch("https://jarvis-c-phishing-detector.onrender.com/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: window.location.href
            })
        });

        const data = await response.json();

        console.log("API RESPONSE:", data);

        // ✅ FIXED KEYS
        document.querySelector("#result").innerText = data.final_result;
        document.querySelector("#risk").innerText = data.risk_score;
        document.querySelector("#ssl").innerText = data.ssl;
        document.querySelector("#domain").innerText = data.domain_age;

    } catch (error) {
        console.error("ERROR:", error);
    }
})();