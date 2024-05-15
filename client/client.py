import json
import sys
import requests
import base64

if __name__ == '__main__':
    # Loading the config and defining the full endpoint URI
    with open(sys.argv[1], 'r') as f:
        config = json.load(f)
    service = 'http://' + config['HOST'] + ':' + config['PORT'] + '/process-image'

    # Read the image and encode it in base64
    with open(sys.argv[2], 'rb') as f:
        encoded_img = base64.b64encode(f.read()).decode('utf-8')

    # Send the request to the endpoint and process the returned json object
    response = requests.post(service, json={'image': encoded_img})
    if response.status_code == 200:
        processed_img = base64.b64decode(response.json()['image'])
        with open(sys.argv[3], 'wb') as f:
            f.write(processed_img)
    else:
        raise Exception(f"Invalid response from server: {response.json()['error']}")
