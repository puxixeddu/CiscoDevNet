import requests

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDJjMGUyODE0NzEwYTIyZDFmN2UxNzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwOSJdLCJ0ZW5hbnRJZCI6IjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwMiIsImV4cCI6MTYyMjQ5NzYzNywiaWF0IjoxNjIyNDk0MDM3LCJqdGkiOiI3YzI0MzI5Ny0yMDkyLTQ0YTUtYmExMy05ZmQ4YWM4MmFmOTAiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.V7qbpHk2Lh2u68EUZLHn4ghD6KZdN9e6w4Dl13hf91s1I1aVppNnRNHO7U_v5z9WQF9movlVD8rP8lD8n5n46sQUrvPfUWFXcCorj2RaJw--hxsNV7Rlium8McMjRTN3kPYdNsvask1vJleX6ZWhRGOushnwY2L5yzIm9TCgCCxVWy0uWsOH8xto1NJmQTl-0tsbf_xilV_UNJYMCV2rVrmu8VdN_WhJ0yHbuQtKFXetsfnQd9-BK-9bmpGSIlQuuBNckn4FNig9VxFEpQHATLH8m0B__G5yURxR3savfOyv0nS07csQ3sZJBRDsmEWTb1t4DccCmPDVrYIbnxn8sg'
}

response = requests.request("GET", url, headers=headers, verify=False, data=payload)

print(response.text)

