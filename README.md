# Simple IMG
This is a simple backend with a sample client for image uploading and processing.

## Usage

### Install dependencies
First, create and activate a Python virtual environment by
```shell
python -m venv venv
source venv/bin/activate
```
Then install all the required dependencies
```shell
pip install -r requirements.txt
```

### Starting the server
Before starting the server, please make sure you have the correct configuration. Check the [sample configuration](https://github.com/caesarw/simple-img/blob/master/server/config.json) and adjust it to your need.   

To start the server, run the following
```shell
python server/main.py <path-to-config>
# for example, if your config file is at the root of the project folder, run
# python server/main.py config.json
```

> [!WARNING] 
> If you plan to run Flask in production, it's best practice to configure it with WSGI and a web server.  

### Using the client
Before using the client, please make sure you have the correct configuration. Check the [sample configuration](https://github.com/caesarw/simple-img/blob/master/client/config.json) and adjust it to your need. 
Also make sure you have a valid server instance running.  

Then run the following
```shell
python client/client.py <path-to-config> <path-to-image> <path-to-new-image>
# for example, if your config file is at the root of the project folder, run
# python client/client.py config.json client/image.png client/image_new.png 
# this will use client/image.png as the source image, and generate a processed image
# at client/image_new.png
```
If no error is reported, you should see the processed image at `client/image_new.png`.  
If there's any error during processing, you will receive a `JSON` object with `image` being `null` and `error` being the error message.  