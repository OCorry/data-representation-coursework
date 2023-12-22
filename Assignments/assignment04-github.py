#Write a program that reads in a file from a repository  
#The program should replace all the instances of the text "Andrew" with my name
#The program should then commit those changes and push the updated file back to the repository

#Importing GitHub
from github import Github
#Importing the config Module created in another file which contains the API key 
from config2 import config as cfg 
#To send HTTP requests
import requests

#Storing the api key which has been inmpoted from another file 
apikey = cfg["GitHubApiKey"]

#Telling python it is a GitHub API key and storing as variable as 'g'
g = Github(apikey)

#Show all repos the the API key has allowed the user access to 
#for repo in g.get_user().get_repos():
    #print(repo.name)

#Show url of the privatetestrepo only and store as variable 'repo'
repo = g.get_repo("OCorry/privatetestrepo")
#print(repo.clone_url)

#Show the url of the text file inside the repo
fileInfo =repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

#Show the contents of the test.txt file
response = requests.get(urlOfFile)
contentsOfFile = response.text
#Print status code to terminal to tell user if error or successful
print (response.status_code)
#Print contents of file to terminal 
#print (contentsOfFile)

#Add more text to the file
newContents = contentsOfFile +("Andrew \n" "Mike \n" "Mary \n" "Joe \n" "Lisa \n" "Kevin \n" "Andrew \n" "Martin\n" 
                               "John \n" "Andrew \n" "Gerard \n" "Sarah \n" "Andrew \n" "Jessie \n" "Andrew \n")
#Print the added text to the terminal 
#print(newContents)


#Replacing every instance of text "Andrew" with "Orla"
#Code adapted from: https://www.programiz.com/python-programming/methods/string/replace#:~:text=The%20replace()%20method%20returns,copy%20of%20the%20original%20string.

#Storing as new variable "replacedContents" 
replacedContents = newContents.replace('Andrew', 'Orla')
#print(replacedContents)

#Upload the contents of the updated file back up to github
#Using the new variable "replacedContents" to push the replaced contents rather than the "newContents" that were nputted by user
# "updated by prog is the commit message that appears in Github"
gitHubResponse= repo.update_file(fileInfo.path,"updated by prog",
replacedContents,fileInfo.sha)   
#Printing GitHub response to terminal to show if the commit to GitHub was successful                              
#print (gitHubResponse)