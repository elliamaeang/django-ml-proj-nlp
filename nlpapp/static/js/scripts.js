
/* Credit: W3Schools (https://www.w3schools.com/graphics/plot_chartjs.asp)  */

// Initialize chart variables
var targets = ["Negative", "Neutral", "Positive"];
var colors = ["#fb6353", "#fbcf6a", "#59c859"];

// Create chart and draw on canvas with ID pie-chart
new Chart("pie-chart", {
    type: "pie",
    data: {
      labels: targets,
      datasets: [{
        backgroundColor: colors,
        data: percent
      }]
    }
  });