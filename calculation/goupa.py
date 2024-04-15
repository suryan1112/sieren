# all joining operation of frame data and column will under goes over here....



from sieren.calculation.testing import testing
import numpy as np
import pandas as pd
from sieren.source.soma import *
from sieren.calculation.webScraping import *
        
def get_sgpa(roll_arr):
    data_list,subject_arr=[],[]
    
    if testing(roll_arr[:10]): return 
    
    same_branch=np.all([roll[2]==roll_arr[0][2] for roll in roll_arr])
    same_semester=np.all([roll[3]==roll_arr[0][3] for roll in roll_arr])

    for roll in roll_arr:
        print(roll)
        
        touple=fetching(roll) # main step...
        if touple is None: continue
        (enrollment_number,roll_number,student_name,sgpa,marks,subject_arr)=touple 
        
        class_room=f'{(branch_names[roll[2]][-1]).upper()}{"" if roll[2] in non_sectional_branch else "."+chr(int(roll[4])+65)}'
        list=[enrollment_number, roll_number,class_room, student_name, sgpa,backs(marks)]
        
        if same_branch: list.pop(2)
        data_list.append(list)    
           
    frame_columns=[ "Enrollment", "Roll.No","branch", "_Name_of_Student___", "SGPA","Back_logs"]
    if same_branch: frame_columns.pop(2)
    
    frame=pd.DataFrame(data_list,columns=frame_columns)
    frame.dropna(axis=1, how='all',inplace=True)
    return frame
  
def get_cgpa(roll_arr):
    data_list=[]
    
    if testing(roll_arr[:10]): return  
    same_branch=np.all([roll[2]==roll_arr[0][2] for roll in roll_arr])
    
    for roll in roll_arr:
        print('_______') 
        print(roll)
        
        touple=fetching2(roll) # main step...
        if touple is None: continue
        (enrollment_number,roll_number,student_name,sgpa_sum,semester,data_skip,back_sum)=touple
        
        class_room=f'{(branch_names[roll[2]][-1]).upper()}{"" if roll[2] in non_sectional_branch else "."+chr(int(roll[4])+65)}'
         
        list=[enrollment_number, roll_number,class_room, student_name, round(sgpa_sum/(semester-data_skip),2),back_sum,(semester-data_skip)]
        
        if same_branch: list.pop(2)
        data_list.append(list)
        
    data_column=[ "Enrollment", "Roll.No",'branch', "_Name_of_Student___", "CGPA",'Backs','sem-s']
    if same_branch: data_column.pop(2)
    frame=pd.DataFrame(data_list,columns=data_column)
    
    return frame
    
    
    