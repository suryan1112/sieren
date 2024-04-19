from sieren.source.soma import *
from sieren.source.testa import *
                                 
def backs(marks):
    fail_count = 0
    for i in range(0, len(marks), 2): 
        if marks[i]=='F' or marks[i]=='Ab':
            fail_count += 1
    return fail_count

def backs2(subjects_details):
        marks=[]
        for j in subjects_details[1:]:
            subject_data=j.find_all('td')
            marks.append(subject_data[-2].string)
        return marks.count('F')+marks.count('Ab')      


def subject_handeler(subjects_details):
    subjects,marks=[],[]
    creditz2=None
    for j in subjects_details[1:]:
        subject_data=j.find_all('td')
        
        if 'SVR' in subject_data[1].string :
            creditz2=subject_data
            continue
        
        subjects.append((subject_data[0].string,subject_data[1].string,'Theory'))
        subjects.append((subject_data[0].string,subject_data[1].string,'Practical'))
        
        G1=subject_data[-2].string
        G2=subject_data[-1].string
        
        marks.append(G1 if G1 else 'F')  #THEORY...
        marks.append(G2 if G2 else 'F')  #PRACTICAL...
    
    if(creditz2):
        subject_data=creditz2
        
        subjects.append((subject_data[0].string,subject_data[1].string,'Theory'))
        subjects.append((subject_data[0].string,subject_data[1].string,'Practical'))
        
        G1=subject_data[-2].string
        G2=subject_data[-1].string
        
        marks.append(G1 if G1 else 'F')  #THEORY...
        marks.append(G2 if G2 else 'F')  #PRACTICAL...
        
    return (subjects,marks)