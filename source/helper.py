from sieren.source.soma import *
import os
import pandas as pd
from sieren.export.runner import file_uploading

def find_parent_branch(branch):
    for parent, child_names in branch_names.items():
        if any(branch.lower() in child.lower() for child in child_names):
            return parent
    return None

def get_roll_numbers(addmission_year,semester,branch=None,section=None):
    roll_arr=[]
    sectionsi=sections
    if branch:    
        sectionsi={branch:(section if section else sectionsi[branch])}
    
    for branch,sectioni in sectionsi.items():
        for section in sectioni:
            for i in range(1,100):
                if i==90: addmission_year+=1
                roll_arr.append(f"{addmission_year}{branch}{semester}{ord(section)-65}{i:02d}")
            addmission_year-=1
    return roll_arr   

def ordered_frame(frame,sorted,SGPA):
    frame.index.name='s.no'
    if sorted: 
        frame.sort_values(by=("SGPA" if SGPA else "CGPA"), ascending=False, inplace=True)
        frame.reset_index(drop=True,inplace=True)
        frame.index.name='rank'
    frame.index+=1 
    return frame


def file_name_creater(semester, admission_year, sorted, branch=None, section=None, category=None):
    
    branch_suffix = f'_{branch_names[branch][-1].upper()}' if branch else ''
    section_suffix = f'.{section}' if section else f'.{sections[branch]}' if branch and len(sections.get(branch, '')) > 1 else ''
    
    file_name = (f'sem({semester})'
                 f'_batch[{admission_year}]'
                 f'{branch_suffix}'
                 f'{section_suffix}'
                 f'_({category.upper()})'
                 f'{"_sorted" if sorted else ""}')
    
    return file_name+'.xlsx'

def save_file(frame, file_name):
   
    path=os.getcwd()+'\container'
    
    os.makedirs(path, exist_ok=True)
    with pd.ExcelWriter(os.path.join(path,file_name), engine='xlsxwriter') as writer:  
        frame.to_excel(writer, sheet_name='Sheet1')
        
    file_path=os.path.join(path,file_name)    
    file_uploading(file_path)
    print('file is been saved',file_path,'👍')
    

def create_file_name(branch,sorted,section=None,category=None):
    
    branch_suffix = f'_{branch_names[branch][-1].upper()}' if branch else ''
    section_suffix = f'.{section}' if section else f'.{sections[branch]}' if branch and len(sections.get(branch, '')) > 1 else ''
    
    file_name = ('All'
                 f'{branch_suffix}'
                 f'{section_suffix}'
                 f'_({category.upper()})'
                 f'{"_sorted" if sorted else ""}')
    
    return file_name+'.xlsx'    

    

