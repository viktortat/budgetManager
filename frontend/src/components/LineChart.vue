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
                labels: ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec"],
                datasets: [
                {
                    label: "Příjmy",
                    backgroundColor: 'rgba(8, 210, 111, 0.2)',
                    borderColor: 'rgba(8, 210, 111, 1)',
                    data: [10, 500, 2, 200, 100, 30, 45],
                    pointRadius: 0
                },
                {
                    label: "Výdaje",
                    backgroundColor: 'rgba(255, 92, 135, 0.2)',
                    borderColor: 'rgba(255, 92, 135, 1)',
                    data: [400, 100, 20, 50, 160, 430, 15],
                    pointRadius: 0
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
