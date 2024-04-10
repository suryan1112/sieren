from bs4 import BeautifulSoup
import requests
from source.soma import *
import roman
from calculation.helper import *


def fetching(roll,credits):
        
    subject_arr=[]
    response = requests.get("http://results.ietdavv.edu.in/DisplayStudentResult", params={"rollno": roll, "typeOfStudent": "Regular"})
    data = BeautifulSoup(response.text, "html.parser")

    if data.find("table", {"border": "1", "align": "center", "width": "80%"}) is None:
        print('    |_','user does not exist...👎')
        return
    
    personal_data = data.find("table", {"border": "1", "align": "center", "width": "80%"}).find_all("b")
    enrollment_number = personal_data[0].string
    roll_number = personal_data[1].string
    student_name = personal_data[2].string

    subjects_details = data.find_all("table", {"border": "1", "align": "center", "width": "80%"})[1].find_all("tr")
    
    (subjects,marks,Total_marks)=subject_handeler(subjects_details,credits,roll[2])
         
    subject_arr.append(subjects)
    sgpa = float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
        
    return (enrollment_number,roll_number,student_name,sgpa,marks,subject_arr,Total_marks)

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

    subjects_details = data.find_all("table", {"border": "1", "align": "center", "width": "80%"})[1].find_all("tr")

    sgpa_sum=float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
    back_sum=backs2(subjects_details)
    
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
            subjects_details = data.find_all("table", {"border": "1", "align": "center", "width": "80%"})[1].find_all("tr")
            back_sum+=backs2(subjects_details)
            sgpa_sum+= float(data.find("table", {"height": "40%"}).find_all("b")[-1].string)
        print()           
        sem_dummy-=1
        
    return (enrollment_number,roll_number,student_name,sgpa_sum,semester,data_skip,back_sum)
