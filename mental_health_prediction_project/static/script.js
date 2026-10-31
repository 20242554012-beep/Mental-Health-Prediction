const form = document.getElementById("prediction-form");
const fields = ["stress", "sleep", "anxiety", "workload", "support"];

fields.forEach((name) => {
  const slider = document.getElementById(name);
  const output = document.getElementById(`${name}-value`);
  slider.addEventListener("input", () => output.textContent = slider.value);
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = document.getElementById("submit-btn");
  button.disabled = true;
  button.innerHTML = "Analyzing…";
  const payload = {};
  fields.forEach((name) => payload[name] = Number(document.getElementById(name).value));

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Prediction failed.");

    document.getElementById("empty-state").classList.add("hidden");
    document.getElementById("result-state").classList.remove("hidden");
    document.getElementById("result-title").textContent =
      result.prediction === 1 ? "Higher-risk pattern" : "Lower-risk pattern";
    document.getElementById("result-message").textContent = result.message;
    document.getElementById("probability-value").textContent = `${result.probability}%`;
    document.getElementById("probability-bar").style.width = `${result.probability}%`;
    document.getElementById("result-symbol").textContent = result.prediction === 1 ? "!" : "✓";
  } catch (error) {
    alert(error.message);
  } finally {
    button.disabled = false;
    button.innerHTML = 'Analyze indicators <span>→</span>';
  }
});
