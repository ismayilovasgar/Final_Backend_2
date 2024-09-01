//? nice-select
const select = document.querySelector(".nice-select");
const spanText = document.querySelector(".nice-select input.current");
const arrows = document.querySelectorAll(".nice-select .select_arrow i");
const list = document.querySelector(".nice-select ul.list");
const listItems = document.querySelectorAll(".nice-select ul.list li");

select.addEventListener("click", (e) => {
  list.classList.toggle("show");
  select.classList.toggle("focus");

  arrows.forEach((arrow) => {
    arrow.classList.toggle("changeDirection");
  });

  listItems.forEach((item) => {
    item.addEventListener("click", (e) => {
      spanText.value = item.textContent;
    });
  });
});
//! --------------------------------------------------------------------------------------------------------
//! --------------------------------------------------------------------------------------------------------

//? sorting-select
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
        item.querySelector("input.current").value = list_item.textContent;
      });
      //
    });
    //
  });
  //
});
//! --------------------------------------------------------------------------------------------------------
//! --------------------------------------------------------------------------------------------------------

//? Form
const catalogInput = document.getElementById("catalog_input");
const form = document.getElementById("catalog_search");

catalogInput.addEventListener("focus", function () {
  form.classList.add("active-border");
});

catalogInput.addEventListener("blur", function () {
  form.classList.remove("active-border");
});

//! Swiper Buttons
var swiper = new Swiper(".testimonials-swiper", {
  slidesPerView: "4",
  spaceBetween: 10,

  pagination: {
    el: ".swiper-pagination",
    type: "progressbar",
    clickable: true,
  },
  navigation: {
    // nextEl: ".myswiper-button-next",
    // prevEl: ".myswiper-button-prev",
  },

  breakpoints: {
    375: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    480: {
      slidesPerView: 2,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 0,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 0,
    },
  },
});
//! --------------------------------------------------------------------------------------------------------
//! --------------------------------------------------------------------------------------------------------

//? Fetch Data From Django url
const catalogList = document.querySelector(".catalogList");
const catalogSearch = document.querySelector(".catalogSearch");
const linkItems = [...document.querySelectorAll("ul li.cataloglink")];

// click button by trainer name
const button = document.querySelector(".catalogSearch button");
const inputText = document.querySelector(".catalogSearch input");

inputText.addEventListener("input", function (event) {
  let value = inputText.value;

  // Check for multiple consecutive spaces
  const hasConsecutiveSpaces = /\s{2,}/.test(value);
  // Check for any numbers
  const hasNumbers = /[0-9]/.test(value);

  if (hasConsecutiveSpaces || hasNumbers) {
    // Add error styling
    catalogSearch.classList.add("error-input");
  } else {
    // Remove error styling
    catalogSearch.classList.remove("error-input");
  }

  // Optionally, replace invalid input while preserving existing text
  // This will correct the text but not remove it
  value = value.replace(/\s{2,}/g, " ").replace(/[0-9]/g, "");
  inputText.value = value;
});

linkItems.map((item) => {
  item.addEventListener("click", (e) => {
    // remove all selected tag
    linkItems.forEach((el) => el.classList.remove("selected"));
    // add selected tag to special item
    item.classList.toggle("selected");

    // fetchPostByText(`"category_"${item.textContent}`, catalogList);
  });
});

button.addEventListener("click", (e) => {
  isValidString = inputText.value.trim();
  if (!!isValidString) {
    fetchPostByText("name_" + isValidString, catalogList);
  }
});

//? click button by category name
linkItems.forEach((item) => {
  item.addEventListener("click", (e) => {
    fetchPostByText("category_" + item.textContent, catalogList);
    // e.preventDefault();
  });
});

function markFirstItem() {
  // Select the first item in the list
  const firstItem = document.querySelector("ul li.cataloglink");

  // Apply a CSS class to mark the first item
  if (firstItem) firstItem.classList.add("selected");
}

const fetchPostByText = async (search_text, wrap) => {
  wrap.innerHTML = "";
  const response = await fetch(
    `http://127.0.0.1:8000/courses/programs/${search_text}/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(),
    }
  );
  const data = await response.json();

  fillCardToContainer(data.results, data.results.length, wrap);
  inputText.value = "";
};

const advancFilterBtn = document.querySelector(".customFilter");
advancFilterBtn.addEventListener("click", (e) => {
  // convert 4 input value to array
  const myarray = [...document.querySelectorAll(".catalogSorting input")].map(
    (el) => el.value
  );
  fetchPostByArray(myarray, catalogList);
});

async function fetchPostByArray(array, wrap) {
  const response = await fetch("http://127.0.0.1:8000/courses/programs/list/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({ data: array }),
  });
  const data = await response.json();

  fillCardToContainer(data.results, data.results.length, wrap);
}

//! --------------------------------------------------------------------------------------------------------
//! --------------------------------------------------------------------------------------------------------
const oldestBtn = document.querySelector("[data-value='Oldest']");
const newestBtn = document.querySelector("[data-value='Newest']");
let oldest_status = true;
let newest_status = false;
oldestBtn.addEventListener("click", (e) => {
  newest_status = true;
  if (oldest_status) reverseCard();
  oldest_status = false;
});

newestBtn.addEventListener("click", (e) => {
  oldest_status = true;
  if (newest_status) reverseCard();
  newest_status = false;
});

function reverseCard() {
  let cards = [...catalogList.querySelectorAll(".card")].reverse();
  catalogList.innerHTML = "";
  cards.map((item) => {
    catalogList.append(item);
  });
}

//! --------------------------------------------------------------------------------------------------------
//! --------------------------------------------------------------------------------------------------------

function fillCardToContainer(data, len, wrap = catalogList) {
  oldest_status = true;
  newest_status = false;
  if (len > 0) {
    wrap.innerHTML = "";
    data.map((item) => {
      wrap.innerHTML += `
    <a class="card" href="/programs/detail/${item.course_id}/">
    <div class="">
            <div class="cardPreview">
                <img class="backPreview" src="${item.course_image}" alt="">
                <div class="cardStatus ${item.course_category}">${item.course_category}</div>
            </div>
      
            <div class="cardHead">
                <div class="cardUser">
                    <div class="cardAvatar">
                        <img src="${item.trainer_image}" alt="">
                    </div>
                    <div class="cardDetails">
                        <div class="cardTitle">${item.course_description}</div>
                        <div class="cardTrainer">
                            <span class="firstName">${item.trainer_fullname} </span>
                        </div>
                    </div>
                </div>
                <div class="cardLevel ${item.course_level}">${item.course_level}</div>
            </div>
      
            <div class="cardParameters">
                <div class="cardParameter">
                   <i class="fa-brands fa-youtube"></i>
                   <span>7</span> 
                </div>
                <div class="cardParameter">
                   <i class="fa-regular fa-user"></i>
                  <span>160</span>
                </div>
            </div>
      </div>
      </a>
    `;
    });
  } else {
    wrap.innerHTML = "";
    notFounded();
  }
}

function notFounded() {
  catalogList.innerHTML = `<div class="notFounded">not founded available content .....</div>`;
  setTimeout(() => {
    // catalogList.innerHTML = "";
  }, 750);
}

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
