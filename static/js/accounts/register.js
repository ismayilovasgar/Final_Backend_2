const alert_text = document.querySelector(".custom_alert");
const submit_btn = document.querySelector(".actions button");

submit_btn.addEventListener("click", (e) => {
  localStorage.setItem("regIsDisbaled", "true");
});

document.addEventListener("DOMContentLoaded", (e) => {
  // Retrieve the string value from localStorage
  let storedValue = localStorage.getItem("regIsDisbaled");

  // Convert the string "false" to the boolean false
  let booleanValue = storedValue === "true" ? true : false;

  if (booleanValue) alert_text.classList.add("show_alert");
  localStorage.setItem("regIsDisbaled", "false");

  setTimeout(() => {
    alert_text.classList.remove("show_alert");
  }, 1550);
});
