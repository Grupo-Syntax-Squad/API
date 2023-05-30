     const ctx = document.getElementById('myChart');
    
    new Chart(ctx, {
    type: 'bar',
    data: {
        labels:  [2019,2020,2021,2022],
        datasets: [{
        label: "Total gasto com medicamentos",
        data: [2198546.45,1325888.37,1288791.62,2337375.98],
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