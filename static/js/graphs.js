function toLowerKeys(obj) {
  return Object.keys(obj).reduce((accumulator, key) => {
    accumulator[key.toLowerCase()] = obj[key];
    return accumulator;
  }, {});
}

function get_colors(countries) {

  var countries=toLowerKeys(countries)

  var max = 0,
    min = Number.MAX_VALUE,
    cc,
    startColor = [200, 238, 255],
    endColor = [0, 100, 145],
    colors = {},
    hex;

  //find maximum and minimum values
  for (cc in countries) {
    if (parseFloat(countries[cc]) > max) {
      max = parseFloat(countries[cc]);
    }
    if (parseFloat(countries[cc]) < min) {
      min = parseFloat(countries[cc]);
    }
  }

  //set colors according to values of GDP
  for (cc in countries) {
    if (countries[cc] > 0) {
      colors[cc] = '#';
      for (var i = 0; i < 3; i++) {
        hex = Math.round(startColor[i]
          + (endColor[i]
            - startColor[i])
          * (countries[cc] / (max - min))).toString(16);

        if (hex.length == 1) {
          hex = '0' + hex;
        }
        
        colors[cc] += (hex.length == 1 ? '0' : '') + hex;
        
      }
    }
  }

  return colors
}



function render_countries(countries) {

  // var countries = JSON.parse('{{ countries | tojson | safe}}');
  // console.log(countries)

  $(document).ready(function () {
    $("#vmap").vectorMap({
      map: 'world_en',
      backgroundColor: 'white',
      borderColor: '#818181',
      borderOpacity: 0.25,
      borderWidth: 1,
      color: '#4B4B4B',
      enableZoom: false,
      hoverColor: '#c9dfaf',
      hoverOpacity: null,
      normalizeFunction: 'linear',
      scaleColors: ['#b6d6ff', '#005ace'],
      selectedColor: '#c9dfaf',
      selectedRegions: null,
      showTooltip: true,
      onLabelShow: function (event, label, code) {

        code = code.toUpperCase();
        engagements = countries[code];
        label.html('<strong>' + engagements);
      }
    });
     colors=get_colors(countries)
    jQuery('#vmap').vectorMap('set', 'colors', colors);
  });

}


