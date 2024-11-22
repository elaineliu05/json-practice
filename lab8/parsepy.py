#!/usr/bin/python3

import json

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
	counter = 0
	for i in data:
		if counter >=5:
			break

		name = i.get('name', '')
		html_url = i.get('html_url', '')
		updated_at = i.get('updated_at', '')
		visibility = i.get('visibility', '')

		line = f"{name}, {html_url}, {updated_at}, {visibility}\n"
		csv_file.write(line)
		
		counter = counter + 1
