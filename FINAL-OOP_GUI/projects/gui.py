#importing different libraries and files
from tkinter import *
from functools import partial
from login import *
from add_student import *
from print_allstudent import *
from search import *
from add_student import *
from student import *
from login import  *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


#assigning objects
stu = Studentinfo()
stu.read()
search = Search(stu)
print_all =Print_allstudent(stu)
addstu = AddStudent(stu)
login1 = Login(stu)


win = Tk()
btns = []
win.config(bg="#1e1d1d")
#functions
def login():
    global curr_stu
    login_result = login1.login(login_entry.get())
    if login_result:
        curr_stu =login_result
        login_frame.pack_forget()
        menu_contain.pack(side="left", fill="y")
        content_contain.pack(side="right", fill="both")
        for content in content_contain.winfo_children():
            content.destroy()
        Label(content_contain, text=f"Welcome Admin, {login_result.getName()}!", font=("Century Gothic", 28), fg="#00BFFF", bg="#1e1d1d").grid(row=0, column=0, sticky="ew", pady=350, padx=260)
    else:
        error.config(text="Invalid id number", fg="#e17676")
        error.pack(pady=10)

def view_information():
    for content in content_contain.winfo_children():
        content.destroy()
    if curr_stu: 
        Label(content_contain, text="", font=("Century Gothic", 20, "bold"), bg="#1e1d1d").grid(row=0, column=0,sticky="nsew", pady=100, padx=200)
        Label(content_contain, text="Information\n", font=("Century Gothic", 30, "bold"), fg="#00BFFF", bg="#1e1d1d").grid(row=1, column=0, columnspan=2,  pady=10, padx=350)
        Label(content_contain, text=curr_stu, font=("Century Gothic", 20), fg="#00BFFF", bg="#1e1d1d", justify="left").grid(row=2, column=0, sticky="ew", pady=1, padx=310)
    else:
        Label(content_contain, text="No student is logged in!", font=("Century Gothic", 20), fg="red", bg="white").grid(row=0, column=0, sticky="ew", pady=350, padx=250)
def logout():
    global curr
    curr = None
    content_contain.pack_forget()
    error.config(text="")
    menu_contain.pack_forget()
    login_frame.pack(fill="both", expand=True)
    login_entry.delete(0,END)

def check_button_click():
    check(label_error)
def add_new_student():
    
    global text_entry, label_text, label_error
    for content in content_contain.winfo_children():
        content.destroy()
    #adding label in the content
    Label(content_contain, text="", font=("Century Gothic", 20, "bold"), fg="black", bg="#1e1d1d").grid(row=0, column=0, columnspan=2,  pady=100, padx=200)
    Label(content_contain, text="Add student", font=("Century Gothic", 30, "bold"), fg="#00BFFF", bg="#1e1d1d").grid(row=1, column=0,
    columnspan=2, sticky="nsew", pady=10, padx=200)
    label_error = Label(content_contain, text = "", font=("Century Gothic", 14), fg="#e17676", bg="#1e1d1d")
    label_error.grid(row=8, column=0,columnspan=2, sticky="ew", pady=10)
    label_text = ["Name", "Age", "Student ID", "Email", "Phone Number"]
    text_entry = []
    #looping through all the label to add Entry
    for i in range(len(label_text)):
        Label(content_contain, text = f"{label_text[i]}:", font = ("Century Gothic", 14, "bold"), anchor = "e", width=14, bg="#1e1d1d",fg="#00BFFF").grid(row= i+2, column=0)
        text = Entry(content_contain, width= 38, font=("Century Gothic", 14, "bold"))
        text.grid(row = i+2, column= 1, pady =5, padx=20 )
        text_entry.append(text)
    save_button =Button(content_contain, text = "Add", font=("Century Gothic", 14), bg="#00BFFF", command=check_button_click)
    save_button.grid(row=len(label_text) + 2, column=0, columnspan=2, pady=20)



#checking the entry for inputs
def check(label_error):
    error = []
    for i in range(len(text_entry)):
        if not text_entry[i].get().strip():
            
            error.append(f"Input your: {label_text[i]}")
    if error:
        label_error.config(text = "\n".join(error))
    else:
        data = [entry.get().strip() for entry in text_entry]
        result = addstu.save(data[0], data[1],data[2], data[3], data[4])
        label_error.config(text=result, fg= "#82f882")


def view_other_information():
    for content in content_contain.winfo_children():
        content.destroy()
    Label(content_contain, text="", font=("Century Gothic", 14), bg="#1e1d1d").grid(row = 0, column= 0, columnspan =2, pady= 110, padx=500)
    Label(content_contain, text="Enter Student Id", font=("Century Gothic", 25, "bold"),  bg="#1e1d1d", fg="#00BFFF").grid(row = 1, column= 0, columnspan =2, pady= 50, padx=150)

    id_entry = Entry(content_contain, font=("Century Gothic", 14))
    id_entry.grid(row = 2, column=0, padx=20, columnspan=2)

    result_l =Label(content_contain, text = "", font=("Century Gothic", 14),bg="#1e1d1d")
    result_l.grid(row = 4, column=0, columnspan=2, pady=20)
    def srch_stu():
        id =id_entry.get().strip()
        if not id:
            result_l.config(text="Enter valid Student number: ", fg="#e17676",  bg="#1e1d1d",font=("Century Gothic", 14))
        else:
            result = search.search_student(id)
            result_l.config(text=result, fg="#00BFFF",  bg="#1e1d1d")


    search_btn =Button(content_contain, text="Search", font=("Century Gothic",14), command=srch_stu,  bg="#00BFFF")
    search_btn.grid(row =3, column=0, columnspan=2, pady=20, padx=10)
    id_entry.delete(0,END)

    
def view_all_stu():
    for content in content_contain.winfo_children():
        content.destroy()
    # Clear existing content

    Label(content_contain, text="", font=("Century Gothic", 14),bg="#1e1d1d").grid(row = 0, column= 0, columnspan =2, pady= 90, padx=315)
    Label(content_contain, text="All registered\nstudents", font=("Century Gothic", 25,"bold"), bg="#1e1d1d", fg="#00BFFF").grid(row = 1, column= 0, columnspan =2, pady= 50, padx=150)

    # Retrieve student information
    info = print_all.printStudentInfo()
    scroll = scrolledtext.ScrolledText(content_contain, wrap=tk.WORD, font=("Century Gothic", 14),bg="#2e2c2c",fg="#00BFFF", height= 10, width= 50)
    scroll.grid(row = 2, column=0, sticky="ew", padx=200, pady=10)
    scroll.insert(tk.END, info)
    scroll.config(state=tk.DISABLED)


    

        
#login frame
login_frame = Frame(win, bg="#1e1d1d")
login_frame.pack(fill="both", expand=True)
float_frame = Frame(login_frame, bg="#1e1d1d", padx=20, pady =10, relief="solid")
float_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
Label(float_frame, text="Enter ID", font=("Century Gothic", 20),fg="#00BFFF",padx=20,bg="#1e1d1d").pack()
login_btn = Button(float_frame, text="Login", width=10, font=("Century Gothic", 18),bg="#00BFFF", command=login)

login_entry = Entry(float_frame, width=10, font= ("Century Gothic", 20), show="*")
login_entry.pack(pady=10, padx=100)
login_btn.pack(pady=10, padx=100)

error= Label(float_frame, text = "", font=("Century Gothic", 20), fg="red", bg="#1e1d1d")
error.pack()


#main_manu frame
main_frame =Frame(win, bg="#1e1d1d")
Label(main_frame, text="", font=("Century Gothic", 20), padx=20).pack()
logout_btn = Button(main_frame, text="Logout", width=20, font=("Century Gothic", 20), command=logout)
logout_btn.pack()
btn_txt = ["View information","Add Student","View Other student information", "View all student"]
btn_txt1 = []
Func = [view_information, add_new_student, view_other_information, view_all_stu] 

#geometry
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
menu_contain = Frame(win, borderwidth=1, bg="#1e1d1d", relief="sunken")

content_contain = Frame(win, borderwidth=1, bg="#1e1d1d")

content_contain.grid_columnconfigure(0,weight=1)

#buttons na ilalagay sa menu
Label(menu_contain, text="Main Menu", font=("Century Gothic", 30),fg="#00BFFF", bg = '#1e1d1d', padx=20).grid(row=0, column=0, pady=50)
for i, txt in enumerate(btn_txt): 
    btns = Button(menu_contain, anchor="center", width=30, text=btn_txt[i], font=("Century Gothic", 14), padx=10, pady=35, bg="#8ddbf5")
    btns.grid(row=i+1, column=0)
    btns.config(command=partial (Func[i]))
Label(content_contain, text="Content", font=("Century Gothic", 20),fg="white", bg = 'black', padx=20).grid(row=0, column=0, sticky="ew") 
for i, txt in enumerate(btn_txt1):
    btns = Button(content_contain, anchor="center", width=40, text=btn_txt1[i], font=("Century Gothic", 14), padx=10, pady=15, bg="#FFFFFF")
    btns.grid(row=i+1, column=0)
    btns.config(command=partial ())
logout_btn = Button(menu_contain, text="Logout", width=20, font=("Century Gothic", 20),padx=10,pady=20, command=logout)
logout_btn.grid(row=5,column=0, sticky="ew")

win.mainloop()