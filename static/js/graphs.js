function render_countries(countries) {

    // var countries = JSON.parse('{{ countries | tojson | safe}}');
    console.log(countries)
  
    $(document).ready(function () {
      $("#vmap").vectorMap({
        map: 'world_en',
        backgroundColor: 'white',
        borderColor: 'white',
        color: 'blue',
        hoverOpacity: 0.7,
        selectedColor: '#666666',
        enableZoom: false,
        enableDrag: true,
        showTooltip: true,
        normalizeFunction: 'polynomial',
        onLabelShow: function (event, label, code) {
        
          code = code.toUpperCase();
          engagements = countries[code];
          label.html('<strong>' + engagements);
        }
      });
    });
}
