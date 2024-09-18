//? For recieve data with fetch request
const cardsContainer = document.querySelector(".postBox .postList");
const allListItem = [...document.querySelectorAll(".postNav ul li")];

let tagSlug = "mindfulness";
localStorage.setItem("tag", tagSlug);
let localStorageKey = localStorage.getItem("tag");

function displayCourses(cards) {
  cardsContainer.innerHTML = "";

  cards.map((card) => {
    cardsContainer.innerHTML += `
    <div class="postItem">
      <a href="/singleblog/${card.course_id}" >
        <div class="postPreview">
            <img src="${card.course_image}" alt="">
        </div>
        <div class="postStatus ${card.course_category}">${card.course_category_long}</div>
        <div class="postSubtitle">${card.course_name}</div>
        <div class="postFoot">
            <div class="postUser">
              <div class="postAvatar">
                <img src="${card.trainer_image_url}" alt="">
              </div>
             <div class="postAuthor">${card.name}</div>
            </div>
            <div class="postDate">${card.course_date}</div>
          </div>
        </a>
   </div>`;
  });
}

let items = [];
let len = 0;

async function searchCoursesByTag(slug) {
  await fetch(`http://127.0.0.1:8000/courses/tags/${slug}/`, {
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
        localStorage.setItem("courses", JSON.stringify(data));
        localStorage.setItem("lastTag", slug); // Store the last used category slug

        // Add the new search results to the container
        displayCourses(data);
      } else {
        console.warn("No data found for the selected category.");
      }

      items = [...document.querySelectorAll(".postItem")];
      len = items.length;
      loadMoreItems(len, items);
    })
    .catch((error) => console.error("Error fetching data:", error));
}

allListItem.map((item) => {
  item.addEventListener("click", (e) => {
    // remove all selected tag
    allListItem.forEach((el) => el.classList.remove("selected"));
    // add selected tag to special item
    item.classList.toggle("selected");

    searchCoursesByTag(`${item.textContent.toLowerCase()}`);

    const tag = item.getAttribute("data-value");

    if (tag) {
      // Perform search by category slug
      searchCoursesByTag(tag);
    }

    currentItem = 3;
  });
});

// On page load, check if there is a last used category slug stored in localStorage
const lastTagSlug = localStorage.getItem("lastTag");
if (lastTagSlug) {
  searchCoursesByTag(lastTagSlug);
}

// On page load, try to load the last search result from localStorage
const storedCards = localStorage.getItem("courses");
if (storedCards) {
  // Display the stored cards on initial page load
  displayCourses(JSON.parse(storedCards));
}

document.addEventListener("DOMContentLoaded", function () {
  const lastTagSlug = localStorage.getItem("lastTag");
  if (lastTagSlug) {
    let lastSelectedItem = document.querySelector(
      `ul li[data-value=${lastTagSlug}]`
    );
    console.log(lastSelectedItem);
    lastSelectedItem.classList.add("selected");
    displayCourses(JSON.parse(localStorage.getItem("courses")));

    // document.querySelector("input.current").value = lastSelectedItem.textContent;
  } else {
    const tag = localStorage.getItem("tag");
    const data = searchCoursesByTag(tag);
    let lastSelectedItem = document.querySelector(
      `ul.list li[data-value=${tag}]`
    );
    lastSelectedItem.classList.add("selected");
    displayCourses(data);
  }
});

//?  For load more button
const loadMoreBtn = document.querySelector(".postBtns button");
loadMoreBtn.addEventListener("click", clickBtn);
const itemsPerPage = 3;
let visibleItems = itemsPerPage;

function loadMoreItems(itemsLength, items) {
  visibleItems = itemsPerPage;

  if (itemsLength <= 3) {
    loadMoreBtn.style.display = "none";
  } else {
    loadMoreBtn.style.display = "block";
  }

  items.forEach((item, index) => {
    if (index >= visibleItems) {
      item.style.display = "none";
    }
  });
}

function clickBtn() {
  items = [...document.querySelectorAll(".postItem")];
  len = items.length;
  let index = 0;
  visibleItems += itemsPerPage;
  items.forEach((item, index) => {
    if (index < visibleItems) {
      item.style.display = "block";

      if (index == len - 1) {
        loadMoreBtn.style.display = "none";
      }
    }
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

// ? Community Send Message Code
// Handle form submission via Fetch API
const mailForms = document.querySelectorAll("form.subscription");
mailForms.forEach((element) => {
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
