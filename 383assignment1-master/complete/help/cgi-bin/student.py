#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import csv



def Student_list(file_name):
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
            list_of_students.append(row)
            # Remove metadata from top row
        list_of_students.pop(0)
    return list_of_students

def match_site(slist,name):
    count=0
    for i in slist:
        if i[4] ==name:
            print('<script type="text/javascript"> ')
            print("location.href ='http://' + window.location.href.split('/')[2]+'/'+'%s';"%name)
            print('</script>')

        else:
            count=count+1
    if count==len(slist):

         print("Your site name is wrong ,please check it")
         print("""
            <form action="../student.html" method="GET">
                <input type="submit" value="Back to Home page">
            </form>
            """)




print("Content-type: text/html\n")
print("<title>Result</title>")
print("<body><center>")

form = cgi.FieldStorage()
name = form['id'].value if 'id' in form else ''
students=Student_list("StudentDatas.csv")
match_site(students,name)
print('</center></body>')
                               
