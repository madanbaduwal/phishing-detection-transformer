import requests

url = "https://ffksfmskfjsi.com" # Replace with the URL you want to check
api_key = "Xa4TEDdRpvF91scwtEHxJum4bit1lqYN" # Replace with your PhishTank API key

# Make a request to the PhishTank API to check if the URL is a known phishing website
response = requests.get(f"https://ipqualityscore.com/api/json/url?key={api_key}&url={url}")

# Parse the JSON response
result = response.json()
print(result)

# # Check if the URL is a known phishing website
# if result['results']['in_database']:
#     print(f"{url} is a known phishing website.")
# else:
#     print(f"{url} is not a known phishing website.")

