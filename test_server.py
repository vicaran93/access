import requests
import sys,os



final_url = "https://sdp-lh18.herokuapp.com/connection_test.php"

content = {'test_var': 'test1'}
response = requests.post(final_url, data=content)

if response.text[0] == "S":
    print("Test connection to Heroku and S3 database working")
    # os.system('python showGreen.py')
else:
    print("Error!! No server connection")
    # os.system('python showRed.py')




print(response.status_code, response.reason)  # HTTP

