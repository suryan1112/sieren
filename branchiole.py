from sieren.calculation.goupa import get_cgpa,get_sgpa
from sieren.source.helper import *

def branchwise_sgpa(addmission_year,branch,semester,section=None,sorted=True):
    
    branch= find_parent_branch(branch)
    if section: section=section.upper()
    if branch is None: 
        print('Branch is not correct ❌')
        return     
    file_name=file_name_creater(semester,addmission_year,sorted,branch,section,category='SGPA+MARKS')
      
    roll_arr=get_roll_numbers(addmission_year,semester,branch,section)
            
    frame=get_sgpa(roll_arr)  # main step....
    if frame is None: return
    
    ordered_frame(frame,sorted,SGPA=True)
     
    save_file(frame,file_name)
    return frame

def branchwise_cgpa(addmission_year,branch,semester,section=None,sorted=True):
    
    branch= find_parent_branch(branch)
    if section: section=section.upper()
    if branch is None: 
        print('Branch is not correct ❌')
        return     
    file_name=file_name_creater(semester,addmission_year,sorted,branch,section,category='CGPA')
      
    roll_arr=get_roll_numbers(addmission_year,semester,branch,section)
            
    frame=get_cgpa(roll_arr)  # main step....
    if frame is None: return
    
    ordered_frame(frame,sorted,SGPA=False)
     
    save_file(frame,file_name)
    return frame



def complete_branch(last_year,branch,last_year_semester,section=None,sorted=True):
    
    branch= find_parent_branch(branch)
    if section: section=section.upper()
    if branch is None: 
        print('Branch is not correct ❌')
        return     
    file_name=create_file_name(branch,sorted,section,category='SGPA+MARKS')
    
    roll_arr=[]
    for i in range(0,4): 
        roll_arr.extend(get_roll_numbers(last_year,last_year_semester,branch,section))
        last_year+=1
        last_year_semester-=2
          
    frame=get_sgpa(roll_arr)  # main step....
    if frame is None: return
    
    ordered_frame(frame,sorted,SGPA=True)
      
    save_file(frame,file_name)
    return frame