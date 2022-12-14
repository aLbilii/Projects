
#               ____ ____ ____  _____   ____  ____      _  _____ ___ ____    _    _     
#              / ___| __ ) ___|| ____| |  _ \|  _ \    / \|_   _|_ _/ ___|  / \  | |    
#             | |   |  _ \___ \|  _|   | |_) | |_) |  / _ \ | |  | | |     / _ \ | |    
#             | |___| |_) |__) | |___  |  __/|  _ <  / ___ \| |  | | |___ / ___ \| |___ 
#              \____|____/____/|_____| |_|   |_| \_\/_/   \_\_| |___\____/_/   \_\_____|
                                                                             



# 1 - Program to calculate factorial of entered number
'''
num = int(input("Enter any number :"))
f = 1
n = num                           
while num>1:                      
    f = f * num
    num-=1
print("Factorial of ", n , " is :",f)
'''
# 2 - Program to input any number from use and check if it is Prime number of not 
'''
num = int(input("Enter the number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
'''

# 3 - Program to search any word in given string/sentence
'''
def countWord(sent,word):
    s = sent.split()
    count=0
    for w in s:
        if w==word:
            count+=1
    return count
sent = input("Enter any sentence :")
word = input("Enter word to search in sentence :")
count = countWord(sent,word)
if count==0:
    print(word," not found")
else:
    print(word," occurs ",count," times")
'''

# 4 - Program to Bubble Sort using a user-defined function.
'''
def BubbleSort():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

print(BubbleSort())
'''
 
# 5 - Program to read and display file content line by line with each word separated by “#”
'''
f =open('txt1.txt') 
item=[] 
for line in f: 
    words=line.split() 
    for i in words:  
        print(i+'#', end='')
    print()
'''

# 6 - Program to read the content of file and display the total number of consonants, uppercase, vowels and lower case characters.
'''
f = open("txt2.txt")
v=0
c=0
u=0
l=0
o=0
data = f.read()
vowels=['a','e','i','o','u']

for ch in data:
    if ch.isalpha():
        if ch.lower() in vowels:
            v+=1
        else:
            c+=1
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
    elif ch!=' ' and ch!='\n':
        o+=1
print("Total Vowels in file             :",v)
print("Total Consonants in file n       :",c)
print("Total Capital letters in file    :",u)
print("Total Small letters in file      :",l)
print("Total Other than letters         :",o)
f.close()
'''

# 7 - Program to create binary file to store Rollno and Name, Search any Rollno and display name if Rollno found otherwise “Rollno not found”

'''
import pickle
student=[]
f=open('FILE1.dat','wb')
print("-----ENTER DETAILS-----")
while True:
    roll = int(input("Enter Roll Number :"))
    name = input("Enter Name :")
    student.append([roll,name])
    ans=input("Add More ?(Y)")
    if ans.lower()!='y':
        break
pickle.dump(student,f) 
f.close()

print("-----SEARCH DETAILS-----")
f=open('FILE1.dat','rb')
student=[]
while True:
    try:
        student = pickle.load(f)
    except EOFError:
        break

while True:
    found=False
    r = int(input("Enter Roll number to search :"))
    for s in student:
        if s[0]==r:
            print("Name is :",s[1])
            found=True
            break
    if not found:
        print("Roll number not found")
    ans=input("Wish to continue? (Y): ")
    if ans.lower()!='y':
        break
f.close()
print("Thank you!")
'''

# 8 - Program to create binary file to store Rollno,Name and Marks and update marks of entered Rollno
'''
import pickle 
student=[] 
f=open('FILE2.dat','wb')
print("-----  Enter Details -----")
while True:
    roll = int(input("Enter Roll Number :"))
    name = input("Enter Name :") 
    marks = int(input("Enter Marks :"))
    student.append([roll,name,marks]) 
    ans=input("Add More ? (Y)")
    if ans.lower()!='y':
        break
pickle.dump(student,f)
f.close()

f=open('FILE2.dat','rb+')
student=[]
while True:
    try:
        student = pickle.load(f)
    except EOFError:
        break
print("-----  Update Details -----")
while True:
    found=False
    r = int(input("Enter Roll number to update :"))
    for s in student:
        if s[0]==r:
            print("Name: ",s[1])
            print("Current Marks: ",s[2])
            m = int(input("Enter new marks: "))
            s[2]=m
            print("Record Updated")
            found=True 
            break
    if not found:
        print("Roll number not found")
    ans=input("Wish to continue? (Y): ")
    if ans.lower()!='y':
        break
    f.close()
'''

# 9 - Program to read the content of file line by line and write it to another file except for  the lines contains "a" letter in it.
'''
f1 = open("txt3.txt")
f2 = open("txt3copy.txt","w")

for line in f1:
    if 'a' not in line:
        f2.write(line)
print("File Copied Successfully!")
f1.close()
f2.close()
'''

# 10 - Program to create CSV file and store empno, name, salary and search any empno and display name, salary and if not found appropriate message.
'''
import csv
with open('csv1.csv',mode='a') as csvfile:
    mywriter = csv.writer(csvfile,delimiter=',')
    print("-----Enter Details-----")
    while True:
        eno=int(input("Enter Employee Number "))
        name=input("Enter Employee Name ")
        salary=int(input("Enter Employee Salary :"))
        mywriter.writerow([eno,name,salary])
        print(" Data Saved...")
        ans=input("\nAdd More: ")
        if ans.lower()!='y':
            break
    
with open('csv1.csv',mode='r') as csvfile:
    myreader = csv.reader(csvfile,delimiter=',')
    print("----- Search Details -----")
    while True:
        found=False
        e = int(input("\nEnter Employee Number to search :"))
        for row in myreader:
            if len(row)!=0:
                if int(row[0])==e:
                    print("============================") 
                    print("NAME	:",row[1])
                    print("SALARY :",row[2])
                    found=True
                    break

        if not found:
            print("==========================\nEMPNO NOT FOUND\n==========================") 
            ans = input("Search More ? (Y)")
            if ans.lower()!='y':
                break
'''

# 11 - Program to generate random number 1-6, simulating a dice
'''
import random
import time
print("Press CTRL+C to stop the dice ")
while True:
    try:
        while True:
            for i in range(10):
                print()
            n = random.randint(1,6)
            print(n,end='')
            time.sleep(.00001)
    except KeyboardInterrupt: 
            print("Your Number is :",n)
            ans=input("Play More? (Y) :")
            if ans.lower()!='y':
                break
'''

# 12 - Program to implement Stack in Python using List
'''
def isEmpty(S):
    if len(S)==0:
        return True
    else:
        return False
 

def Push(S,item):
    S.append(item)
    top=len(S)-1


def Pop(S):
    if isEmpty(S):
        return "Underflow"
    else:
        val = S.pop()
        if len(S)==0:
            top=None
        else:
            top=len(S)-1
        return val


def Peek(S):
    if isEmpty(S):
        return "Underflow"
    else:
        top=len(S)-1
        return S[top]
 

def Show(S):
    if isEmpty(S):
        print("Sorry No items in Stack ")
    else:
        t = len(S)-1
        print("Stack (Top)")
        while(t>=0):
            print(S[t])
            t-=1
        print()
 
S=[]
top=None
print("""**** STACK DEMONSTRATION ******
1. PUSH 
2. POP
3. PEEK
4. SHOW STACK 
0. EXIT""")

while True:
    ch = int(input("\nEnter your choice :"))
    if ch==1:
        val = int(input("Enter Item to Push :"))
        Push(S,val)
    elif ch==2:
        val = Pop(S)
        if val=="Underflow":
            print("Stack is Empty")
        else:
            print("\nDeleted Item was :",val)
    elif ch==3:
        val = Peek(S)
        if val=="Underflow":
            print("Stack Empty")
        else:
            print("Top item:",val)
    elif ch==4:
        Show(S)
    elif ch==0:
        print("Bye")
        break
'''


# 13 - Program to implement Queue in Python using List
'''
def LinearSearch():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    c = eval(input("Enter element to search : "))
    for i in range(len(L)):
        if L[i] == c:
            print("Element found at index", i)
            break
    else:
        print("Element not found")

def BinarySearch():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    c = eval(input("Enter element to search : "))
    L.sort()
    low = found = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == c:
            found = 1
            break
        elif L[mid] > c:
            high = mid - 1
        else:
            low = mid + 1
    if found == 1:
        print("Element found")
    else:
        print("Element not found")

LinearSearch()
BinarySearch()
'''

# 14 - Program to take 10 sample phishing email, and find the most common word occurring
'''
fakemails=[
    "jackpotwin@lottery.com",
    "claimtheprize@mylife.com",
    "youarethewinner@lottery.com",
    "luckywinner@mylife.com",
    "spinthewheel@flipkart.com",
    "dealwinner@snapdeal.com"
    "luckywinner@snapdeal.com"
    "luckyjackpot@americanlottery.com"
    "claimtheprize@lootolottery.com"
    "youarelucky@mylife.com"
    ]
myd={}
for e in fakemails:
    x=e.split('@')
    for w in x:
        if w not in myd:
            myd[w]=1
        else:
            myd[w]+=1
key_max = max(myd,key=myd.get)
print("Most Common Occuring word :",key_max)
'''

# 15 - : Program to connect with database and store record of employee and display records.
'''
import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',password="root")
cur = con.cursor()
cur.execute("create database  if not exists company")
cur.execute("use company")
cur.execute("create table if not exists employee(empno int, name varchar(20), dept varchar(20),salary int)")
con.commit()

while True:
    print(""" \n~~~ MENU ~~~
1. ADD RECORD
2. DISPLAY RECORD
0. EXIT""")
    choice = int(input("Enter Choice :"))
    
    if choice == 1:
        e = int(input("Enter Employee Number :"))
        n = input("Enter Name :")
        d = input("Enter Department :")
        s = int(input("Enter Salary :"))
        query="insert into employee values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(query)
        con.commit()
        print("Details Saved")
        
    elif choice == 2:
        query="select * from employee"
        cur.execute(query)
        result = cur.fetchall()
        print("%10s"%"EMPNO","%20s"%"NAME","%15s"%"DEPARTMENT", "%10s"%"SALARY")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%15s"%row[2],"%10s"%row[3])
    elif choice==0:
        con.close()
        print("Thank you")
        break
    else:
        print("INCORRECT OPTION!!")
'''

# 16 - Program to connect with database and search employee number in table employee and display record, if empno not found display appropriate message.
'''
import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',password="root", database="company")
cur = con.cursor()
print("------------------------")
print("EMPLOYEE SEARCHING FORM")
print("------------------------")

while True:
    eno = int(input("\nENTER EMPNO TO SEARCH :"))
    query="select * from employee where empno={}".format(eno)
    cur.execute(query)
    result = cur.fetchall()
    if cur.rowcount==0:
        print("Sorry! Empno not found ")
    else:
        print("%10s"%"EMPNO", "%20s"%"NAME","%15s"%"DEPARTMENT", "%10s"%"SALARY")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%15s"%row[2],"%10s"%row[3])
        ans=input("SEARCH MORE (Y) :")
        if ans.lower()!='y':
            break
print("Thank you!!")
'''

# 17 - Program to connect with database and update the employee record of entered empno
'''
import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',password="root",database="company")
cur = con.cursor()
print("-----------------------")
print("EMPLOYEE UPDATION FORM")
print("-----------------------")

while True:
    eno = int(input("\nENTER EMPNO TO UPDATE :"))
    query="select * from employee where empno={}".format(eno)
    cur.execute(query)
    result = cur.fetchall()
    if cur.rowcount==0:
        print("Sorry! Empno not found ")
    else:
        print("%10s"%"EMPNO","%20s"%"NAME", "%15s"%"DEPARTMENT", "%10s"%"SALARY")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%15s"%row[2],"%10s"%row[3])
            choice=input("\n## ARE YOUR SURE TO UPDATE ? (Y) :")
            if choice.lower()=='y':
                print("== YOU CAN UPDATE ONLY DEPT AND SALARY ==")
                print("== FOR EMPNO AND NAME CONTACT ADMIN ==")
                d = input("ENTER NEW DEPARTMENT,(LEAVE BLANK IF NOT WANT TO CHANGE )")
                if d=="":
                    d=row[2]
                try:
                    s = int(input("ENTER NEW SALARY,(LEAVE BLANK IF NOT WANT TO CHANGE"))
                except:
                    s=row[3]
            else:
                continue
        query="update employee set dept='{}',salary={} where empno={}".format(d,s,eno)
        cur.execute(query)
        con.commit()
        print("## RECORD UPDATED ## ")
        ans=input("UPDATE MORE (Y) : ")
        if ans.lower()!='y':
            break
'''

# 18 - Program to connect with database and delete the record of entered employee number
'''
import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',password="root",database="company")
cur = con.cursor()
print("-----------------------\nEMPLOYEE UPDATION FORM\n-----------------------")

while True:
    eno = int(input("ENTER EMPNO TO DELETE :"))
    query="select * from employee where empno={}".format(eno)
    cur.execute(query)
    result = cur.fetchall()
    if cur.rowcount==0:
        print("Sorry! Empno not found ")
    else:
        print("%10s"%"EMPNO","%20s"%"NAME", "%15s"%"DEPARTMENT", "%10s"%"SALARY")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%15s"%row[2],"%10s"%row[3])
            choice=input("\n## ARE YOUR SURE TO DELETE ? (Y) :")
            if choice.lower()=='y':
                query="delete from employee where empno={}".format(eno)
                cur.execute(query)
                con.commit()
        print("=== RECORD DELETED SUCCESSFULLY! ===")
        ans=input("DELETE MORE ? (Y) :")
        if ans.lower()!='y':
            break
'''

# 19 - Write a method CREATE() to create an EMP.csv file with the following details:
#         Emp_no to store employee number of integer type,
#         Emp_name to store employee name of string type,
#         Emp_dep to store their respective department of string type,
#         Emp_basic to store basic salary of respective employee,
#         Emp_hra to be calculated from his/her basic salary which is 10% of basic 
#         Emp_sal to be calculated as salary = basic_salary + hra
'''
import csv
def CREATE():
    f=open("Emp.csv","a",newline="")      
    obj=csv.writer(f)
    L=[]
    print("---Enter Details---")
    while True:
        print()
        emp_no    = input("Enter employee number:")
        emp_name  = input("Enter employee name:")
        emp_dep   = input("Enter employee department:")
        emp_basic = int(input("Enter employee basic:"))
        emp_hra   = emp_basic*10/100
        emp_sal   = emp_basic + emp_hra
        L.append([emp_no,emp_name,emp_dep,emp_basic,emp_hra,emp_sal])
        print("%10s"%"emp_no","%10s"%"emp_name", "%15s"%"emp_dept", "%15s"%"emp_basic","%10s"%"emp_hra","%15s"%"emp_salary")
        print("%10s"%emp_no,"%10s"%emp_name, "%15s"%emp_dep, "%15s"%emp_basic,"%10s"%emp_hra,"%15s"%emp_sal)
        ch=input("do you want to continue?")
        if ch.lower()!='y':
            break
    obj.writerows(L)
    f.close()

CREATE()
'''

# 20 - Write a Python program to copy file1.csv into file2.csv
'''
def COPY():
    import csv
    with open('csv1_copy.csv', 'w') as outfile:
        with open('csv1.csv', 'r') as infile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                writer.writerow(row)
COPY()
'''