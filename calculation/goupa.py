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
        year= years_available[(int(roll[3])+1)//2-1]
        
        list=[enrollment_number, roll_number,year,class_room, student_name, sgpa,backs(marks)]
        
        if same_branch: list.pop(3)
        if same_semester: list.pop(2)
    
        if len(marks)>=8*2 or (same_branch and same_semester): 
            data_list.append([*list,*marks])
            
        elif len(marks) == 7 * 2:
            data_list.append([*list,*marks[:4],*marks[6:12] #comprehensive abstracted
                              ,None,None
                              ,marks[4],marks[5],  #comprehensive
                              *marks[12:]
                              ])
            subject_arr=[*subject_arr[:10],None,None,*subject_arr[12:14],*subject_arr[10:12]]
        else: 
            data_list.append([*list,*marks[:8],
                              None,None,*marks[8:12],
                              (marks[-2] if len(marks)>=14 else None),
                              (marks[-1] if len(marks)>=14 else None)
                              ])
       
    if same_branch and same_semester:
        print('branches and semester are all same 👌')
        frame_columns = [("Enrollment", '', ''), ("Roll.No", '', ''), ("_Name_of_Student___", '', ''), ("SGPA", '', ''), ("Back_logs", '', ''),*subject_arr[0]]
        
    else: 
        print('branches are not same 🙌')        
        frame_columns=[ ("Enrollment",''), ("Roll.No",''),('year',''),("branch",''), ("_Name_of_Student___",''), ("SGPA",''),("Back_logs",''),*sub1]
  
        if same_branch: frame_columns.pop(3)
        if same_semester: frame_columns.pop(2)
   
    frame=pd.DataFrame(data_list,columns=pd.MultiIndex.from_tuples(frame_columns))
    frame.dropna(axis=1, how='all',inplace=True)
    return frame
  
def get_cgpa(roll_arr):
    data_list=[]
    
    if testing(roll_arr[:10]): return  
    same_branch=np.all([roll[2]==roll_arr[0][2] for roll in roll_arr])
    same_semester=np.all([roll[3]==roll_arr[0][3] for roll in roll_arr])
    
    for roll in roll_arr:
        print('_______') 
        print(roll)
         
        touple=fetching2(roll) # main step...
        if touple is None: continue
        (enrollment_number,roll_number,student_name,sgpa_sum,semester,data_skip,back_sum)=touple
        
        class_room=f'{(branch_names[roll[2]][-1]).upper()}{"" if roll[2] in non_sectional_branch else "."+chr(int(roll[4])+65)}'
        year= years_available[(int(roll[3])+1)//2-1]
          
        list=[enrollment_number, roll_number,year,class_room, student_name, round(sgpa_sum/(semester-data_skip),2),back_sum,(semester-data_skip)]
        
        if same_branch: list.pop(3)
        if same_semester: list.pop(2)
        
        data_list.append(list)
    
    data_column=[ "Enrollment", "Roll.No",'year','branch', "_Name_of_Student___", "CGPA",'Backs','sem-s']
    
    if same_branch: data_column.pop(3)
    if same_semester: data_column.pop(2)
    
    frame=pd.DataFrame(data_list,columns=data_column)
    
    return frame
    
    
    