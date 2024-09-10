const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".context");
const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");

const loginButton = document.getElementById("login_button");
const loginErrorText = document.querySelector(".account-text-login");
const loginError = document.querySelector(".alert-error");

sign_up_btn.addEventListener("click", (e) => {
  container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", (e) => {
  container.classList.remove("sign-up-mode");
});
// sign_up_btn2.addEventListener("click", (e) => {
//   container.classList.add("sign-up-mode2");
// });
// sign_in_btn2.addEventListener("click", (e) => {
//   container.classList.remove("sign-up-mode2");
// });

document.addEventListener("DOMContentLoaded", (e) => {
  loginButton.addEventListener("click", (e) => {
    loginErrorText.classList.add("expand");
    loginError.classList.add("expand");

    setTimeout(() => {
      loginErrorText.classList.remove("expand");
      loginError.classList.remove("expand");
    }, 1500);
  });
});
