import requests
from requests.auth import HTTPBasicAuth

# Here I'm defining the URL with the standard placeholders VendorID and addonKey
url = "https://marketplace.atlassian.com/rest/2/vendors/{vendorId}/addons/{addonKey}/reporting/search-keywords"

vendor_id = "1223970"
addon_key = "onramp-employee-onboarding-and-offboarding"

url = url.format(vendorId=vendor_id, addonKey=addon_key)

# Authentication credentials
email = "rmathur200410@gmail.com"
api_token = "ATATT3xFfGF0tqlecmN9xASI0wUgacv-yJevnmzdKN4GPtaQRvJQzWpG1HOZl7o0XLfTyeWzlBjwnkldydM3EMj4chpEz8LwY7UUfRGMbSVnkFm6b-dp_dDvOPzHD3_mCeBlnRXfFgQSA6QL9bDvSb0cvgRQNpb5cdO9GzIM-Fk0Eiv7Ds-AAGE=BF604DF9"

auth = HTTPBasicAuth(email, api_token)


# Making a GET request to the URL
response = requests.get(url, auth=auth)

# Checking to see if the requests were successful (sucess = status code of 200)
if response.status_code == 200:
    data = response.json() # Extract the JSON data from the response

    # Getting the top 10 keywords from the data
    top_keywords = []
    for word in range(10):
        top_keywords.append(data["top_keywords"][word])

        print("The top 10 keywords: ")
        for keyword in top_keywords:
            print(keyword)
else:
    print("Failed to fetch the data. Status code: ", response.status_code)