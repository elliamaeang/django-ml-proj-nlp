
var xValues = ["Negative", "Neutral", "Positive"];
var barColors = ["#e96258", "#efce42", "#3cb14f"];

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