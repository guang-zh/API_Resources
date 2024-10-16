# Chapter 1
from urllib.request import urlopen


with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)
  

##############################################
# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get("http://localhost:3000/lyrics")


# Print out the text attribute of the response object
print(response.text)


##############################################
# Construct the URL string and pass it to the requests.get() function
response = requests.get("http://localhost:3000/lyrics/random")

print(response.text)


##############################################
# Add the `include_track` parameter
query_params = {'artist': 'Deep Purple', 'include_track': True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)


##############################################
# Create a dictionary with the playlist info
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', params=playlist_data)
print(response.text)
