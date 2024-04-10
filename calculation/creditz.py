import sieren
from bs4 import BeautifulSoup
import requests
import roman
import re
import numpy as np

#link = https://www.ietdavv.edu.in/index.php/be-iiiyr-civ-sem-a
# https://www.ietdavv.edu.in/index.php/be-cs-iyr 
# https://www.ietdavv.edu.in/index.php/be-cs-iyr-sem-b

branchii={'C':'cs','I':'it','T':'tc','E':'ei','M':'mech','V':'civ'}

def move_number_to_beginning(string):
    # Find the index of the first occurrence of a number
    index = next((i for i, char in enumerate(string) if char.isdigit()), None)
    if index is not None:
        # Move the number to the beginning
        string = string[index] + string[:index] + string[index + 1:]
    return string


def fetch_data(roll):
    year=int((int(roll[3])+1)/2)
    year=roman.toRoman(year).lower()
    
    branch=branchii[roll[2]]
    sem='b' if int(roll[3])%2==0 else 'a'
    
    if year=='i':  
        if (branch in ['it','cs','civ'] and sem=='b') or (branch in ['tc','ei','mech'] and sem=='b'): 
            response=requests.get('https://www.ietdavv.edu.in/index.php/be-cs-iyr-sem-b')
        else :
            response=requests.get('https://www.ietdavv.edu.in/index.php/be-cs-iyr')
    elif year=='ii' and branch=='civ':
        branch='civil'
        response = requests.get(f"https://www.ietdavv.edu.in/index.php/be-{year}yr-{branch}-sem-{sem}")
    else:
        response = requests.get(f"https://www.ietdavv.edu.in/index.php/be-{year}yr-{branch}-sem-{sem}")
    
    data = BeautifulSoup(response.text, "html.parser")
    return data
    
def credit2_subject(roll):
    data=fetch_data(roll)
        
    subjects_details = data.find('table').find_all("tr")
    subject_credits={}
    svz=None
    
    for tr in subjects_details[2:]:
        subject_data=tr.find_all('td')
        if len(subject_data)<5: continue
        
        sub_code=subject_data[1].get_text(strip=True)
        if not sub_code: continue
        sub_code=move_number_to_beginning(sub_code)
        
        credit=subject_data[-2].get_text(strip=True)
        if not credit: continue
 
        if credit: 
            L,T,P = np.array(re.findall(r'\d+', credit),dtype='int')
            if(L+T+P==0): svz=(0,7)
            else : svz=(L+T,P)
        
        subject_credits[sub_code]=svz
    # if roll[2:4]=='E7': subject_credits['7EIRP1']=(0,7)
    # if roll[2:4]=='E8': subject_credits['EIR8P2']=(0,7)
    
    return subject_credits
