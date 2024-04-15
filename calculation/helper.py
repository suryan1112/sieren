from sieren.source.soma import *
from sieren.calculation.creditz import *
from sieren.source.testa import *

def backs(marks):
    fail_count = 0
    for i in range(0, len(marks), 2): 
        if marks[i][-1]=='F' or marks[i][-2:]=='Ab':
            fail_count += 1
    return fail_count

def backs2(subjects_details):
        marks=[]
        for j in subjects_details[1:]:
            subject_data=j.find_all('td')
            marks.append(subject_data[-2].string)
        return marks.count('F')+marks.count('Ab')      
        
def creditz_creater(substring_set):
    credits={}
    print(substring_set)
    for i in substring_set:
        branch=i[0]
        if branch not in credits:
            credits[branch]={}    
        credits[branch].update(credit2_subject(f'21{i}023'))
    return credits

    
def subject_handeler(subjects_details,credits,branch):
    # print(credits)
    subjects,marks=[],[]
    creditz2=None
    Total_marks=0
    
    for j in subjects_details[1:]:
        subject_data=j.find_all('td')
        
        if move_number_to_beginning(subject_data[1].string) in credits[branch]:
            credit=credits[branch][move_number_to_beginning(subject_data[1].string)]
        else: credit=(0,7)    
        
        if 'SVR' in subject_data[1].string :
            creditz2=subject_data
            continue
        
        subjects.append((subject_data[0].string,subject_data[1].string,'Theory'))
        subjects.append((subject_data[0].string,subject_data[1].string,'Practical'))
        
        #THEORY...
        grade=grd[subject_data[-2].string]
        marks.append(superscript[grade] +'*'+superscript[credit[0]]+'  '+subject_data[-2].string)
        Total_marks+=grade*credit[0]
        
        #PRACTICAL...
        grade=grd[subject_data[-1].string]
        marks.append(superscript[grade] +'*'+superscript[credit[1]]+'  '+subject_data[-1].string)
        Total_marks+=grade*credit[1]
    
    if(creditz2):
        subject_data=creditz2
        credit=credits[branch][move_number_to_beginning(subject_data[1].string)][:]
        
        subjects.append((subject_data[0].string,subject_data[1].string,'Theory'))
        subjects.append((subject_data[0].string,subject_data[1].string,'Practical'))
        
        #THEORY...
        grade=grd[subject_data[-2].string]
        marks.append(superscript[grade] +'*'+superscript[credit[0]]+'  '+subject_data[-2].string)
        Total_marks+=grade*credit[0]
        
        #PRACTICAL...
        grade=grd[subject_data[-1].string]
        marks.append(superscript[grade] +'*'+superscript[credit[1]]+'  '+subject_data[-1].string)
        Total_marks+=grade*credit[1]
        
    return (subjects,marks,Total_marks)