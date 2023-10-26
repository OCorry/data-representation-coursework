from github import Github
from config import config as cfg 
import requests

apikey= cfg["githubkey"]

g = Github(apikey)

#Show all repos the the API key has allowed the user access to 
#for repo in g.get_user().get_repos():
    #print(repo.name)

#Show url of the privatetestrepo only 
repo = g.get_repo("OCorry/privatetestrepo")
#print(repo.clone_url)

#Show the url of the text file inside the repo
fileInfo =repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

#Show the contents of the test.txt file
response = requests.get(urlOfFile)
contentsOfFile = response.text
print (contentsOfFile)

#Add more text to the file
newContents = contentsOfFile +"more stuff2 \n"
print(newContents)

#Upload the contents of the file back up to github
gitHubResponse= repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)                                
print (gitHubResponse)