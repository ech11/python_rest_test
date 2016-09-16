'''
this micro service returns address and authors comment given lat/lon.

google maps api is used to lookup address given lat/lon:
https://maps.googleapis.com/maps/api/geocode/json?latlng

for reference, inverse (lookup lat/lon given address is:
https://maps.googleapis.com/maps/api/geocode/json?address
'''
from flask import Flask, Response
import os, sys
import urllib
import json

app = Flask(__name__)

#returns address from google api given lat and lon
@app.route('/ll/api/1.0/address/<lat>/<lon>', methods=['GET'])
def get_address(lat, lon):
    #todo1 - cache lat/lon response
    #todo2 - ability to switch geo providers is nice
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s' % (lat, lon)
    u = urllib.urlopen(url)
    res = u.read()
    json_data = json.loads(res)
    try:
        state = json_data['results'][0]['address_components'][6]['short_name'] #yikes
        address = json_data['results'][0]['formatted_address'] #yikes2
    except:
        state = None
        address = 'Move Out Of The Sticks!!'
    comment = (state == 'NY') and 'nice place' or 'move to a better state!'
    res = {'address':address, 'comment':comment}
    res = str(res)

    resp = Response(response=res, status=200, mimetype="application/json")
    return(resp)

if __name__ == '__main__':
    app.run(debug=True)
