// Desktop
// const dropdown = document.querySelector("li.drop");
// const dropdownArrow = document.querySelector("li.drop > i");

// dropdown.addEventListener("mouseover", (e) => {
//   dropdownArrow.classList.toggle("rotate_180");
// });

// Bars Menu
const btnHidden = document.querySelector("i.fa-solid.fa-bars");
const headerTrialBtn = document.querySelector(".headerTrialBtn");
const tabletMenu = document.getElementById("tabletMenu");
const dropdownMenu = document.querySelector(".dropdownBody");
const dropdownBtn = document.querySelector(".dropdownLink");
const popup = document.getElementById("hiddenTabletMenu");
const headerNavbar = document.getElementById("headerNavbar");
const class_arrow = document.querySelector(".dropdownLink i");

btnHidden.addEventListener("click", (e) => {
  btnHidden.classList.toggle("fa-xmark");
  // alert(tabletMenu);
  tabletMenu.classList.toggle("show");
  // headerTrialBtn.classList.toggle("hidden");
});

dropdownBtn.addEventListener("click", (e) => {
  dropdownMenu.classList.toggle("active");
});

class_arrow.addEventListener("click", (e) => {
  console.log("+++");
  class_arrow.classList.toggle("rotate_180");
});

function clickOutside(e) {
  if (
    !e.composedPath().includes(headerNavbar) &&
    tabletMenu.classList.contains("show")
  ) {
    tabletMenu.classList.toggle("show");
    btnHidden.classList.toggle("fa-xmark");
  }
}
// document.addEventListener("click", clickOutside);

// ? Footer
const footer_nav = document.querySelector(
  ".footer__col:nth-child(1) .footer__category"
);
const footer_nav__icon = document.querySelector(
  ".footer__col:nth-child(1) .footer__category i"
);
const footer_menu = document.querySelector(".footer__menu ul");

footer_nav.addEventListener("click", (e) => {
  footer_menu.classList.toggle("active");
  footer_nav__icon.classList.toggle("rotate");
});

// Chnage Theme
const toggle_button = document.getElementById("dark-change");
const light_images = document.querySelectorAll(".some-icon-light");
const dark_images = document.querySelectorAll(".some-icon-dark");

toggle_button.addEventListener("click", function () {
  document.body.classList.add("dark");
  toggle_button.classList.toggle("active");
});

function hidden_all_item(items) {
  items.forEach((element) => {
    element.style.display = "none";
  });
}

function show_all_item(items) {
  items.forEach((element) => {
    element.style.display = "block";
  });
}

// Dark / light mode
const currentTheme = localStorage.getItem("theme");

if (currentTheme === "dark") {
  setDarkMode();
}

toggle_button.addEventListener("click", function () {
  setTheme();
});

function setTheme() {
  let currentTheme = document.body.getAttribute("theme");

  if (currentTheme === "dark") {
    setLightMode();
  } else {
    setDarkMode();
  }
}

function setDarkMode() {
  document.body.setAttribute("theme", "dark");
  toggle_button.classList.add("active");

  localStorage.setItem("theme", "dark");
  hidden_all_item(light_images);
  show_all_item(dark_images);
}

function setLightMode() {
  document.body.removeAttribute("theme");
  toggle_button.classList.remove("active");
  localStorage.setItem("theme", "light");
  hidden_all_item(dark_images);
  show_all_item(light_images);
}

//? Send Message Form Code
// Handle form submission via Fetch API
const baseMailForms = document.querySelectorAll(".footer_subs_form");
baseMailForms.forEach((element) => {
  element.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    const csrfToken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value; // CSRF token

    // Send form data using Fetch API
    fetch("http://127.0.0.1:8000/sendmail/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken, // Include CSRF token in the request header
        Accept: "application/json",
      },
      body: formData, // Send the form data
    })
      .then((response) => response.json())
      .then((data) => {
        const messageDiv = document.querySelector(
          `#${element.id} ~ .result_email_msg`
        );
        messageDiv.classList.add("active");
        if (data.status === "success") {
          messageDiv.innerHTML = `<p style="color:green;">${data.message}</p>`;
          element.reset(); // Reset the form on success
        } else {
          messageDiv.innerHTML = `<p style="color:red;">${data.message}</p>`;
        }

        setTimeout(() => {
          messageDiv.classList.remove("active");
        }, 1500);
      })
      .catch((error) => {
        const messageDiv = document.querySelector(
          `#${element.id} ~ .result_email_msg`
        );

        messageDiv.innerHTML = "";
        messageDiv.classList.add("active");
        messageDiv.innerHTML = `<p style="color:red;">There was an error. Please try again.</p>`;
        setTimeout(() => {
          messageDiv.classList.remove("active");
        }, 1500);
      });
  });
});

// swiper cards in navbar
var swiper = new Swiper(".swiper_content_navbar", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
