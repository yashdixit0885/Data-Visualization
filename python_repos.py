import requests

# Make an API call and store the response
def github_call(url,headers=''):
    r = requests.get(url,headers=headers)
    
    return r



def response_display(s):
    #Store API response in a variable
    response_dict = s.json()
    print(f"Total repositories:{response_dict['total_count']}")

    #Explore information about the repositories
    repo_dicts = response_dict['items']
    print(f"Repositories returned:{len(repo_dicts)}")

    #Examine the first repo

    print("\nSelected information about each repo:")

    for repo_dict in repo_dicts:
        print(f"\nName : {repo_dict['name']}")
        print(f"Owner:{repo_dict['owner']['login']}")
        print(f"Stars:{repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Description:{repo_dict['description']}")

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
response= github_call(url,headers=headers)
print(f"Status code:{response.status_code}")
response_display(response)