# sieren & goupa_collaborations
### About
 this is a python package  
 created to fetch students marks with there cgpa, backs, etc. we are fetching data from iet's database to our local. we are also applying sorting to the fetched data according to the student's **sgpa** or **cgpa** this is very benifical for students because they can compare each other with the others and enhance there performance.
## installation
```bash
pip install sieren
```
> [!NOTE]
> In sieren-beta version we are using `IETdavv.edu.in` to fetch the credits of subjects, it is the most time consuming process because here is the data very huge..
## initializing
```python
import sieren
```

## implementation
the **branchwise_sgpa** contains `addmission_year`, `branch`, `semester`,`section`, `sorted`[default=True] as arguments
```python
sieren.branchwise_sgpa(21,'it',5)
```
> [!TIP]
> * make sure you are having good network connection
> * 100kb/s can takes 10 sec to fetch 100 results  
> while 1mb/s takes 5sec.
>* also it depends on the server side.

the return type is a **pandas data frame**.  
```python
frame=sieren.branchwise_sgpa(21,'it',5,)
print(frame)
```
_a container folder is been created and all your fetched data and operation will be monitored over there_


> [!IMPORTANT]
> currently there are a lots of data is been removed from our `results.io` **server** , because they were getting lot's of traffic in there server  
>mainly due to `get_cgpa()` , *but it will be resembeled in the future*  
> >we will be colaborating soon

## other functions
behalf of operatoin we are haveing:-  
* **branchwise_sgpa & branchwise_cgpa**
* **yearly_sgpa & yearly_cgpa**
* **complete_branch**
* **get_sgpa & get_cgpa**  

get sgpa and cgpa can works indipendently we can just push an rollnumber array into it.
### working 
here branchwise and yearly manages the students rollnumber array and get_sgpa and get_cgpa actualy performs the main operations of *1) fetching thedata 2) making the frame*

### Technology
> `web-scrapping` and `selenium`

> [!WARNING]
> do not excecute the program as many times. our server provides around **1000 calls per day** , so if the server got crashed, you would have to be wait for the next day.   
> *so , kindly do not exceed this limit!*

> [!CAUTION]
> if you are having that data file(excel file) already open, **just close it before 
> executing the sieren**.  otherwise it will shows an error : 
> >cannot change the opend file.
