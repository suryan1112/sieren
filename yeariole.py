from sieren.calculation.goupa import get_cgpa,get_sgpa
from sieren.source.helper import *

def yearly_sgpa(addmission_year,semester,sorted=True):
    
    file_name=file_name_creater(semester,addmission_year,sorted,category='SGPA+GRADES')
    roll_arr=get_roll_numbers(addmission_year,semester)
            
    frame=get_sgpa(roll_arr)  # main step....
    if frame is None: return
    
    frame=ordered_frame(frame,sorted,SGPA=True)
      
    save_file(frame,file_name)
    return frame

def yearly_cgpa(addmission_year,semester,sorted=True):
    
    file_name=file_name_creater(semester,addmission_year,sorted,category='CGPA')
    roll_arr=get_roll_numbers(addmission_year,semester)
            
    frame=get_cgpa(roll_arr)  # main step....
    if frame is None: return
    
    frame=ordered_frame(frame,sorted,SGPA=False)
      
    save_file(frame,file_name)
    return frame