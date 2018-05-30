
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";


d3.json(queryUrl, function(data) {

  createFeatures(data.features);
});

function createFeatures(earthquakeData) {


  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
  }


  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature
  });


  createMap(earthquakes);
}

function createMap(earthquakes) {


  var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/dbruec1/cjhjjxs0u067j2rqy72pp9rgl/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGJydWVjMSIsImEiOiJjamhqanI2anQwMjl1MzByMG4wMjYzNGVuIn0.XgoEKyYg1er69yhDLcxlOA");


  var baseMaps = {
    "Street Map": streetmap
  };


  var overlayMaps = {
    Earthquakes: earthquakes
  };


  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [streetmap, earthquakes]
  });


  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}
