import requests
import sys,os,time
from datetime import datetime,timedelta



final_url = "https://sdp-lh18.herokuapp.com/connection_test.php"

content = {'test_var': 'test1'}
t1 = datetime.now()
response = requests.post(final_url, data=content)
t2 = datetime.now()
delta = t2 - t1 # 10 seconds of showing Red or Green LEDs
if response.text[0] == "S":
    print("Connection to Heroku and S3 database working. Response is:")
    print(response.text)
    #print(delta)

    timestamp = int(delta.total_seconds())
    print("Duration:"+str(timestamp))
    if timestamp < 15:
        print("Connection done in less than 15s")
        #os.system('python showGreen.py')
else:
    print("Error!! No server connection")
    #os.system('python showRed.py')




print(response.status_code, response.reason)  # HTTP

