import csv
import sys
from tkinter import *

def submit():
    thepath = entry.get() #gets entry text
    sheetrenpy(entry.get())


def sheetrenpy(thepath):
    inmenu=False
    inifmenu=False

    with open(thepath, mode ='r',encoding="utf8")as file:
        csvFile = csv.reader(file)
        sys.stdout = open(thepath[:-4]+'.rpy', 'w')
        for lines in  csvFile:
            if len(lines[1])>=1:
                ####MENU
                if lines[1][0:4] == "menu":#menu header
                    if len(lines[2])>1:
                        print("\n    "+lines[1]+" "+lines[2]+ ":#menu start        " )
                    else:
                        print("    "+lines[1]+ ":#menu start    ")
                elif lines[1] == "choice":#menu choice text
                    inmenu=True
                    print("\n        \""+lines[2]+ "\":#menu choice")
                elif inmenu:#menu choice dialouge
                    if "\n" not in lines[2]:
                        print("            "+lines[1]+"    \""+lines[2]+ "\"")   
                    else:
                        for ii in lines[2].splitlines():
                            print("            "+lines[1]+"    \""+ii+ "\"")   
                ####IF'S
                elif lines[1][0:2] == "if" or lines[1][0:4] == "elif":
                    if lines[1][0:2] == "if":
                        print("\n")
                    inifmenu=False
                    print("    "+lines[1]+"    "+lines[2]+":" )
                    inifmenu=True
                elif lines[1][0:4] == "else":
                    inifmenu=False
                    print("    "+lines[1]+":")
                    inifmenu=True
                elif inifmenu:#if choice dialouge
                    print("        "+lines[1]+"    \""+lines[2]+ "\"")
                    
                ####REGULAR DIALOUGE
                else:#regular dialouge
                    if "\n" not in lines[2]:
                            print("    "+lines[1]+ "    \""+lines[2]+ "\"")
                    else:
                        for ii in lines[2].splitlines():
                            print("    "+lines[1]+ "    \""+ii+ "\"")
                    
            elif len(lines)==1 and lines[0][0]!="#":#label
                print("label "+lines[0]+":\n")
            
            else:
                #for i in lines:
                if len(lines[0])>1:
                    print("label "+lines[0]+":\n")
                elif lines == ["","",""]:
                    inmenu=False
                    inifmenu=False
                    print("\n")
                else:
                    for i in lines:
                        if i!="":
                            print("    #"+str(i)) 

    
    sys.stdout.close()


##ui colours
col1='#f1f7ed'
col2='#7ca982'
col3='#243e36'
fontui='consolas'
##

window = Tk()
window.title("sheets 2 renpy 2")
window.config(bg=col1)
window.geometry("500x200")
window.eval('tk::PlaceWindow . center')
window.resizable(width=False, height=False)


label = Label(window,text="enter your file path here!")
label.config(font=(fontui,15),bg=col1,fg=col2)
label.pack(side=TOP,pady=10)

entry = Entry()
entry.config(font=(fontui,15),bg='#fff',fg=col3,width=40)
entry.insert(0,'yourfilepath.csv') #set default text
entry.pack(pady=15)

label2 = Label(window,text="©️dimikira 2024")
label2.config(font=(fontui,10),bg=col1,fg=col2)
label2.pack(side=BOTTOM,)

submit = Button(window,text="rpy it!",command=submit,activebackground=col2)
submit.config(width=20,bg=col1,fg=col2,font=(fontui,15))
submit.config(padx=5,  pady=5)
submit.pack(side = BOTTOM,pady=10)
window.mainloop()

#main()
