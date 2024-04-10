
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
       
#link = https://www.ietdavv.edu.in/index.php/be-iiiyr-civ-sem-a       #for creadits fectching

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
        
        marks.append(subject_data[-2].string)
        marks.append(subject_data[-1].string)
    
    if(creditz2):
        subject_data=creditz2
        
        subjects.append((subject_data[0].string,subject_data[1].string,'Theory'))
        subjects.append((subject_data[0].string,subject_data[1].string,'Practical'))
        
        marks.append(subject_data[-2].string)
        marks.append(subject_data[-1].string)
        
    return (subjects,marks)