# Day 12 - HTTP Requests with Python

# Import modules
from urllib.request import urlopen
import json

# Sample API endpoint (URL)
url = "https://jsonplaceholder.typicode.com/posts/1"

# GET Request:
# urlopen() sends a request to the server and retrieves data.
response = urlopen(url)

# Response:
# The server sends back data in JSON format.

# JSON Payload:
# json.loads() converts the JSON response into a Python dictionary.
data = json.loads(response.read())

# Display the JSON payload
print(data)

# Status Code:
# A status code tells us if the request was successful.
# Common codes:
# 200 = Success
# 404 = Not Found
# 500 = Server Error

# Explanation:
# GET Request  -> Retrieves data from a server.
# Response     -> Data returned by the server.
# Status Code  -> Indicates success or failure of the request.
# JSON Payload -> Structured data returned by the server.