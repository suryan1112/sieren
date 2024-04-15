from sieren.source.soma import *
from sieren.source.testa import *
from sieren.calculation.goupa import get_cgpa,get_sgpa
from branchiole import branchwise_sgpa,branchwise_cgpa,complete_branch
from yeariole import yearly_cgpa,yearly_sgpa

df=get_sgpa(['21I5054'])
print(df)