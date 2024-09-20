// Get the table element
var hiddenRows = 0;

function hideRows(step) {
    hiddenRows += step;
    var table = document.getElementById("cards");

    // Loop through the first 10 rows and hide them
    for (var i = 0; i < hiddenRows; i++) {
        table.rows[i].style.display = "none"; // +1 to skip the header row
    }

}