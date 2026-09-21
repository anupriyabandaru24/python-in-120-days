import requests

def get_random_activity():
    response=requests.get("https://bored-api.appbrewery.com/random")
    data=response.json()
    return data["activity"]

print(get_random_activity())    

def get_github_user(username):
    response=requests.get(f"https://api.github.com/users/{username}")
    data=response.json()
    return (data["name"],data["public_repos"])

print(get_github_user("octocat"))

def get_status_code(url):
    response=requests.get(url)
    return response.status_code

print(get_status_code("https://api.github.com"))   # 200
print(get_status_code("https://api.github.com/nonexistent-endpoint-xyz")) 

def safe_get_json(url):
    try:
       response=requests.get(url)
       data=response.json()
       return data
    except requests.exceptions.RequestException as e:
           return "Request failed"

print(safe_get_json("https://api.github.com/users/octocat"))
print(safe_get_json("https://this-does-not-exist-xyz123.com"))
# Second call: "Request failed" (connection error caught gracefully) 

def get_dog_image():
    response=requests.get("https://dog.ceo/api/breeds/image/random")
    data=response.json()
    return data["message"]

print(get_dog_image()) 

def get_multiple_activities(n):
    i=0
    list_activity=[]
    while i<n:
         response=requests.get("https://bored-api.appbrewery.com/random")
         data=response.json()
         list_activity.append(data["activity"])
         i+=1
    return list_activity

print(get_multiple_activities(3))
# ['Play a video game', 'Learn to whistle', 'Go for a walk']  (actual results will vary)

def get_country_info(country_name):
    response=requests.get(f"https://countries.dev/alpha/{country_name}")
    data=response.json()
    return data["capital"]
print(get_country_info("IN"))

def check_multiple_sites(urls):
    dict_urls={}
    for i in urls:
        try:
           response=requests.get(i)
           code=response.status_code
           dict_urls[i]=code
        except requests.exceptions.RequestException as e: 
               dict_urls[i]="Error"
    return dict_urls
urls = ["https://api.github.com", "https://this-site-does-not-exist-xyz.com"]
print(check_multiple_sites(urls))
# {'https://api.github.com': 200, 'https://this-site-does-not-exist-xyz.com': 'Error'}  

def get_joke():
    response=requests.get("https://official-joke-api.appspot.com/random_joke")
    data=response.json()
    return data["setup"]+" "+data["punchline"]
print(get_joke()) 

def search_github_repos(query,limit=5):
    response=requests.get(f"https://api.github.com/search/repositories?q={query}")
    data=response.json()
    items = data["items"]
    names=[]
    for repo in items[:limit]:
        names.append(repo["name"])
    return names    
print(search_github_repos("python"))