#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import pymysql
import os
# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import string
import pymysql
print("Content-type: text/html\n")
print("<title>Assignment1 progress<</title>")

r = os.popen("curl ifconfig.me")
exip = r.read()
r.close()
f = open("ip.txt","r")
ip = f.read()
sqlip = ip.replace("\n","")
f.close()
with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)

print("<head>")
print("<style type='text/css'>")
print("th,td{border:2px solid black;}")
print("table{padding: 60px 50px;}")
print("input:hover { background-color:green; /* Green */    color: white;border-radius: 50%;}")
print("input,button {color: green; text-align: left; text-decoration: none; display: inline-block; font-size: 16px;border: 2px solid #4CAF50;border-radius: 50%;}")
print("body {background:url('http://blog.hostbaby.com/wp-content/uploads/2014/03/PaintSquares_1400x900-1024x658.jpg');background-size:98% 100%;background-repeat:no-repeat; }")
print("h1{text-shadow: 5px 5px 5px #95CACA;text-align:center;text-decoration:overline;letter-spacing:2px;")
print("</style>")
print("</head>")
print("<body><center>")
print("<h1>Progress of Assignment1</h1>")
print("<table>")
print("<tr><th>ID/task</th><th>first</th><th>second</th><th>third</th><th>fifth</th><th>sixth</th><th>seventh</th><th>eight</th></tr>")
for i in list_of_students:
        print("<tr>")
        print("<td><a href='http://%s/%s' target='_blank'>student%s</a></td>"%(exip,str(i[4]),str(i[0])))
        form = cgi.FieldStorage()
        # query to check password and get permissions
        sql= "select 1 from mdl_course"
        sq1= "select 1 from mdl_user"
        sq2= 'SELECT 1 FROM mdl_user WHERE password="123" and username="Betty Birch" and idnumber="bbirch" and email="bettybirch120@gmail.com"'
        sq3='SELECT 1 FROM `mdl_user` WHERE picture!=0'
        sq5="SELECT 1 FROM `mdl_assign_submission` WHERE status='submitted'"
        sq6="SELECT DISTINCT(userid) FROM mdl_forum_discussions"
        sq7="SELECT 1 FROM mdl_url"
        sq8="SELECT 1 FROM `mdl_files` WHERE component='mod_resource'"
        # connect to database
        conn = pymysql.connect(host=sqlip,user="root",password="Moodle123moodle",db ="student%s"%str(i[0]),charset ="utf8")
        #1
        cursor = conn.cursor()
        cursor.execute(sql)
        courses = cursor.fetchall()
        if len(courses)>=3 :
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        #2
        cursor1 = conn.cursor()
        cursor1.execute(sq1)
        user=cursor1.fetchall()
        cursor2 = conn.cursor()
        cursor2.execute(sq2)
        spe=cursor2.fetchall()
        if len(user)>=6 and len(spe)!=0 :
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        #3
        cursor3 = conn.cursor()
        cursor3.execute(sq3)
        pic=cursor3.fetchall()
        if len(pic)!=0:
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        #5
        cursor5 = conn.cursor()
        cursor5.execute(sq5)
        sub=cursor5.fetchall()
        if len(sub)>=2:
                print("<th>ok</th>")
	else:
                print("<th>no</th>")
        #6
        cursor6 = conn.cursor()
        cursor6.execute(sq6)
        forum=cursor6.fetchall()
        if len(forum)>=3:
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        #7
        cursor8 = conn.cursor()
        cursor8.execute(sq7)
        files=cursor8.fetchall()
        if len(files)>= 1:
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        #8
        cursor7 = conn.cursor()
        cursor7.execute(sq7)
        url=cursor7.fetchall()
        if len(url)>= 1:
                print("<th>ok</th>")
        else:
                print("<th>no</th>")
        print("</tr>")
print("</table>")
print("""
<form action="../login.html" method="GET">
    <input type="submit" value="Back to progress">
</form>
""")
print("<td><button id='btn'>phpmyadmin</button></td>")
print("<script type='text/javascript'>")
print("var btn = document.getElementById('btn')")
print("btn.onclick=function(){window.location.href='http://%s/phpMyAdmin'}"%exip)
print("</script>")
print("<h3>You can check all the changes in their moodle site</h3>")
print('</center></body>')		
