window.onload = function () {
    const modal = document.getElementById("resultModal");
    const closeBtn = document.getElementById("closeModal");
    const form = document.getElementById("ticketForm");

    if (typeof priority !== 'undefined' && priority) {
        modal.style.display = "block";
    }

    closeBtn.onclick = function () {
        modal.style.display = "none";
        form.reset();
    };

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
            form.reset();
        }
    };
};
