from statistics import *

admins = {'Python':'hello'}
student_dict = {'Jeff':[78, 88, 93],
                'Alex': [92, 76, 88],
                'Sam':[89, 92, 93]}

menu = """

Welcome to Grade Central

[1] - Enter Grades
[2] - Remove Student
[3] - Student Average Grades
[4] - Exit
"""


task_options = ['1', '2', '3', '4']


def login():
    login = input('Username: ')
    passw = input('Password: ')
    if login in admins:
        if admins[login] == passw:
            print('welcome',login)
            while True:
                main()


def input_task(menu):
    print(menu)
    task = input('What would you like to do today? (Enter a number): ')
    return task


def gradebook(task, task_options):
    while task == '4':
        exit()
    
    while task != '4':
        
        if task in task_options:
                navigation(task)
                task = input_task(menu)
            
        if task not in task_options:
            print("Please enter a valid response")
            task = input_task(menu)
            navigation(task) 


def navigation(task):
    if task == '1':
        enter_grades()

    if task == '2':
        remove_student()

    if task == '3':
        student_average()


def enter_grades():
    student = input("Which student has a new grade? ")
    new_grade = int(input("Enter new grade for " + student + ": "))

    if student in student_dict:
        print('Adding Grade...')
        student_dict[student].append(new_grade)
        print("Here are "+student+"'s grades: ")
        print(student_dict[student])
    
    else:
        print('Student not in gradebook')


def remove_student():
    print("Remove Student")
    student = input("Which Student would you like to remove? ")


    print(student + " has been removed from your gradebook.")


def student_average():
    print("Student Average Grades")
    
    for student in student_dict:
        grade_list = student_dict[student]
        avg_grade = str(round(mean(grade_list)))
        print(student +"'s average grade is "+avg_grade+".")


def main():
    
    task=input_task(menu)
    gradebook(task, task_options)
     

if __name__ == "__main__":
    login()
