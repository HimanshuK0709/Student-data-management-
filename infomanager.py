import json
data={}
def save_to_file():
    with open("students_data.json","w") as f:
        json.dump(data,f)   
def Data_Entry():
    num_of_students=int(input("Enter num of students="))
    for i in range(num_of_students):
        Roll_num=int(input("Enter the roll number of the student:"))
        name=(input("Enter the name of the student:")).capitalize()
        data[Roll_num]=name
    save_to_file()
    
def Data_Access():
    data_ques=input("What data you want?\n"
                    "A-> Data of all students\n"
                    "B-> Data of particular student\n"
                    "Enter option of your choice=").upper()
    if len(data_ques)==1 and data_ques in "AB":
        if data_ques=="A":  
          with open("students_data.json","r") as f:
              print(f.read())
        elif data_ques=="B":
            ask_roll_num=int(input("Enter roll number of the student to access it's data:"))
            with open("students_data.json","r") as f:
                data2=json.load(f)

            for x in data2:
                if int(x)==ask_roll_num:
                    print(x,data2[x])                    

    
def menu():
    global data
    try:
        with open("students_data.json","r") as f:
            data=json.load(f)
    except:
        with open("students_data.json","w") as f:
            data={}
    while True:
        user=input("What you want to do?\n"
        "A->Enter data of students.\n" 
        "B->Access data of students.\n"
        "C->Exit the program.\n"
        "Enter option of your choice=").upper()
        if len(user)==1 and user in "ABC":
                if user=="A":
                    Data_Entry()
        
                elif user=="B":
                    Data_Access()
                elif user=="C":
                    print("Thank you for coming!")
                    break
        else:
            print("Enter only one option that is to be chosen!")
        

user=menu()
