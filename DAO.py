import bcrypt
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Akhil@63057',database='stu_management')
cur=mydb.cursor()
class StudentDAO:
    display=None
    def __init__(self):
        # You set in a try statement so that the user knows why it crashes if there is no file
            # This array will hold the list of students in it
    
        f='select email,name,password from students'
        cur.execute(f)  
        self.display=cur.fetchall()
            # Read in the student table
    def hash_fun(self,password):
        salt=bcrypt.gensalt()
        password=password.encode('utf-8')
        hashed=bcrypt.hashpw(password,salt)
        return hashed
    def validate_user(self, email, pw):
        pw=pw.encode('utf-8')
        for k in self.display:
            if k[0] == email and bcrypt.checkpw(pw,k[2].encode('utf-8')): #cycles through the classes to find the right one
                return True
        return False

    def get_student_by_email(self, email):
        for i in self.display:
                if email in i[0]:
                    return False
        return True

    def add_new_student(self, email, name, password):
        q='insert into students(email,name,password) values(%s,%s,%s)'
        v=(email,name,password)
        cur.execute(q,v)
        mydb.commit()
        print("You've been added!")

class CourseDAO:
    courses=None
    def __init__(self):
        f='select courseid,coursename,instructorname from cources'
        cur.execute(f)  
        self.courses=cur.fetchall()
            # Read in the student table

    def show_all_courses(self):
        for i in self.courses:
            print(i[0],i[1],i[2])
class AttendingDAO:
    attending=None
    def __init__(self):
        # You set in a try statement so that the user knows why it crashes if there is no file
        f='select courseid,email from attending'
        cur.execute(f)  
        self.attending=cur.fetchall()
    
    def register_student_to_course(self,course_id,email):
        totalCourses = []
        c=CourseDAO()
        for k in c.courses:
            totalCourses.append(k[0])

        if course_id in totalCourses:
            flag = True
            for k in self.attending:
                if k[0]==course_id and k[1]==email:
                    flag = False
            if flag == True:
                q="insert into attending values(%s,%s)"
                v=(course_id,email)
                cur.execute(q,v)
                print("I've added you to the class")
                mydb.commit()
                return True
            else:
                print("You are already in this class!")
                return False
        else:
            print("This is not a class!")
            return False
    def show_my_courses(self,email):
        f='select * from attending'
        cur.execute(f) 
        mycourcses=cur.fetchall()
        for i in mycourcses:
            if i[1]==email:
                print(i[0],i[1])

        















#
