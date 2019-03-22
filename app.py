from flask import Flask, request
import pandas as pd
    
app = Flask(__name__)

'''
Returns [{ network: <IP>, latitude: #, longitude: # }] 
for all IP addresses within a bounding box specified by query params:
@lat: center latitude
@lg: center longitude
@ht: height (in latitude) of bounding box
@width: width (in longitude) of bounding box
Example query: http:/.../?lat=30&lg=20&ht=40&width=30`
'''
@app.route('/')
def get_networks_in_range():
  lat = float(request.args.get('lat'))
  lg = float(request.args.get('lg'))
  height = float(request.args.get('ht'))
  width = float(request.args.get('width'))

  df = pd.read_csv('geolite2-city-blocks-IPv4.csv.gz', compression='gzip', usecols=['network', 'latitude', 'longitude'])
  df = df[(df['latitude'] >= lat - height/2) & (df['latitude'] <= lat + height/2)]
  df = df[(df['longitude'] >= lg - width/2) & (df['longitude'] <= lg + width/2)]
  return df.to_json(orient='records')

if __name__ == '__main__':
  app.run(debug=True)