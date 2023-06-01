
const ctx1 = document.getElementById('myChart1');
    
new Chart(ctx1, {
type: 'bar',
data: {
    labels:  [2020,2021,2022],
    datasets: [{
    label: "Total de consultas com sintomas gripais:",
    data: [419,269,416],
    backgroundColor: [
      'rgba(54, 162, 235, 0.2)'
      ],
      borderColor: [
      'rgb(54, 162, 235)'
      ],
    borderWidth: 1
    }, {
    label: "Total de consultas COVID-19",
    data: [194,115,68],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)'
      ],
      borderColor: [
      'rgb(255, 99, 132)'
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

//gráfico

const ctx = document.getElementById('myChart');
  
new Chart(ctx, {
type: 'bar',
data: {
    labels:  [2019,2020,2021,2022],
    datasets: [{
    label: "Total de consultas",
    data: [392281,398007,309336,568505],
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