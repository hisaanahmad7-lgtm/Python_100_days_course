import requests

url = "https://claude.ai/chat/3b0f7c49-0108-4c5b-9476-f58e3a254fb2"
q1 = requests.get(url)
print(q1.text)


response = requests.get("https://pypi.org/pypi/numpy/json")
data = response.json()

print("Status Code:", response.status_code)
print("Package Name:", data["info"]["name"])
print("Version:", data["info"]["version"])
print("Summary:", data["info"]["summary"])




headers = {"User-Agent": "HisaanBot/1.0"}
response = requests.get("https://pypi.org/pypi/pandas/json", headers=headers)

print("Status Code:", response.status_code)
print("Package Name:", response.json()["info"]["name"])
print("Package URL:", response.json()["info"]["package_url"])
print("Sent User-Agent:", response.request.headers["User-Agent"])




myheaders = {"User-Agent": "MyCustomBot/1.0"}
# response = requests.get("https://pypi.org/pypi/requests/json", headers=myheaders)
response = requests.get("https://pypi.org/pypi/flask/json", headers=myheaders)
    
print("Status Code:", response.status_code)
print("OK?:", response.ok)
print("Package Name:", response.json()["info"]["name"])
print("Package URL:", response.json()["info"]["package_url"])
print("Time Taken:", response.elapsed.total_seconds(), "seconds")
print("Content-Type:", response.headers["Content-Type"])


import http.client

conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {import requests

url = "https://claude.ai/chat/3b0f7c49-0108-4c5b-9476-f58e3a254fb2"
q1 = requests.get(url)
print(q1.text)


response = requests.get("https://pypi.org/pypi/numpy/json")
data = response.json()

print("Status Code:", response.status_code)
print("Package Name:", data["info"]["name"])
print("Version:", data["info"]["version"])
print("Summary:", data["info"]["summary"])




headers = {"User-Agent": "HisaanBot/1.0"}
response = requests.get("https://pypi.org/pypi/pandas/json", headers=headers)

print("Status Code:", response.status_code)
print("Package Name:", response.json()["info"]["name"])
print("Package URL:", response.json()["info"]["package_url"])
print("Sent User-Agent:", response.request.headers["User-Agent"])




myheaders = {"User-Agent": "MyCustomBot/1.0"}
# response = requests.get("https://pypi.org/pypi/requests/json", headers=myheaders)
response = requests.get("https://pypi.org/pypi/flask/json", headers=myheaders)
    
print("Status Code:", response.status_code)
print("OK?:", response.ok)
print("Package Name:", response.json()["info"]["name"])
print("Package URL:", response.json()["info"]["package_url"])
print("Time Taken:", response.elapsed.total_seconds(), "seconds")
print("Content-Type:", response.headers["Content-Type"])


import http.client

conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "014f211bafmsh50e29e0fd51c2c7p134b80jsn949ef4228303",
    'x-rapidapi-host': "meteostat.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/point/monthly?lat=52.5244&lon=13.4105&alt=43&start=2020-01-01&end=2020-12-31", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





url = "https://api.github.com/user/repos"

# Custom Headers aur Authorization Token
headers = {
    "Authorization": "Bearer YOUR_GITHUB_TOKEN_HERE",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "MyPythonApp"
}

# Optional filtering
params = {
    "visibility": "public",
    "sort": "created"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    repos = response.json()
    for repo in repos[:3]:
        print(f"Repo Name: {repo['name']} | Stars: {repo['stargazers_count']}")
else:
    print("Auth Failed or Error:", response.status_code)





    'x-rapidapi-key': "014f211bafmsh50e29e0fd51c2c7p134b80jsn949ef4228303",
    'x-rapidapi-host': "meteostat.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/point/monthly?lat=52.5244&lon=13.4105&alt=43&start=2020-01-01&end=2020-12-31", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





url = "https://api.github.com/user/repos"

# Custom Headers aur Authorization Token
headers = {
    "Authorization": "Bearer YOUR_GITHUB_TOKEN_HERE",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "MyPythonApp"
}

# Optional filtering
params = {
    "visibility": "public",
    "sort": "created"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    repos = response.json()
    for repo in repos[:3]:
        print(f"Repo Name: {repo['name']} | Stars: {repo['stargazers_count']}")
else:
    print("Auth Failed or Error:", response.status_code)




