import requests
import sys

requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

headers = {'Content-Type': 'application/yang-data+json',
             'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=(USER, PASS),
                          headers=headers, verify=False)


print(response.text)
