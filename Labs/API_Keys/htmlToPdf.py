import requests
import urllib.parse
#importing the config dict from config.py
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#using the variable htmltopdfkey in place of the API
apiKey = cfg["htmltopdfkey"]

#Target URL example from html2pdf documentation:
#https://api.html2pdf.app/v1/generate?html=https://example.com&apiKey={your-api-key}
#the parameters for the target url are stored as a dict below rather than having them all in the one URL like the 
#example given in the documentation

#Setting up the Target URL
apiurl = 'https://api.html2pdf.app/v1/generate'

# Parameters are the target URL and the API key
params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams
#print(requestUrl)

#Using get request to get the URL 
response = requests.get(requestUrl)
#Print response code to the terminal to show if there are any issues with the url requested 
print (response.status_code)

#put the content of the url into a file called document.pdf 
result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)


 