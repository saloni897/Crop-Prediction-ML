document.querySelector("form").addEventListener("submit", function(e) {
    let inputs = document.querySelectorAll("input");

    for (let input of inputs) {
        if (input.value === "" || isNaN(input.value)) {
            alert("Please enter valid numeric values!");
            e.preventDefault();
            return;
        }
    }
});