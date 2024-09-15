// ! Swiper - 1
// let swiper_programs = new Swiper(".programs_swiper", {
//   grabCursor: true,
//   slidesPerView: 3,
//   spaceBetween: 24,
//   pagination: {
//     el: ".swiper-pagination",
//     type: "fraction",
//     clickable: true,
//   },
//   navigation: {
//     nextEl: ".programs_next_btn",
//     prevEl: ".programs_prev_btn",
//   },
//   breakpoints: {
//     0: {
//       slidesPerView: 1,
//     },

//     700: {
//       slidesPerView: 2,
//     },
//     1024: {
//       slidesPerView: 2,
//     },
//   },
// });

// async function fillDemo(data) {
//   listWrap.innerHTML = "";
//   data.map((item) => {
//     listWrap.innerHTML += `
//       <div class="trainerItem">
//               <div class="profile">
//                 <img src="${item.trainer_image}" alt="">
//               </div>
//               <div class="trainerName">${item.fullname}</div>
//               <div class="trainerPosition"> ${item.profession} </div>
//       </div>

//       <div class="modal" id="">
//                       <div class="modalContent">
//                           <div class="popupContainer">

//                               <div class="trainerTop">
//                                   <div class="trainerAvatar">
//                                       <img src="${item.trainer_image}" alt="">
//                                   </div>
//                                   <div class="trainerName">${
//                                     item.fullname
//                                   }</div>
//                                   <div class="trainerPosition">${
//                                     item.profession
//                                   }</div>
//                                   <div class="trainerSocials">
//                                       <a href="${
//                                         item.facebook
//                                       }" target="_blank" class="trainer_social">
//                                           <i class="fa-brands fa-facebook"></i>
//                                       </a>
//                                       <a href="${
//                                         item.instagram
//                                       }" target="_blank" class="trainer_social">
//                                           <i class="fa-brands fa-instagram"></i>
//                                       </a>
//                                       <a href="${
//                                         item.twitter
//                                       }" target="_blank" class="trainer_social">
//                                           <i class="fa-brands fa-twitter"></i>
//                                       </a>
//                                       <a href="${
//                                         item.linkedin
//                                       }" target="_blank" class="trainer_social">
//                                           <i class="fa-brands fa-linkedin"></i>
//                                       </a>
//                                   </div>
//                               </div>
//                               <form action="" method="/" class="subscriptionInput">
//                                   <input class="subscription__input" type="email" placeholder="Find a class"
//                                       required="required">
//                                   <button class="subscriptionBtn">
//                                       <i class="fa-solid fa-arrow-right"></i>
//                                   </button>
//                               </form>

//                               <div class="trainerModalWrap programs_swiper2">
//                                   <div class="trainerSlider swiper-wrapper">
//                                   ${item.courses
//                                     .map(
//                                       (el) => `
//                                           <div class="card programs_swiper">
//                                               <div class="trainerPreview">
//                                                   <img src="${el.image}" alt="">
//                                                   <p>${el.category}</p>
//                                               </div>
//                                               <div class="modalTrainerHead">
//                                                   <div class="trainer__title">${truncateString(
//                                                     el.description,
//                                                     25
//                                                   )}</div>
//                                                   <div class="trainerLevel">${
//                                                     el.level
//                                                   }</div>
//                                               </div>
//                                               <div class="trainerParameters">
//                                                   <div class="trainerParameter">
//                                                      <i class="fa-brands fa-youtube"></i>
//                                                      <span>7</span>
//                                                   </div>
//                                                   <div class="trainerParameter">
//                                                     <i class="fa-regular fa-user"></i>
//                                                     <span>160</span>
//                                                   </div>
//                                               </div>
//                                           </div>
//                                        `
//                                     )
//                                     .join("")}
//                                   </div>
//                               </div>

//                               <div class="bottomBtns">
//                                   <div class="arrowBtns">
//                                       <i class="fa-solid fa-left-long"></i>
//                                      <i class="fa-solid fa-right-long"></i>
//                                   </div>
//                                   <button class="btn btn_orange">Browse all class</button>
//                               </div>

//                               <button title="Close (Esc)" type="button" class="modalCloseBtn">
//                                  <i class="fa-solid fa-xmark"></i>
//                               </button>

//                           </div>
//                       </div>
//               </div>

//       `;
//   });

//   const trainers = [...document.querySelectorAll(".listWrap .trainerItem")];
//   const closeBtns = [...document.querySelectorAll(".modal .modalCloseBtn")];

//   trainers.forEach((trainer) => {
//     trainer.addEventListener("click", (e) => {
//       // trainer.nextElementSibling.style.display = "block";
//       trainer.nextElementSibling.classList.add("showed");
//       e.preventDefault();
//     });
//   });

//   closeBtns.forEach((closeBtn) => {
//     closeBtn.addEventListener("click", (e) => {
//       // closeBtn.closest(".modal").style.display = "none";
//       closeBtn.closest(".modal").classList.remove("showed");
//     });
//   });

//   //
//   window.onclick = function (event) {
//     const modal = document.querySelector(".modal.showed");

//     if (event.target == modal) {
//       modal.classList.remove("showed");
//     }
//   };
// }
