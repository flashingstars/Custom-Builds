document.addEventListener("DOMContentLoaded", function() {
    // Add functionality to the like buttons
    let likeButtons = document.getElementsByClassName("like-btn");
    for (let i = 0; i < likeButtons.length; i++) {
      let likeCount = 0; // Initial like count
  
      likeButtons[i].addEventListener("click", function() {
        this.classList.toggle("liked");
        if (this.classList.contains("liked")) {
          likeCount++;
        } else {
          likeCount--;
        }
        updateLikeCount(this, likeCount);
      });
    }
  
    // Function to update the like count
    function updateLikeCount(button, count) {
      let likeCountElement = button.querySelector(".like-count");
      likeCountElement.textContent = count;
    }
  });
  
// Add functionality to the order buttons
let orderButtons = document.getElementsByClassName("order-btn");
for (let i = 0;  i < orderButtons.length; i++) {
    orderButtons[i].addEventListener("click", function() {
        let card = this.parentNode;
        let title = card.querySelector("h2").innerText;
        let price = card.querySelector(".price").innerText;

        let order = {
            title: title,
            price: price
        };

        fetch("/order", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON,stringify(order)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("order placed! It should reflect on the custom builds page");
            } else {
                alert("Failed to place the order. Please try again.");
            }
        })
        .catch(error => {
            alert("An error occured while processing the order. Please try again later.");
            console.error(error);
        });
    });
}