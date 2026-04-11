function updateUI(strength, feedback) {
  const colors = ["bg-red-500", "bg-yellow-500", "bg-blue-500", "bg-green-500"];
  const texts = ["Weak", "Fair", "Good", "Strong"];

  if (strength === 0) {
    strengthBar.style.width = "0%";
    strengthBar.className = "h-3 rounded-full bg-gray-500";
    strengthText.textContent = "Enter a password";
    suggestions.innerHTML = "";
    return;
  }

  strengthBar.className = "h-3 rounded-full " + colors[strength - 1];
  strengthBar.style.width = (strength * 25) + "%";

  strengthText.textContent = texts[strength - 1];

  suggestions.innerHTML = feedback.map(item => `<li>• ${item}</li>`).join("");
}
