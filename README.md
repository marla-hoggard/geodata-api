# Python Flask API for IP addresses by location

A simple Python API for receiving the list of IPv4 networks within a particular geographic area.
Data is pulled from [Geolite](http://geolite.maxmind.com).

## Running locally
```
git clone
cd geodata
python3 -m venv venv
source venv/bin/activate
python app.py
```
Send your query to `http://127.0.0.1:5000/?<query_params>`

## Accessing via Heroku

This app is deployed on Heroku. Send your query to `https://geodata-python-api.herokuapp.com/?<query_params>` to retrieve data without running app locally.

## Query Params

In order to receive data, you will need to include four query params in the url.

The params make up the coordinates (lat/long) of the center of the geographic area as well as the size of the bounding box:
- **lat**: The latitude for the center of the geographic area.
- **lg**: The longitude for the center of the geographic area 
- **ht**: Height (in latitude) of the bounding box 
- **width**: Width (in longitude) of the bounding box

Ex: `https://geodata-python-api.herokuapp.com/?lat=30&lg=20&ht=40&width=30` will return all IPv4 networks that are in a 40x30 box centered at [30, 20]. 
i.e. Any IPv4 networks between 10 and 50 latitude and 5 and 35 longitude.
