from sieren.calculation.goupa import get_cgpa,get_sgpa
from sieren.source.helper import *
from sieren.export.runner import *

def yearly_sgpa(addmission_year,semester,sorted=True,force_full=False):
    
    file_name=file_name_creater(semester,addmission_year,sorted,category='SGPA')
    
    if alternative_flow(file_name) and not force_full: return
    roll_arr=get_roll_numbers(addmission_year,semester)
            
    frame=get_sgpa(roll_arr)  # main step....
    if frame is None: return
    
    frame=ordered_frame(frame,sorted,SGPA=True)
      
    save_file(frame,file_name)
    return frame

def yearly_cgpa(addmission_year,semester,sorted=True,force_full=False):
    
    file_name=file_name_creater(semester,addmission_year,sorted,category='CGPA')
    
    if alternative_flow(file_name) and not force_full: return
    roll_arr=get_roll_numbers(addmission_year,semester)
            
    frame=get_cgpa(roll_arr)  # main step....
    if frame is None: return
    
    frame=ordered_frame(frame,sorted,SGPA=False)
      
    save_file(frame,file_name)
    return frame