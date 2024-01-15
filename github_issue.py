import requests

token = '' #Insert your Personal Access Token

url = 'https://api.github.com/repos/elbekirkrasniqi/api-test/issues'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

payload = {
            "title": "test",
            "body": "test"
        }


response = requests.post(url=url, headers=headers, json=payload)
print(response.text)
print(response)