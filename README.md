# sieren & goupa_corporations
## About
 ***this is a python package***  
 created to fetch students marks with there cgpa, backs, etc. we are fetching data from iet's database to our local. we are also applying sorting to the fetched data according to the student's **sgpa** or **cgpa** this is very benifical for students because they can compare each other with the others and enhance there performance.
## installation
```powershell
pip install sieren
```
> [!NOTE]
> In sieren-beta version we are using `IETdavv.edu.in` to fetch the credits of subjects, it is the most time consuming process because here, *The data is very huge..*
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
frame=sieren.branchwise_sgpa(23,'civil',1)
print(frame)
```
_a container folder is been created and all your fetched data and operation will be monitored over there_  
*EXCEL FILE FORMATE* 
![output img](https://i.ibb.co/5K37fvW/Screenshot-2024-04-19-121316.png)

> [!IMPORTANT]
> currently there are a lots of data is been removed from our `results.io` **server** , because they were getting lot's of traffic in there server  
>mainly due to `get_cgpa()` , *but it will be resembeled in the future*  
> >**Result not available. For more information, Contact EDP Section**

## other functions
behalf of operatoin we are haveing:-  
* **branchwise_sgpa & branchwise_cgpa**
* **yearly_sgpa & yearly_cgpa**
* **complete_branch**
* **get_sgpa & get_cgpa**  

get sgpa and cgpa can works indipendently we can just push an rollnumber array into it.
```python
frame=sieren.get_sgpa(['21I5064','21I5062','22T3023','23C5063'])
print(frame)
```
*Output:*  
```powershell
  Enrollment  Roll.No branch  _Name_of_Student___  SGPA Marks Back_logs     sub1               sub2               sub3               sub4                sub5                 LAB           comprihensive               sub8
                                                                          Theory Practical   Theory Practical   Theory Practical   Theory Practical    Theory Practical    Theory Practical        Theory Practical   Theory Practical    
0    DE21525  21I5064   IT.A         SURYAN GUPTA  7.87   236         0  ¹⁰*⁴  O  ⁰*⁰   -    ⁸*⁴  A    ⁸*¹  A  ⁷*⁴  B+    ⁸*¹  A  ⁷*⁴  B+    ⁸*¹  A   ⁷*⁴  B+  ⁰*⁰   -   ⁰*⁰   -    ¹⁰*¹  O      ⁰*⁰   -    ⁷*⁴  B+  ⁹*²  A+  ⁰*⁰   -     
1    DE21521  21I5062   IT.A            SOMI GOUR  9.23   277         0  ¹⁰*⁴  O  ⁰*⁰   -   ¹⁰*⁴  O   ⁹*¹  A+  ⁹*⁴  A+   ¹⁰*¹  O  ⁹*⁴  A+   ⁹*¹  A+   ⁷*⁴  B+  ⁰*⁰   -   ⁰*⁰   -    ⁹*¹  A+      ⁰*⁰   -    ¹⁰*⁴  O  ¹⁰*²  O  ⁰*⁰   -     
2    DE22351  22T3023  ETC.A  GAJENDRA KUMAR AYAM  3.83   115         3   ⁵*⁴  C  ⁰*⁰   -    ⁰*⁴  F    ⁶*¹  B   ⁶*⁴  B   ⁷*¹  B+   ⁰*⁴  F    ⁶*¹  B    ⁰*⁴  F  ⁰*⁰   -   ⁰*⁰   -     ⁶*¹  B      ⁰*⁰   -    ⁷*⁴  B+  ⁹*²  A+  ⁰*⁰   -     
3    DE23206  23C1063   CS.A      SHIVANSHU KHODE  5.53   157         0   ⁵*⁴  C   ⁹*¹  A+   ⁴*⁴  P  ⁰*⁰   -    ⁴*⁴  P    ⁶*¹  B   ⁴*⁴  P    ⁸*¹  A  ⁰*¹   -    ⁹*²  A+      None      None      ⁰*⁰   -     ⁶*⁴  B   ⁶*⁴  B  ⁰*⁰   -  
```

```python
frame=sieren.get_cgpa(['21I5064','21I5062','22T3023','23C5063'])
print(frame)
```
*Output:* 
```powershell
  Enrollment  Roll.No branch  _Name_of_Student___  CGPA  Backs  sem-s
0    DE21525  21I5064   IT.A         SURYAN GUPTA  7.87      0      1
1    DE21521  21I5062   IT.A            SOMI GOUR  9.23      0      1
2    DE22351  22T3023  ETC.A  GAJENDRA KUMAR AYAM  3.83      3      1
3    DE23206  23C1063   CS.A      SHIVANSHU KHODE  5.53      0      1
```
    
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
here branchwise and yearly manages the students rollnumber array and get_sgpa and get_cgpa actualy performs the main operations of *1) fetching the data 2) making the frame*

### Technology
> `web-scrapping` and `selenium`

> [!WARNING]
> do not excecute the program as many times. our server provides around **1000 calls per day** , so if the server got crashed, you would have to be wait for the next day.   
> *so , kindly do not exceed this limit!*

> [!CAUTION]
> if you are having that data file(excel file) already open, **just close it before 
> executing the sieren**.  otherwise it will shows an error : 
> >error : can not manupulate file while it is open
