/* global Chart, coreui */

/**
 * --------------------------------------------------------------------------
 * CoreUI Boostrap Admin Template (v4.2.1): main.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */
// Disable the on-canvas tooltip
Chart.defaults.pointHitDetectionRadius = 1;
Chart.defaults.plugins.tooltip.enabled = false;
Chart.defaults.plugins.tooltip.mode = 'index';
Chart.defaults.plugins.tooltip.position = 'nearest';
Chart.defaults.plugins.tooltip.external = coreui.ChartJS.customTooltips;
Chart.defaults.defaultFontColor = '#646470';

const random = (min, max) => // eslint-disable-next-line no-mixed-operators
  Math.floor(Math.random() * (max - min + 1) + min); // eslint-disable-next-line no-unused-vars




function render_main_graph(projects) {


  const ctx = document.getElementById('main-chart');



  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
      datasets: [{
        label: '# of Engagements',
        data: projects,
        borderWidth: 1,
        borderColor: '#5EAFD3',
        backgroundColor: '#5EAFD3',

      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });




}





