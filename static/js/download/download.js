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
// ? Fetch Button Click Method
// const mailForm = document.getElementById("contactForm");
// const formButton = document.getElementById("mailFormButton");
// const emailAddress = document.getElementById("email_input");
// //
// mailForm.addEventListener("submit", async (e) => {
//   fetchPostByMail(emailAddress.value);
// });

// async function fetchPostByMail(str_email) {
//   //
//   const url = "http://127.0.0.1:8000/joinmebymail/";
//   const emailData = {
//     email: `${str_email}`,
//   };
//   //
//   try {
//     const response = await fetch(`${url}`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": getCookie("csrftoken"),
//       },
//       body: JSON.stringify(emailData),
//     });
//     const data = await response.json();
//     console.log(data);
//     //
//   } catch (error) {
//     console.log(error);
//     return []; // Return an empty array in case of an error
//   }
// }

// // ? csrf token
// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
