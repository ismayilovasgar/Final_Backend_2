// Handle form submission via Fetch API
document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Prepare the form data
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
        // Handle the response data
        const messageDiv = document.getElementById("message");
        messageDiv.classList.add("active");
        if (data.status === "success") {
          messageDiv.innerHTML = `<p style="color:green;">${data.message}</p>`;
          console.log("+++");
          document.getElementById("contactForm").reset(); // Reset the form on success
        } else {
          messageDiv.innerHTML = `<p style="color:red;">${data.message}</p>`;
          console.log("---");
        }

        setTimeout(() => {
          messageDiv.classList.remove("active");
        }, 2000);
      })
      .catch((error) => {
        const messageDiv = document.getElementById("message");
        // Handle any unexpected errors
        messageDiv.innerHTML = "";
        messageDiv.classList.add("active");

        document.getElementById(
          "message"
        ).innerHTML = `<p style="color:red;">There was an error. Please try again.</p>`;
        setTimeout(() => {
          messageDiv.classList.remove("active");
        }, 2000);
      });
  });
