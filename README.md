# sieren - p_a_c_k_a_g_e
## About
 ***it is a python package***  
 created to fetch students marks with there cgpa, backs, etc. we are fetching data from iet's database to our local. we are also applying sorting to the fetched data according to the student's **sgpa** or **cgpa** this is very benifical for students because they can compare each other with the others and enhance there performance.
## installation
```powershell
pip install numpy pandas roman re requests sys time os
pip install beautifylsoup
pip install firebase_admin
```
ensure that you are haveing these libraries already installed.  
```powershell
pip install sieren
```
> [!NOTE]
> In sieren-beta version we are using `IETdavv.edu.in` to fetch the credits of subjects, it is the most time consuming process because here, *The data is very huge..*
## initializing
```python
import sieren as sr
```

## implementation
the **branchwise_sgpa** contains `addmission_year`, `branch`, `semester`,`section`, `sorted`[default=True] as arguments   
also there is `force_full` set it to **True**, if you don't want to fetch data from fire-base (it will force-fully runs the scrapping loop)
```python
sr.branchwise_sgpa(21,'it',5)
```
> [!TIP]
> * make sure you are having good network connection
> * 100kb/s can takes 10 sec to fetch 100 results  
> while 1mb/s takes 5sec.
>* also it depends on the server side.

the return type is a **pandas data frame**.  
```python
frame=sr.branchwise_sgpa(23,'electric',1,'A')
print(frame)
```
_a container folder is been created and all your fetched data and operation will be monitored over there_  
>`sem(1)_batch[23]_ETC.A_(SGPA+GRADES)_sorted.xlsx`   

*EXCEL FILE FORMATE* 
![output img](https://i.ibb.co/r5btQQY/Screenshot-2024-04-20-004101.png)


## other functions
behalf of operatoin we are haveing:-  
* **branchwise_sgpa & branchwise_cgpa**
* **yearly_sgpa & yearly_cgpa**
* **complete_branch**
* **get_sgpa & get_cgpa**  

get sgpa and cgpa can works indipendently we can just push an rollnumber array into it.
```python
frame=sieren.get_sgpa(['20C7023', '21I5023', '22T3023', '23E1023','22M3023','20V7023'])
print(frame)
```
*Output:*  
```powershell
  Enrollment  Roll.No year branch    _Name_of_Student___   SGPA Back_logs   sub1             sub2             sub3             sub4             sub5              LAB           comprihensive             sub8
                                                                          Theory Practical Theory Practical Theory Practical Theory Practical Theory Practical Theory Practical        Theory Practical Theory Practical
0    DE20115  20C7023  4ᵗʰ   CS.A           DHRUV BAKSHI   7.57         0      A        -      A+        B+     B+        A+      B        B+   None      None     -          A            -         B+   None      None
1    DE21445  21I5023  3ʳᵈ   IT.A         DIVYANSHI GARG   7.83         0     B+        -      A+        A+     B+         A      A        A+      C        -      -         A+            -         A+      O        -
2    DE22351  22T3023  2ⁿᵈ  ETC.A    GAJENDRA KUMAR AYAM   3.83         3      C        -       F         B      B        B+      F         B      F        -      -          B            -         B+     A+        -
3    DE23260  23E1023  1ˢᵗ     EI  JASKARAN SINGH KHALSA   6.63         0     B+        -       B        B+      B         A     B+         A      B         B   None      None            -          B     A+        -
4    DE22639  22M3023  2ⁿᵈ   MECH            DHAWAL MORE   7.50         0      B        -      A+         O      A        A+      P         A     B+        -      -          A            -          O     B+        -
5    DE20022  20V7023  4ᵗʰ  CIVIL        BHAVYA TRIPATHI  10.00         0      O         O      O         O      O         O      O        -    None      None     -          O            -          O   None      None
```
> [!IMPORTANT]
> currently there are a lots of data is been removed from our `results.io` **server** , because they were getting lot's of traffic in there server  
>mainly due to `get_cgpa()` , *but it will be resembeled in the future*  
> >**Result not available. For more information, Contact EDP Section**
```python
frame=sieren.get_cgpa(['20C7023', '21I5023', '22T3023', '23E1023','22M3023','20V7023'])
print(frame)
```
*Output:* 
```powershell
  Enrollment  Roll.No year branch    _Name_of_Student___   CGPA  Backs  sem-s
0    DE20115  20C7023  4ᵗʰ   CS.A           DHRUV BAKSHI   7.57      0      1
1    DE21445  21I5023  3ʳᵈ   IT.A         DIVYANSHI GARG   7.83      0      1
2    DE22351  22T3023  2ⁿᵈ  ETC.A    GAJENDRA KUMAR AYAM   3.83      3      1
3    DE23260  23E1023  1ˢᵗ     EI  JASKARAN SINGH KHALSA   6.63      0      1
4    DE22639  22M3023  2ⁿᵈ   MECH            DHAWAL MORE   7.50      0      1
5    DE20022  20V7023  4ᵗʰ  CIVIL        BHAVYA TRIPATHI  10.00      0      1
```
**The columns will be aseemble automaticaly**  
if results are of same branch then branch section will be discarded(removed) and for same year(same semester) year section removed.   


The get_sgpa and get _cgpa will not automaticaly save your file  
you can use save_file function -> just add this to your code and pass your frame and file_name to it.
```python
import os

def save_file(frame, file_name):
    file_name+='.xlsx'
    path=os.getcwd()+'\container'
    
    os.makedirs(path, exist_ok=True)
    with pd.ExcelWriter(os.path.join(path,file_name), engine='xlsxwriter') as writer:  
        frame.to_excel(writer, sheet_name='Sheet1')
    
    print('file is been saved',path,file_name,'👍')
```


### working 
here branchwise and yearly manages the students rollnumber array. 
>function in branchiole and yeariole create a array of rollnumbers  
**(21,'it',5)**=> `['21I5001',-to-,'22I5099' , '21I5101',-to-,'22I5199']`  
**(21,5)**=> chunks of roll numbers of complete year



**get_sgpa** and **get_cgpa** actualy performs the main operations of *1) fetching the data 2) making the frame*  
all other extra curriculum activitys like *1) sorting 2) file saving*   
are been done within the fuctions ~~branchwise and yearwise~~.

### Technology
> `web-scrapping` , `selenium` and `google-firebase`

> [!WARNING]
> do not excecute the program as many times (same file can be extracted multiple times). our server provides around **3000 calls per day** , so if the server got crashed, you would have to be wait for the next day.   
> *so , kindly do not exceed this limit!*

> [!CAUTION]
> if you are having that data file(excel file) already open, **just close it before 
> executing the sieren**.  otherwise it will shows an error : 
> >error : can not manupulate file while it is open
