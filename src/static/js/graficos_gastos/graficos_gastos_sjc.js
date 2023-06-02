      const ctx1 = document.getElementById('myChart1');
      
      new Chart(ctx1, {
      type: 'bar',
      data: {
          labels:  [2019,2020,2021,2022],
          datasets: [{
          label: "Total de gastos com saúde no primeiro quadrismestre:",
          data: [202971545.28,219782309.70,244265999.47,263560510.55],
          backgroundColor: [
          'rgba(54, 162, 235, 0.2)'
          ],
          borderColor: [
          'rgb(54, 162, 235)'
          ],
          borderWidth: 1
          },]
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

    //gráfico1

    const ctx = document.getElementById('myChart2');
    
      new Chart(ctx, {
      type: 'bar',
      data: {
          labels:  [2019,2020,2021,2022],
          datasets: [{
          label: "Total de gastos com saúde no segundo quadrismestre:",
          data: [237389818.82,276378462.62,290652445.36,305642051.84],
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
    //gráfico2

    const ctx = document.getElementById('myChart3');
    
        new Chart(ctx, {
        type: 'bar',
        data: {
            labels:  [2019,2020,2021,2022],
            datasets: [{
            label: "Total de gastos com saúde no terceiro quadrismestre:",
            data: [271364555.62,287390845.76,285709597.06,319894667.89],
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