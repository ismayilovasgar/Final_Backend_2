var swiper = new Swiper(".clients_swiper", {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: ".swiper-pagination",
    clickable: "fraction",
  },
  pagination: {
    el: ".swiper-pagination",
    type: "fraction",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
      spaceBetween: 32,
    },
    480: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 32,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 32,
    },
  },
});

var swiper = new Swiper(".review-swiper-content", {
  pagination: {
    el: ".swiper-pagination",
    type: "progressbar",
  },
  navigation: {
    nextEl: ".previoustBtn",
    prevEl: ".nextBtn",
  },
});

// Filter Select
//* sorting-select
const select_sorting = document.querySelectorAll(".sorting");
let sorting_list_items = "";
select_sorting.forEach((item) => {
  item.addEventListener("click", (e) => {
    item.querySelector("i").classList.toggle("changeDirection");
    item.classList.toggle("focus");
    item.querySelector("ul.list").classList.toggle("show");
    sorting_list_items = item.querySelectorAll("ul li");
    sorting_list_items.forEach((list_item) => {
      list_item.addEventListener("click", (e) => {
        item.querySelector("input.current").value = list_item.innerText;
      });
    });
  });
});
//
//
//
// Home Trainer Category
// ------------------------------------------------------------------------------------------------------
const trainersContainer = document.querySelector(".trainersList  .listWrap");
const allListItem = [...document.querySelectorAll("ul.list li")];
let categorySlug = "yoga";
localStorage.setItem("category", categorySlug);
let localStorageKey = localStorage.getItem("category");

// Function to display trainer cards
function displayTrainers(trainers) {
  trainersContainer.innerHTML = "";

  trainers.map((trainer) => {
    trainersContainer.innerHTML += `
    <div class="trainerItem">
        <div class="profile">
          <img src="${trainer.image_url}" alt="">
        </div>
        <div class="trainerName">${trainer.name}</div>
        <div class="trainerPosition">
          ${trainer.profession}
        </div>
    </div>
    `;
  });
}

function searchCoursesByCategory(slug) {
  fetch(`http://127.0.0.1:8000/courses/categories/${slug}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify("text"),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data && data.length > 0) {
        // Override the previous data in localStorage with new search results
        localStorage.setItem("trainers", JSON.stringify(data));
        localStorage.setItem("lastCategory", slug); // Store the last used category slug

        // Add the new search results to the container
        displayTrainers(data);
      } else {
        console.warn("No data found for the selected category.");
      }
    })
    .catch((error) => console.error("Error fetching data:", error));
}

// Event listener for category input (e.g., dropdown or search box)
allListItem.map((item) => {
  item.addEventListener("click", (e) => {
    // remove all selected tag
    allListItem.forEach((el) => el.classList.remove("selected"));
    // add selected tag to special item
    item.classList.toggle("selected");

    const slug = item.getAttribute("data-value");

    if (slug) {
      // Perform search by category slug
      searchCoursesByCategory(slug);
    }
  });
});

// On page load, check if there is a last used category slug stored in localStorage
const lastCategorySlug = localStorage.getItem("lastCategory");
if (lastCategorySlug) {
  searchCoursesByCategory(lastCategorySlug);
}

// On page load, try to load the last search result from localStorage
const storedCards = localStorage.getItem("trainers");
if (storedCards) {
  // Display the stored cards on initial page load
  displayTrainers(JSON.parse(storedCards));
}
//
//
//
document.addEventListener("DOMContentLoaded", function () {
  const lastCategorySlug = localStorage.getItem("lastCategory");
  if (lastCategorySlug) {
    let lastSelectedItem = document.querySelector(
      `ul.list li[data-value=${lastCategorySlug}]`
    );
    lastSelectedItem.classList.add("selected");
    displayTrainers(JSON.parse(localStorage.getItem("trainers")));
    document.querySelector("input.current").value =
      lastSelectedItem.textContent.trim();

    // document.querySelector("input.current").value = lastSelectedItem.textContent;
  } else {
    const category = localStorage.getItem("category");
    const data = searchCoursesByCategory(category);
    let lastSelectedItem = document.querySelector(
      `ul.list li[data-value=${category}]`
    );
    lastSelectedItem.classList.add("selected");
    displayTrainers(data);

    document.querySelector("input.current").value =
      lastSelectedItem.textContent.trim();
  }
});

// ? swiper_content_steps
var swiper = new Swiper(".swiper_content_steps", {
  slidesPerView: 4,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
      spaceBetween: 20,
    },

    600: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
  },
});

// ? advantages list
var swiper = new Swiper(".swiper_content_advantageslist", {
  slidesPerView: 3,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
      spaceBetween: 20,
    },

    600: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
  },
});

//! My Old Solution  and lacking so use time is bad )))
// const listWrap = document.querySelector(".trainersList  .listWrap");
// const allListItem = [...document.querySelectorAll("ul.list li")];
// function markFirstItem() {
//   // Select the first item in the list
//   const firstItem = document.querySelector("ul.list li");

//   // Apply a CSS class to mark the first item
//   if (firstItem) firstItem.classList.add("selected");
// }

// allListItem.map((item) => {
//   item.addEventListener("click", (e) => {
//     // remove all selected tag
//     allListItem.forEach((el) => el.classList.remove("selected"));
//     // add selected tag to special item
//     item.classList.toggle("selected");
//     fetchFilteredData(`${item.getAttribute("data-value")}`);
//   });
// });

// async function fetchFilteredData(text) {
//   const response = await fetch(
//     `http://127.0.0.1:8000/courses/categories/${text}/`,
//     {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": getCookie("csrftoken"),
//       },
//       body: JSON.stringify("text"),
//     }
//   );

//   const data = await response.json();
//   // return data.trainers;
//   displayTrainers(data.trainers);
// }

// function displayTrainers(trainers) {
//   listWrap.innerHTML = "";
//   trainers.map((trainer) => {
//     listWrap.innerHTML += `
//     <div class="trainerItem">
//         <div class="profile">
//           <img src="${trainer.image_url}" alt="">
//         </div>
//         <div class="trainerName">${trainer.name}</div>
//         <div class="trainerPosition">
//           ${trainer.profession}
//         </div>
//     </div>
//     `;
//   });
// }

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
