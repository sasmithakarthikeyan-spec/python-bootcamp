#install api
'''import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

if response.status_code == 200:
    post = response.json()

    print("Post ID:", post["id"])
    print("User ID:", post["userId"])
    print("Title:", post["title"])
    print("Body:", post["body"])
else:
    print("Request failed!")
    print("Status code:", response.status_code)'''

#API error

'''import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    post = response.json()

    print("Post ID:", post["id"])
    print("Title:", post["title"])

except requests.exceptions.Timeout:
    print("The request took too long!")

except requests.exceptions.ConnectionError:
    print("Could not connect to the server!")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)'''

#authentication
'''import requests

url = "https://example.com/api/data"

api_key = "your_api_key_here"

headers = {
    "X-API-Key": api_key
}

print("Request URL:", url)
print("Authentication header configured:", "X-API-Key" in headers)'''


#bearer token
import requests

url = "https://example.com/api/data"

token = "your_token_here"

headers = {
    "Authorization": f"Bearer {token}"
}

print("Authorization header configured:",
      headers["Authorization"].startswith("Bearer "))

print("Token authentication is ready!")

