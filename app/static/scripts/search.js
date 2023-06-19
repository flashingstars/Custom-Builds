// Show dropdown content when search box is clicked
document.getElementById("search-input").addEventListener("click", function() {
    let dropdownContent = document.getElementById("dropdown-content");
    dropdownContent.classList.add("show");
  });
  
  // Close dropdown content when clicking outside the dropdown or search box
  window.addEventListener("click", function(event) {
    if (!event.target.matches(".dropdown-toggle") && !event.target.matches("#search-input")) {
      let dropdowns = document.getElementsByClassName("dropdown-content");
      for (let i = 0; i < dropdowns.length; i++) {
        let dropdown = dropdowns[i];
        if (dropdown.classList.contains("show")) {
          dropdown.classList.remove("show");
        }
      }
    }
  });
  