import requests
import json
#Testing the get function 
"""
url = "http://google.com"
response = requests.get(url)
print (response.text)
"""
URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    try: 
        response = requests.get(URL)
        response.raise_for_status()
        print(response.status_code, "Request Successful")
    except requests.exceptions.HTTPError as errh:
        print("Status 404, URL not found. Please check spelling and try again")
        print(errh.args[0])

    return response.json()

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

def updatebook(id, bookdiff):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()





if __name__ == "__main__":
    book ={
        'Author':"Orla",
        'Title' :"Hello World",
        'Price' : 1230
    }

    bookdiff ={
        'Author':"Mary",
        'Title' :"Hellooo World!!",
        'Price' : 100
    }
    
    print (readbooks())
    #print (readbook(326))
    #print (createbook(book))
    #print (updatebook(327, bookdiff))
    #print (deletebook(327))
