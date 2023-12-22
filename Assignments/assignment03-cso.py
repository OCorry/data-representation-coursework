'''
Assignment 3 - Write a program that retrieves the dataset for the "exchequer account (historical series)"
from the CSO,and stores it into a file called "cso.json" 
'''

#importing libraries
import requests
import json

#Breakdown the URL so that it can be easily amended to search another CSO dataset by only changing the dataset ID
urlBeginning ="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Open the dataset in a json file called cso.json
def getAllAsFile(dataset):
    with open ("cso.json", "wt") as fp:
        #calling the getAll() function created 
        print(json.dumps(getAll(dataset)), file = fp)

def getAll(dataset):
    # building the full url back together 
    url = urlBeginning + dataset + urlEnd
    #Use of try and except to let user know why URL may not be working/connecting
    #https://copyprogramming.com/howto/how-to-get-the-exception-string-from-requests-exceptions-requestexception
    try:
        response = requests.get(url)       
        response.raise_for_status()
        print(response.status_code, "Request Successful")
    except requests.exceptions.HTTPError as errh:
        print("Status 404, URL not found. Please check URL and try again", errh)
    except requests.exceptions.ConnectionError as ece:
        print("Connection Error:", ece)
    except requests.exceptions.Timeout as et:
        print("Timeout Error:", et)
    except requests.exceptions.RequestException as e:
        print("Some Ambiguous Exception:", e)
    try:
        if response.status_code >= 400:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        error_str = str(e)
    # log 'error_str' to disk, a database, etc.
        print('Status 400, Bad request, please review the URL and try again:', error_str)
    # Retrun the data in json format     
    return response.json()

# Defining the main function to call the getAllAsFile() function
if __name__ =="__main__":  
    getAllAsFile("FIQ02")
