var columnWidth = 200;
function changeWidth(scale) {
    columnWidth *= scale;
    // Select all div, p, and td elements
    const elements = document.querySelectorAll("div, p, td");

    // Loop through each element and update its width
    elements.forEach(function (element) {
        console.log(element.className);
        if (element.className === "") {
            element.style.width = columnWidth + "px";  // Set new width
        } else if (element.className === "fixwtd") {
            element.style.width = columnWidth + "px";  // Set new width
        }
    });
}