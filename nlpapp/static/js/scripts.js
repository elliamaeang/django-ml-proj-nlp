
var xValues = ["Negative", "Neutral", "Positive"];
var barColors = ["#fb6353", "#fbcf6a", "#94e36b"];

new Chart("pie-chart", {
    type: "pie",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
      }]
    },
    options: {
    }
  });