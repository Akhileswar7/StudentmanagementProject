import DAO
def main():
    print('Welcome!')
    entry=None
    while entry!='2':
        entry = input('\n1. Current Student\n2. New Student\n3. Quit\nPlease, enter 1, 2 or 3: ')

        if entry=='1':
            student_dao = DAO.StudentDAO()
            email = input('\nEnter Your Email: ')
            pwd = input('Enter Your Password: ')

            if student_dao.validate_user(email, pwd):
                attending_dao=DAO.AttendingDAO()
                course_dao=DAO.CourseDAO()
                print("Login Successfull.")
                print('\nWhat Would You Like To Do?')

                while entry!='2':
                    entry = input('\n1. Register To Course\n2. Logout\nPlease, enter 1 or 2: ')

                    if entry=='1':
                        course_dao.show_all_courses()
                        course_id = input('\nSelect Course By ID Number: ')
                        print("\nAttempting to Register...")
                        if attending_dao.register_student_to_course(course_id,email):
                            attending_dao.show_my_courses(email)
                    elif entry=='2':
                        print('\nYou Have Been Logged Out.')
                    else:
                        print('\nInvalid Option...')


            else:
                print('\nWrong Credentials!')
        elif entry=='2':
            print("Welcome to the school!")
            student_dao = DAO.StudentDAO()
            email = input('Please provide your email : ')
            if student_dao.get_student_by_email(email):
                name = input("What is your full name? : ")
                password = input("What would you like your password to be? : ")
                password = student_dao.hash_fun(password)
                student_dao.add_new_student(email, name, password)
                entry = '-1'
                continue;
            else:
                print("That email is already taken")

        elif entry=='3':
            print("Programming is closing, ")
            break;
        else:
            print('Invalid Option...')
    print('\nClosing Program. Goodbye.')

if __name__=='__main__':
    main()
