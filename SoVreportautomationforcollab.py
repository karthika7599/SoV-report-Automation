import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import csv
import re
def count_words(URL1,the_word):
    word=" "
    w=the_word
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    r1 = requests.get(URL1, headers=headers)
    soup1=BeautifulSoup(r1.content,'lxml')
    print(soup1.get_text())
    s=[]
    s.append(str(soup1.find_all(string=re.compile(w,re.I))))
    print(s)
    for i in s:
         b=i.lower()
         n=re.findall(w,b)
    return len(n)
    
def main():
    print("Do you want to enter new details or read from old file? Enter 1 to enter new details and 0 to read")
    choice=input(" ")
    if(choice=='1'):
     print("Enter the brand name")
     b=input("")
     text=".txt"
     textname=b+text
     file1=open(textname,"w")
     print("Enter the number of competitors")
     nb=int(input(""))
     file1.write(str(nb))
     file1.write("\n")
     print("Enter the competitors name")
     l1=[]
     ld=[]
     for i in range(nb):
          l1.append(input(" "))
          ld.append(l1[i])
     l1.append(b)
     print(l1)
     for i in range(nb):
      file1.writelines(ld[i])
      file1.write("\n")
     print("Enter the number of categories")
     nc=int(input(""))
     file1.write(str(nc))
     file1.write("\n")
     print("Enter the category names")
     l2=[]
     for i in range(nc):
        l2.append(input(" "))
     print(l2)
     for i in range(nc):
      file1.writelines(l2[i])
      file1.write("\n")
     print("Enter the URL of the categories in same order")
     l3=[]
     for i in range(nc):
        l3.append(input(" "))
     print(l3)
     for i in range(nc):
      file1.writelines(l3[i])
      file1.write("\n")
     print("Enter total count")
     tt=int(input())
     file1.write(str(tt))
     file1.write("\n")
     wb=Workbook()
     sheet1=wb.add_sheet('Sheet 1')
     for i in range(nb+1):
           sheet1.write(0,i+1,l1[i])
     for i in range(nc):
          sheet1.write(i+1,0,l2[i])
     c=[]
     y="%"
     for j in range(nc):
       for i in range(nb+1):
          c.append(count_words(l3[j],l1[i]))
          sheet1.write(j+1,i+1,f'{int(((c[i]/tt)*100))}{"%"}')
       c=[]
     add="SoVreport"
     name=b+add
     dest=name+".csv"
     print(dest)
     wb.save(dest)   
    elif(choice=='0'):
       print("Enter the brand name")
       b=input("")
       text=".txt"
       textname=b+text
       file1=open(textname,"r+")
       nb=file1.readline()
       print(nb)
       l1=[]
       for i in range(int(nb)):
         l1.append(file1.readline().rstrip('\n'))
       l1.append(b)
       print(l1)
       nc=file1.readline()
       l2=[]
       for i in range(int(nc)):
        l2.append(file1.readline().rstrip('\n'))
       print(l2)
       l3=[]
       for i in range(int(nc)):
        l3.append(file1.readline().rstrip('\n'))
       print(l3)
       tt=file1.readline()
       print(tt)
       wb=Workbook()
       sheet1=wb.add_sheet('Sheet 1')
       for i in range(int(nb)+1):
          sheet1.write(0,i+1,l1[i])
       for i in range(int(nc)):
          sheet1.write(i+1,0,l2[i])
       c=[]
       y="%"
       for j in range(int(nc)):
        for i in range(int(nb)+1):
          c.append(count_words(l3[j],l1[i]))
          sheet1.write(j+1,i+1,f'{int(((c[i]/int(tt))*100))}{"%"}')
        c=[]
       add="SoVreport"
       name=b+add
       dest=name+".csv"
       print(dest)
       wb.save(dest)    
if __name__== '__main__':
    main()
