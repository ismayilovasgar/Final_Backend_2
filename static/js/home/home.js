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
const listWrap = document.querySelector(".trainersList  .listWrap");
const allListItem = [...document.querySelectorAll("ul.list li")];

// document.addEventListener("DOMContentLoaded", function () {
//   const categorySlug = "yoga"; // Replace with the actual category slug
//   const localStorageKey = `trainers_${categorySlug}`;
//   const trainersContainer = document.querySelector(".trainersList  .listWrap");

//   // Function to display trainer cards
//   function displayTrainers(data) {
//     listWrap.innerHTML = "";
//     data.map((trainer) => {
//       listWrap.innerHTML += `
//       <div class="trainerItem">
//           <div class="profile">
//             <img src="${trainer.image_url}" alt="">
//           </div>
//           <div class="trainerName">${trainer.name}</div>
//           <div class="trainerPosition">
//             ${trainer.profession}
//           </div>
//       </div>
//       `;
//     });
//   }

//   // Function to update Local Storage with new data
//   function updateLocalStorage(trainers) {
//     localStorage.setItem(localStorageKey, JSON.stringify(trainers));
//   }

//   // Check Local Storage first
//   const storedData = localStorage.getItem(localStorageKey);
//   if (storedData) {
//     displayTrainers(JSON.parse(storedData)); // Display cached data
//   }
//   const data = fetchFilteredData(categorySlug);
//   if (data.trainers) {
//     updateLocalStorage(data.trainers); // Update Local Storage
//     displayTrainers(data.trainers); // Display new data
//   } else {
//     console.log("++++");
//     trainersContainer.innerHTML = "No trainers found.";
//   }
// });
//
//
//
//

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
    fetchFilteredData(`${item.getAttribute("data-value")}`);
  });
});

async function fetchFilteredData(text) {
  const response = await fetch(
    `http://127.0.0.1:8000/courses/categories/${text}/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify("text"),
    }
  );

  const data = await response.json();
  // return data.trainers;
  displayTrainers(data.trainers);
}

function displayTrainers(trainers) {
  listWrap.innerHTML = "";
  trainers.map((trainer) => {
    listWrap.innerHTML += `
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
