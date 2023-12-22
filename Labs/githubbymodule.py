from github import Github

apikey =["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"]
# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)