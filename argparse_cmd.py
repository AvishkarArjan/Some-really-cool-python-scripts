# pip install argparse
import argparse
import requests
import json
from pprint import pprint


parser = argparse.ArgumentParser(description = '[*]This tool uses the randomuser.me api to display a specified number of random user names, either the first name or the full name, along with the title')
parser.add_argument('no_of_users',metavar='<no_of_users>',type=str, help=":Enter no of users")
parser.add_argument('first_or_full', metavar='<first_or_full>', type=str, help=":First name of Full name")
args = parser.parse_args()

no_of_users = args.no_of_users
first_or_full = args.first_or_full


url ="https://randomuser.me/api/?results="+no_of_users

r = requests.get(url)
data = json.loads(r.text)
# pprint(data['results'])

if(first_or_full == 'first'):
	for record in data['results']:
		print(record['name']['title'] +" "+ record['name']['first'])
elif (first_or_full == 'full'):
	for record in data['results']:
		print(record['name']['title'] +" "+ record['name']['first']+" "+ record['name']['last'])
else:
	print()
	print('use either first or full / make sure the order is <no_of_users> <first_or_full>')