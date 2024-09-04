// Get the modal

// ! Swiper - 1
let swiper_programs = new Swiper(".programs_swiper", {
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

window.onload = function () {
  // fetchFilteredData("yoga", listWrap);
  // markFirstItem();
};

function markFirstItem() {
  // Select the first item in the list
  const firstItem = document.querySelector("ul.list li");

  // Apply a CSS class to mark the first item
  if (firstItem) firstItem.classList.add("selected");
}

allListItem.map((item) => {
  item.addEventListener("click", (e) => {
    // remove all selected tag
    allListItem.forEach((el) => el.classList.remove("selected"));
    // add selected tag to special item
    item.classList.toggle("selected");
    // posts();
    // fetchFilteredData_2(`${item.getAttribute("data-value")}`, listWrap);
    fetchFilteredData(`${item.innerText}`, listWrap);
  });
});

async function fetchFilteredData(text, wrap) {
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
  console.log(data);
  fillDemo(data, wrap);
  //* data.map((item) => {
  //   console.log(item.fullname);
  //*   item.courses.map((course) => {
  //     console.log(course.description);
  //   });
  // });
}

async function fillDemo(data, wrap) {
  wrap.innerHTML = "";
  data.map((item) => {
    wrap.innerHTML += `
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

                            <div class="trainerModalWrap">
                                <div class="trainerSlider">
                                ${item.courses
                                  .map(
                                    (el) => `
                                        <div class="card">
                                            <div class="trainerPreview">
                                                <img src="${el.image}" alt="">
                                                <p>${el.category}</p>
                                            </div>
                                            <div class="modalTrainerHead">
                                                <div class="trainer__title">${el.description}</div>
                                                <div class="trainerLevel">${el.level}</div>
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

                            <div class="bottomBtns">
                                <div class="arrowBtns">
                                    <i class="fa-solid fa-left-long"></i>
                                   <i class="fa-solid fa-right-long"></i>
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
  });
  const trainers = [...document.querySelectorAll(".listWrap .trainerItem")];
  const closeBtns = [...document.querySelectorAll(".modal .modalCloseBtn")];

  trainers.forEach((trainer) => {
    trainer.addEventListener("click", (e) => {
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
