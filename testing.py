import json
from datetime import datetime, timedelta

# Define a named function to extract the count from a tuple
def get_count(item):
    return item[1]

# Opening the JSON file and reading its contents.
with open('search_keywords.json') as file:
    data = json.load(file)

details = data.get('details', [])
three_months_ago = datetime.now() - timedelta(days=90)

keywords_count_dict = {}

for i in data['details']:
    for j in i['elements']:
        date = datetime.strptime(j['date'], '%Y-%m-%d')
        if date >= three_months_ago:
            keywords = i['searchKeyword']
            total_count = j['count']
            keywords_count_dict[keywords] = keywords_count_dict.get(keywords, 0) + total_count

sorted_keywords = sorted(keywords_count_dict.items(), key=get_count, reverse=True)

print("Top keywords and their counts in the last 3 months:")
for keyword, count in sorted_keywords:
    print(f'{keyword}: {count} times')
