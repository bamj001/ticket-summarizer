window.onload = function () {
    const modal = document.getElementById("resultModal");
    const closeBtn = document.getElementById("closeModal");
    const form = document.getElementById("ticketForm");

    // Check if priority is set and then show modal
    if (typeof priority !== 'undefined' && priority) {
        modal.style.display = "block";
    }

    // Close modal functionality
    closeBtn.onclick = function () {
        modal.style.display = "none";
        form.reset();
    };

    // Close modal if clicked outside
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
            form.reset();
        }
    };
};

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("ticketForm");
    const spinnerContainer = document.getElementById("loading-spinner-container");

    if (form) {
        form.addEventListener("submit", (event) => {
            event.preventDefault(); // Prevent default form submission

            // Show the spinner container
            if (spinnerContainer) {
                spinnerContainer.style.display = "block";  // Make it visible
            }

            // Simulate a delay before submitting the form
            setTimeout(() => {
                form.submit();  // Submit the form after a short delay
            }, 1000);  // Adjust the delay as needed (in ms)
        });
    }
});


