import json
from datetime import datetime, timedelta

# Define a named function to extract the count from a tuple
def get_count(item):
    return item[1]  # This function extracts the count (item[1]) from a tuple

# Opening the JSON file and reading its contents.
with open('search_keywords.json') as file:
    data = json.load(file)  # Load the JSON data from the file

details = data.get('details', [])  # Get the 'details' section from the JSON data
three_months_ago = datetime.now() - timedelta(days=90)  # Calculate the date 3 months ago

keywords_count_dict = {}  # Dictionary to store the count of keywords

# Iterate through the 'details' section of the data
for i in data['details']:
    # Iterate through the 'elements' section of each item in 'details'
    for j in i['elements']:
        date = datetime.strptime(j['date'], '%Y-%m-%d')  # Convert date string to datetime object
        if date >= three_months_ago:  # Check if the date is within the last 3 months (format: YYYY-MM-DD)
            keywords = i['searchKeyword']  # Get the search keyword
            total_count = j['count']  # Get the count of occurrences
            keywords_count_dict[keywords] = keywords_count_dict.get(keywords, 0) + total_count  # Update count in dictionary

# Sort the keywords and their counts based on the count in descending order
sorted_keywords = sorted(keywords_count_dict.items(), key=get_count, reverse=True)

# Print the top keywords and their counts in the last 3 months
print("Top keywords and their counts in the last 3 months:")
for keyword, count in sorted_keywords:
    print(f'{keyword}: {count} times')       