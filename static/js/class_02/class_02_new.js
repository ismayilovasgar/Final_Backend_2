// ! Swiper - 1

let swiper_programs2 = new Swiper(".programs_swiper", {
  grabCursor: true,
  slidesPerView: 3,
  spaceBetween: 24,
  pagination: {
    el: ".swiper-pagination",
    type: "fraction",
    clickable: true,
  },
  navigation: {
    nextEl: ".programs_next_btn",
    prevEl: ".programs_prev_btn",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },

    700: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
//? Filter Select
//* sorting-select
const select_sorting = document.querySelectorAll(".sorting");
let sorting_list_items = "";
select_sorting.forEach((item) => {
  item.addEventListener("click", (e) => {
    item.querySelector("i").classList.toggle("changeDirection");
    item.classList.toggle("focus");
    item.querySelector(".select_arrow").classList.toggle("focus");
    item.querySelector("ul.list").classList.toggle("show");
    sorting_list_items = item.querySelectorAll("ul li");
    sorting_list_items.forEach((list_item) => {
      list_item.addEventListener("click", (e) => {
        item.querySelector("input.current").value = list_item.innerText;
      });
    });
    e.preventDefault();
  });
});

// ------------------------------------------------------------------------------------------------------
//? For recieve data with fetch request
const listWrap = document.querySelector(".listWrap");
const allListItem = [...document.querySelectorAll("ul.list li")];

document.addEventListener("DOMContentLoaded", async (e) => {
  const filterValue = "Yoga";

  // Check if there's data in localStorage for this filter
  let storedData = localStorage.getItem("trainers_detail");

  if (storedData) {
    let parsedData = JSON.parse(storedData);
    // Update the DOM with the stored data
    fillDemo(parsedData);
    markSelectCat(localStorage.getItem("trainers_detail_cat"));
  } else {
    const data = await fetchFilteredData(filterValue);
    localStorage.setItem("trainers_detail", JSON.stringify(data));
    localStorage.setItem("trainers_detail_cat", filterValue);
    markSelectCat(localStorage.getItem("trainers_detail_cat"));

    fillDemo(data);
  }
});

allListItem.map((item) => {
  item.addEventListener("click", async (e) => {
    // remove all selected tag
    allListItem.forEach((el) => el.classList.remove("selected"));

    // add selected tag to special item
    item.classList.toggle("selected");

    // Fetch data and stored in localstorage
    const data = await fetchFilteredData(`${item.innerText}`);
    localStorage.setItem("trainers_detail", JSON.stringify(data));
    localStorage.setItem("trainers_detail_cat", JSON.stringify(item.innerText));
    fillDemo(data);

    //
  });
});

async function fetchFilteredData(text) {
  const response = await fetch(
    `http://127.0.0.1:8000/class_02/category/${text}/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(""),
    }
  );
  const data = await response.json();
  return data;
}

// mark category that click above
function markSelectCat(text) {
  const item = document.querySelector(`ul.list li[data-value=${text}]`);
  item.classList.add("selected");
}

// JavaScript function to truncate strings
function truncateString(str, num) {
  if (str.length <= num) {
    return str;
  }
  return str.slice(0, num) + "...";
}

async function fillDemo(data) {
  listWrap.innerHTML = "";
  data.map((item) => {
    listWrap.innerHTML += `
    <div class="trainerItem">
            <div class="profile">
              <img src="${item.trainer_image}" alt="">
            </div>
            <div class="trainerName">${item.fullname}</div>
            <div class="trainerPosition"> ${item.profession} </div>
    </div>

    <div class="modal" id="">
                    <div class="modalContent">
                        <div class="popupContainer">

                            <div class="trainerTop">
                                <div class="trainerAvatar">
                                    <img src="${item.trainer_image}" alt="">
                                </div>
                                <div class="trainerName">${item.fullname}</div>
                                <div class="trainerPosition">${
                                  item.profession
                                }</div>
                                <div class="trainerSocials">
                                    <a href="${
                                      item.facebook
                                    }" target="_blank" class="trainer_social">
                                        <i class="fa-brands fa-facebook"></i>
                                    </a>
                                    <a href="${
                                      item.instagram
                                    }" target="_blank" class="trainer_social">
                                        <i class="fa-brands fa-instagram"></i>
                                    </a>
                                    <a href="${
                                      item.twitter
                                    }" target="_blank" class="trainer_social">
                                        <i class="fa-brands fa-twitter"></i>
                                    </a>
                                    <a href="${
                                      item.linkedin
                                    }" target="_blank" class="trainer_social">
                                        <i class="fa-brands fa-linkedin"></i>
                                    </a>
                                </div>
                            </div>
                            <form action="" method="/" class="subscriptionInput">
                                <input class="subscription__input" type="email" placeholder="Find a class"
                                    required="required">
                                <button class="subscriptionBtn">
                                    <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </form>

                            <div class="swiper">
                            <div class="trainerModalWrap programs_swiper2">
                                <div class="swiper-wrapper">
                                      ${item.courses
                                        .map(
                                          (el) => `
                                            <div class="swiper-slide">

                                                  <div class="trainerPreview">
                                                      <img src="${
                                                        el.image
                                                      }" alt="">
                                                      <p>${el.category}</p>
                                                  </div>

                                                  <div class="modalTrainerHead">
                                                      <div class="trainer__title">${truncateString(
                                                        el.description,
                                                        20
                                                      )}</div>
                                                      <div class="trainerLevel">${
                                                        el.level
                                                      }</div>
                                                  </div>

                                                  <div class="trainerParameters">
                                                      <div class="trainerParameter">
                                                        <i class="fa-brands fa-youtube"></i>
                                                        <span>7</span>  
                                                      </div>
                                                      <div class="trainerParameter">
                                                        <i class="fa-regular fa-user"></i> 
                                                        <span>160</span> 
                                                      </div>
                                                 </div>
                                            </div>
                                      `
                                        )
                                        .join("")}
                                </div>
                              </div>
                            </div>

                            <div class="bottomBtns">
                                <div class="arrowBtns">
                                    <i class="fa-solid fa-left-long left_arrow"></i>
                                   <i class="fa-solid fa-right-long right_arrow"></i>
                                </div>
                                <button class="btn btn_orange">Browse all class</button>
                            </div>

                            <button title="Close (Esc)" type="button" class="modalCloseBtn">
                               <i class="fa-solid fa-xmark"></i>
                            </button>

                        </div>
                    </div>
            </div>
     
    `;
    let swiper_programs = new Swiper(".programs_swiper2", {
      grabCursor: true,
      slidesPerView: 2,
      spaceBetween: 16,
      pagination: {
        el: ".swiper-pagination",
        type: "fraction",
        clickable: true,
      },
      navigation: {
        nextEl: ".arrowBtns .right_arrow",
        prevEl: ".arrowBtns .left_arrow",
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
        },

        768: {
          slidesPerView: 1,
        },
        1024: {
          slidesPerView: 2,
        },
      },
    });
  });

  const trainers = [...document.querySelectorAll(".listWrap .trainerItem")];
  const closeBtns = [...document.querySelectorAll(".modal .modalCloseBtn")];

  trainers.forEach((trainer) => {
    trainer.addEventListener("click", (e) => {
      console.log(trainer);
      // trainer.nextElementSibling.style.display = "block";
      trainer.nextElementSibling.classList.add("showed");
      e.preventDefault();
    });
  });

  closeBtns.forEach((closeBtn) => {
    closeBtn.addEventListener("click", (e) => {
      // closeBtn.closest(".modal").style.display = "none";
      closeBtn.closest(".modal").classList.remove("showed");
    });
  });

  //
  window.onclick = function (event) {
    const modal = document.querySelector(".modal.showed");

    if (event.target == modal) {
      modal.classList.remove("showed");
    }
  };
}

// Function to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
