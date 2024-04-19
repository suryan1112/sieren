from bs4 import BeautifulSoup
import requests
from sieren.source.soma import *
import roman
 
def fetching(roll):
    
    response = requests.get("http://results.ietdavv.edu.in/DisplayStudentResult", params={"rollno": roll, "typeOfStudent": "Regular"})
    data = BeautifulSoup(response.text, "html.parser")

    if data.find("table", {"border": "1", "align": "center", "width": "80%"}) is None:
        print('    |_','user does not exist...👎')
        return
    
    personal_data = data.find("table", {"border": "1", "align": "center", "width": "80%"}).find_all("b")
    enrollment_number = personal_data[0].string
    roll_number = personal_data[1].string
    student_name = personal_data[2].string
    
    sgpa = float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
        
    return (enrollment_number,roll_number,student_name,sgpa)

def fetching2(roll):
    semester=int(roll[3])
    response = requests.get("http://results.ietdavv.edu.in/DisplayStudentResult", params={"rollno": roll, "typeOfStudent": "Regular"})
    data = BeautifulSoup(response.text, "html.parser")

    if data.find("table", {"border": "1", "align": "center", "width": "80%"}) is None:
        print('    |_','user does not exist...👎')
        return

    personal_data = data.find("table", {"border": "1", "align": "center", "width": "80%"}).find_all("b")
    enrollment_number = personal_data[0].string
    roll_number = personal_data[1].string
    student_name = personal_data[2].string

    sgpa_sum=float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
    
    data_skip=0
    sem_dummy=semester-1  
    while sem_dummy>0:
        roll_dummy= roll[:3]+str(sem_dummy)+roll[4:]
        print(f'sem-{roman.toRoman(sem_dummy)}:({roll_dummy})',end='')
        response = requests.get("http://results.ietdavv.edu.in/DisplayStudentResult", params={"rollno": roll_dummy, "typeOfStudent": "Regular"})
        data = BeautifulSoup(response.text, "html.parser")
        
        if data.find("table", {"height": "40%"}) is None:
            print('-->','data is unavailable on server 🤷',end='')
            data_skip+=1
        else:
            sgpa_sum+= float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
        print()           
        sem_dummy-=1
        
    return (enrollment_number,roll_number,student_name,sgpa_sum,semester,data_skip)
