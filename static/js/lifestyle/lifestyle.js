//? For recieve data with fetch request
const listWrap = document.querySelector(".postBox .postList");
const allListItem = [...document.querySelectorAll(".postNav ul li")];

window.onload = function () {
  // fetchFilteredData("Lifestyle", listWrap);
  // markFirstItem();
};

function markFirstItem() {
  // Select the first item in the list
  const firstItem = document.querySelector(".postNav ul li");

  // Apply a CSS class to mark the first item
  if (firstItem) firstItem.classList.add("selected");
}

allListItem.map((item) => {
  item.addEventListener("click", (e) => {
    // remove all selected tag
    allListItem.forEach((el) => el.classList.remove("selected"));
    // add selected tag to special item
    item.classList.toggle("selected");

    fetchFilteredData(`${item.textContent.toLowerCase()}`, listWrap);
    currentItem = 3;
  });
});
let items = [];
let len = 0;

async function fetchFilteredData(text, wrap) {
  wrap.innerHTML = "";
  await fetch(`http://127.0.0.1:8000/courses/tags/${text}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify("text"),
  })
    .then((response) => response.json())
    .then((data) => {
      data.cards.map((card) => {
        wrap.innerHTML += `
        <div class="postItem">
          <a href="/singleblog/${card.id}" >
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
      items = [...document.querySelectorAll(".postItem")];
      len = items.length;
      loadMoreItems(len, items);
    })
    .catch((error) => console.error("Error fetching data:", error));
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
