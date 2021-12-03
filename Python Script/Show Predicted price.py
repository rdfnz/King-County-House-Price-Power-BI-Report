import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "data":
    [
        {
            'bedrooms': str(dataset["Bedroom Value"][0]),
            'bathrooms': str(dataset["Bathrooms Value"][0]),
            'sqft_living': str(dataset["sqft_living Value"][0]),
            'sqft_lot': str(dataset["sqft_lot Value"][0]),
            'floors': str(dataset["floor Value"][0]),
            'waterfront': str(dataset["waterfront Value"][0]),
            'view': str(dataset["view Value"][0]),
            'condition': str(dataset["condition Value"][0]),
            'grade': str(dataset["grade Value"][0]),
            'sqft_above': str(dataset["sqft_above Value"][0]),
            'sqft_basement': str(dataset["sqft_basement Value"][0]), 
            'yr_built': str(dataset["yr_built Value"][0]),
            'yr_renovated': str(dataset["renovated Value"][0]),
            'sqft_living15': str(dataset['sqft_living15'][0]),
            'sqft_lot15': str(dataset['sqft_lot15'][0]),
            'city': str(dataset['city'][0]), 
        },
    ],
}

body = str.encode(json.dumps(data))
url =  ''#Replace with your REST endpoint
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    import re
    result = re.findall("(?<=\[)(.*?)(?=\])", str(result))
    fig = plt.figure(figsize=(5, 1.5))
    text = fig.text(0.5, 0.5, "${:,.2f}".format(round(float(result[0]),3)),
                    ha='center', va='center', size=20)
    text.set_path_effects([path_effects.Normal()])
    plt.show()
except urllib.error.HTTPError as error:
    fig = plt.figure(figsize=(30, 30))
    text = fig.text(0.5, 0.5, data,
                    ha='center', va='center', size=40)
    text.set_path_effects([path_effects.Normal()])
    plt.show()