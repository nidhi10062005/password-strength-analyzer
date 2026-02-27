function checkPassword() {
    const password = document.getElementById("password").value;

    fetch("/check_password", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        const score = data.score;
        const feedback = data.feedback;

        const fill = document.getElementById("strength-fill");
        const text = document.getElementById("strength-text");
        const feedbackList = document.getElementById("feedback");

        const percentage = (score / 5) * 100;
        fill.style.width = percentage + "%";

        if (score <= 2) {
            fill.style.background = "red";
            text.innerText = "Weak";
        } else if (score === 3 || score === 4) {
            fill.style.background = "orange";
            text.innerText = "Moderate";
        } else {
            fill.style.background = "green";
            text.innerText = "Strong";
        }

        feedbackList.innerHTML = "";
        feedback.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            feedbackList.appendChild(li);
        });
    });
}
