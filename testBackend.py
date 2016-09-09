#oggpnosn 
#hkhr 

#testing backend 

from urllib import urlencode
from urllib2 import urlopen
from urllib2 import Request
import json
import sys 
import json 



data = {'T': 18000,
 'interest': 'Sights & Landmarks',
 'latitude': 15.2826122,
 'longitude': 73.9576572}

# url = "http://localhost:8000/"
url = "http://wunderlust-c7579.appspot.com/"

request = Request(url, data=urlencode(data))
response = urlopen(request)
data = json.loads(response.read())
print data
latlng = []
for location in data:
    latlng.append({"lat": location["latitude"], "lng": location["longitude"]})

text = """ 
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple icons</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      // This example adds a marker to indicate the position of Bondi Beach in Sydney,
      // Australia.
      var ambulances = BAZINGA ;
      function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 12,
          center: ambulances[0]
        });

        // var image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
        var i;
        for(i=0; i<ambulances.length; i++){
          var beachMarker = new google.maps.Marker({
            position: ambulances[i],
            map: map
          });
        }
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD-i-lZjkM5lSE_cf6fn_EQN4BP_M98H5E&callback=initMap">
    </script>
  </body>
</html>
"""

text = text.replace("BAZINGA", str(latlng))
fob = open("visualizeGeocoordinate.html", "w")
fob.write(text)
fob.close()

from subprocess import call 
call(["open", "visualizeGeocoordinate.html"])


