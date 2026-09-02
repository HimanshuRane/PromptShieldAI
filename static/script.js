async function analyzePrompt() {

    const prompt = document.getElementById("prompt").value;

    if (prompt.trim() === "") {
        alert("Please enter a prompt.");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").classList.add("hidden");

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                prompt: prompt
            })

        });

        const data = await response.json();

        document.getElementById("loading").style.display = "none";
        document.getElementById("result").classList.remove("hidden");

        // Risk Level
        document.getElementById("risk_level").innerText = data.risk_level;

        // Privacy Score
        document.getElementById("privacy_score").innerText =
            data.privacy_score + "/100";

        // Safe to Share
        document.getElementById("safe_to_share").innerText =
            data.safe_to_share;

        // Detected Items
        let detected = document.getElementById("detected_items");
        detected.innerHTML = "";

        data.detected_items.forEach(item => {

            let li = document.createElement("li");
            li.innerText = item;
            detected.appendChild(li);

        });

        // Privacy Risks
        let risks = document.getElementById("privacy_risks");
        risks.innerHTML = "";

        data.privacy_risks.forEach(item => {

            let li = document.createElement("li");
            li.innerText = item;
            risks.appendChild(li);

        });

        // Recommendations
        let recommendations = document.getElementById("recommendations");
        recommendations.innerHTML = "";

        data.recommendations.forEach(item => {

            let li = document.createElement("li");
            li.innerText = item;
            recommendations.appendChild(li);

        });

        // Sanitized Prompt
        document.getElementById("sanitized_prompt").value =
            data.sanitized_prompt;

    }
    catch (error) {

        document.getElementById("loading").style.display = "none";

        alert("Something went wrong.\n\n" + error);

        console.log(error);

    }

}