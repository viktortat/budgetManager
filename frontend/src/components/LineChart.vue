<template>
    <canvas id="lineChart"></canvas>
</template>

<script>
import Chart from "chart.js"

export default {
    mounted() {
        var ctx = document.getElementById('lineChart');
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July"],
                datasets: [{
                    label: "My First dataset",
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [10, 500, 2, 200, 100, 30, 45],
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
}
</script>


<style lang="stylus" scoped>


</style>
