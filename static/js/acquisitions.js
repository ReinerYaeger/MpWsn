import Chart from "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js";

const url = `ws://${window.location.host}/ws/socket-server/`;
const dataSocket = new WebSocket(url);

document.addEventListener("DOMContentLoaded", function () {
    var gen_chart = {
        type: 'line',

        data: {
            labels: ["Date"],
            datasets: [{
                data: [],
                label: "Average Data",
                backgroundColor: "#3e95cd",
                tension: .1,

            },]
        },
        options: {

            legend: {
                display: true,
                position: "bottom",
                labels: {
                    fontColor: 'rgb(0, 0, 0)'
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    }
    var ctxOne = document.getElementById('acquisitions').getContext('2d');
    const ctx = document.getElementById('acquisitions').getContext('2d');
    var myChart = new Chart(ctx, gen_chart)

    dataSocket.addEventListener('message', function (e) {
        const graphData = JSON.parse(e.data);

        myChart.data.labels.push(graphData.label);
        myChart.data.datasets[0].data.push(graphData['AA']);
        // myChart.data.datasets[0].data.push(graphData.value);
        const maxDataPoints = 100;
        if (myChart.data.labels.length > maxDataPoints) {
            myChart.data.labels.shift();
            myChart.data.datasets[0].data.shift();
        }
        myChart.update();
    });
})