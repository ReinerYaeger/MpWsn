function main_map_init(map, options) {
    var dataurl = '{% url "sensor_dataset" %}';

    $.getJSON(dataurl, function (data) {
        L.geoJSON(data, {
            pointToLayer: function (feature, latlng) {
                var soilMoisture = feature.properties.sensor_data;
                var marker = new L.Marker(latlng)
                    .bindPopup('<h5><b>' + feature.properties.sensor_group_name + '</b></h5>' +
                        '<p>Soil Moisture: ' + soilMoisture + '</p>');
                return marker
            },
        }).addTo(map);
    });

    var dataBtn = new L.Control.Button('dataBtn', {
        toggleButton: 'active',
        position: 'topleft',
    });

    dataBtn.addTo(map);

    dataBtn.on('click', function () {
        rightSidebar.toggle();
    });

    const rightSidebar = L.control.sidebar('sidebar-right', {
        closeButton: true,
        position: 'right'
    }).addTo(map);
}

// Initialize the Leaflet map
var mainMap = L.map('main_map').setView([18.1096, -77.2975], 10);

// Add a tile layer (adjust the URL as needed)
L.tileLayer('http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
}).addTo(mainMap);

// Call the initialization function
main_map_init(mainMap);