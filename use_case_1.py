import json

# Opening the JSON file  and reading its contents.
with open('search_keywords.json', 'r') as file:
    data = json.load(file) # Loading in the json data from the file into a dictionary

all_details = data['details'] # Extracting the details from the dictionary (only the 'details' section)

# A function to get the keyword count from the details dictionary
def get_keyword_count(keyword_detials_dict):
    return keyword_detials_dict['keywordCount']

all_details.sort(key=get_keyword_count, reverse=True) # Sorting the details by keyword count in descending order

top_10_keywords = [] # A list to store the top 10 keywords

# Iterating through each keyword details dictionary in the list
for keyword in all_details:
    if len(top_10_keywords) < 10: # Checking to see if the top 10 keywords list is full
        top_10_keywords.append(keyword)  # Adding the current keyword to the list of top
    else:
        break  # If the list is full, break out of the loop so we don't add any more

# Iterating through each keyword information dictionary in the list
for keyword_info in top_10_keywords:
    # Extracting the keyword and its count from the dictionary
    keyword = keyword_info['searchKeyword']
    count = keyword_info['keywordCount']
    print(f"Keyword: {keyword}, Count: {count}")