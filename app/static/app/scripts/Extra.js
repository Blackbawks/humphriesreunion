function initMap() {
    var mapOptions = {
        center: new google.maps.LatLng(49.127778, -53.610833),
        zoom: 6,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };


    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var markers = [
          ['Valleyfield, Newfoundland', 49.127778, -53.610833],          
    ];


    // markers & place each one on the map  
    for (i = 0; i < markers.length; i++) {
        var position = new google.maps.LatLng(markers[i][1], markers[i][2]);

        marker = new google.maps.Marker({
            position: position,
            map: map,
            title: markers[i][0]
        });



  }

}



