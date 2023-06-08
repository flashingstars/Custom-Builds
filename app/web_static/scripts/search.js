// Script that manipulates the search dropdown

// Toggle dropdown content
document.getElementById("dropdown-btn").addEventListener("click", function() {
    let dropdownContent = document.getElementById("dropdown-content");
    dropdownContent.classList.toggle("show");
});

// Close dropdown content when clicking outside the dropdown
window.addEventListener("click", function(event) {
    if (!event.target.matches(".dropdown-toggle")) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            let dropdown = dropdowns[i];
            if (dropdown.classList.contains("show")) {
                dropdown.classList.remove("show");
            }
        }
    }
});