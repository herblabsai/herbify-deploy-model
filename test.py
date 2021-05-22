import requests

# Change 'your-url-here' with your IP address or domain
url = "http://your-url-here:8080/predict"

# Path to image file
image = {"img": open("/path/to/your/image", "rb")}

# Send POST request with image as parameter
req = requests.post(url, files=image)

# Print out the result
print(req.text)