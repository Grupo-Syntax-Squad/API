
const ctx = document.getElementById('myChart');
    
new Chart(ctx, {
type: 'bar',
data: {
    labels:  [2019,2020,2021,2022],
    datasets: [{
    label: "Total gasto com medicamentos",
    data: [9276151.24,14695626.92,13989926.5,15458099.04],
    backgroundColor: [
      'rgba(75, 192, 192, 0.2)'
      ],
      borderColor: [
      'rgb(75, 192, 192)'
      ],
    borderWidth: 1
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
    y: {
        beginAtZero: true
    }
    }
}
});
