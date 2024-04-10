# about first 10 rollnumbers must be tested before starting the loop..

from bs4 import BeautifulSoup
import requests
import sys
import time

def testing(rool_arr):
    not_found=0
    
    for roll in rool_arr:
        sys.stdout.write('\r' + 'testing....' + roll)
        
        response = requests.get("http://results.ietdavv.edu.in/DisplayStudentResult", params={"rollno": roll, "typeOfStudent": "Regular"})
        data = BeautifulSoup(response.text, "html.parser")
        
        if data.find("table", {"border": "1", "align": "center", "width": "80%"}) is None:
            not_found+=1
            if not_found>=10 or not_found>=len(rool_arr):
                print('\r'+'roll_list failed 😖')
                return True
        time.sleep(.1)    
        
    print()
    print('All tests are passed 🥳') 