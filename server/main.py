import json
import sys
from api import app


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("No config file provided!")
        print(f"Usage: {sys.argv[0]} <path-to-config>")
        exit(-1)

    # Loading the config and starting the Flask server
    with open(sys.argv[1], "r") as f:
        config = json.load(f)
    app.run(host=config['HOST'], port=config['PORT'], debug=False)
