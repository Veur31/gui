from add_student import *
from print_allstudent import *
from search import *
from student import *

import os

stu = Studentinfo()
search = Search(stu)
print_all =Print_allstudent(stu)
addstu = AddStudent(stu)
stu.read()

def clear():
     choice = input("Go back to main menu? (Y/N): ").upper()
     if choice == 'Y':
          os.system('cls')
          main()
     else:
          os.system('cls')
def line():
    line = "="
    count = 60
    result = line * count
    print(result)
def line2():
    line = "="
    count = 20
    result = line * count
    print(f"{result} Student information {result}")
def line3():
    line = "="
    count = 23
    result = line * count
    print(f"{result} Nothing follows{result}")


def login():
     attemps = 0
     while attemps < 4:
          print("============Login=============")
          user4 = input("Enter ID: ")
          global user2
          user2 = search.verify(user4)
          if user2 != False:
               main()
          else:
               attemps += 1
          if attemps == 3:
               print("Error")
               exit()
          

def main():
   # login()
    #print(f"Welcome, {user1}!")
    print("1. View  your information\n2. View other student's information\n3. Register a new student\n4. Print all students in the list\n5. Exit")
    print()
    choice = input("Enter your choice: ")
    line()
    
    if choice == "1":
         print()
         print(search.search_student(user2))
         print()
         clear()
    elif choice == "2":
         choice = "Y"
         while choice == "Y":
            print()
            idnum = input("\nEnter ID Number: ")
            line2()
            print(search.search_student(idnum))
            line3()
            choice = input("Do you want view other student's information? (Y/N): ").upper()
            print()
         clear()
    elif choice == "3":
        choice = "Y"
        while choice == "Y":
            addstu.new_student()
            print()
            choice = input("Do you Want to add new student? (Y/N): ").upper()
        clear()
    elif choice == "4":
         print(print_all.printStudentInfo())
         print()
         clear()
    elif choice == "5":
        exit()

    else:
         print("Invalid Input")
         main()
login()
     

