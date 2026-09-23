# Python +streamlit project
# Motive of this project is to revise important pythons concepts 
# Project Name : University Management System

import streamlit as st


st.set_page_config(page_title="University Management System", layout="wide")
st.title("University Management System")

#create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice=st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "List of Colleges"
    )
)

#college class is storing the college name, students and teachers of that college
class college:
    def __init__(self, cname):
        self.name = cname
        self.students = []
        self.teachers = []
    def add_student(self,s):
        self.students.append(s)
    def add_teacher(self,t):
        self.teachers.append(t)

class person:
    def __init__(self,branch,name):
        self.branch=branch
        self.name=name

class student(person):
    def __init__(self,sname,roll,branch):
        self.roll=roll
        super().__init__(branch,sname) # calling parent constructor function to store student name ,branch

class teacher(person):
    def __init__(self,tname,branch,subject):
        self.subject=subject
        super().__init__(branch,tname)

# Based on college name,college class object is find
def find_college(cname):
    for clg in st.session_state.colleges:
        if clg.name==cname:
            return clg
    return None

if menu_choice=="Create College":
    cname=st.text_input("Enter new College Name")
    if st.button("Create College"):
        clg_obj=college(cname)  # creat a college class object
        st.session_state.colleges.append(clg_obj)  #storing a college class object in college list
        st.success(f"College '{cname}' created successfully!")

elif menu_choice=="Add Student":
    if not st.session_state.colleges:
        st.info("Please add college first")
    else:
        cname=st.selectbox("Select College", [clg.name for clg in st.session_state.colleges])
        roll=st.number_input("Enter Student Roll Number",min_value=1,max_value=100)
        sname=st.text_input("Enter Student Name")
        branch=st.text_input("Enter student Branch")
        if st.button("Add Student"):
            if not (roll and sname and cname and branch):
                st.error("Please don't leave any info blank")
            else:
                clg_obj=find_college(cname) #find college object based on college name
                stu_obj=student(sname,roll,branch)
                clg_obj.add_student(stu_obj)
                st.success(f"Student '{sname}' of {branch} added to college '{cname}' successfully!")

elif menu_choice=="Add Teacher":
    if not st.session_state.colleges:
        st.info("Please add college first")
    else:
        cname=st.selectbox("Select College", [clg.name for clg in st.session_state.colleges])
        subject=st.text_input("Enter Teacher Subject")
        tname=st.text_input("Enter Teacher Name")
        branch=st.text_input("Enter Teacher Branch")
        if st.button("Add Teacher"):
            if not (subject and tname and cname and branch):
                st.error("Please don't leave any info blank")
            else:
                clg_obj=find_college(cname) #find college object based on college name
                teacher_obj=teacher(tname,branch,subject)
                clg_obj.add_teacher(teacher_obj)
                st.success(f"Teacher '{tname}' of {branch} added to college '{cname}' successfully!")

elif menu_choice=="Display Students":
    if not st.session_state.colleges:
        st.info("Please add college first")
    else:
        cname=st.selectbox("Select College", [clg.name for clg in st.session_state.colleges])
        clg_obj=find_college(cname)
        st.subheader(f"List of students:{cname}")
        if clg_obj.students:
            for s in clg_obj.students:
                st.write(s.roll, ":", s.name, "-", s.branch)
        else:
            st.warning("No Student found")

elif menu_choice=="Display Teachers":
    if not st.session_state.colleges:
        st.info("Please add college first")
    else:
        cname=st.selectbox("Select College", [clg.name for clg in st.session_state.colleges])
        clg_obj=find_college(cname)
        st.subheader(f"List of Teachers:{cname}")
        if clg_obj.teachers:
            for t in clg_obj.teachers:
                st.write(t.subject, "-", t.name, "-", t.branch)
        else:
            st.warning("No Teacher found")

elif menu_choice == "List of Colleges":
    st.subheader("List of Colleges")

    if not st.session_state.colleges:
        st.info("Please add college first")
    else:
        for i, clg in enumerate(st.session_state.colleges,start=1):
            st.write(f"{i} : {clg.name}")