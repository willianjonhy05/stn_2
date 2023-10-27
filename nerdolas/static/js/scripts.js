document.addEventListener("DOMContentLoaded", function () {
    const deleteLinks = document.querySelectorAll(".delete-nerd");

    deleteLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            if (!confirm("Tem certeza de que deseja apagar este Nerd?")) {
                e.preventDefault();
            }
        });
    });
});
