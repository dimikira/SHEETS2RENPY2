# SHEET2RENPY2
Take your .csv and export it to .rpy !

THE SHEET:
<br>![image](https://github.com/user-attachments/assets/cc363b0d-40ef-4888-b08e-482b4ac7f01a)
<hr>
<br>How to format the CSV: GENERAL
<li>Column A = Label
<li>Column B = Nametags + [Menus + Menu Choice] + [If + Elif + Else]
<li>Column C = Dialouge + Comments + Conditions
<hr>
How to format the CSV: LABEL
  <li> Add the name of the label in column A, leave the columns B and C empty.
<hr>
How to format the CSV: DIALOUGE
  <li> Add the name of the speaker in column B and the dialouge in the adjacent row in column C.
<hr>
How to format the CSV: COMMENTS
  <li> Leave columns A and B empty. start the comment with # and type in column C
<hr>
How to format the CSV: MENUS
  <li> To start a menu start in column B by typing menu. You can add an optional label to your menus in the adjacent row column C.
  <li> To add choices to the menu, type choice into column B and the choice text in the adjacent row in column C.
  <li> Underneath your choice row, add in any dialouge that's realted to the specific choice.
  <li> To close the menu, add an empty row afterwords.
<hr>
How to format the CSV: IF STATEMENT
  <li> To start an if statement start in column B by typing if. In the adjacent row, column C, add the condition for the statement.
  <li> To add elif, type elif into column B and the condition in column C.
  <li>  Underneath your if/elif row, add in any dialouge that's realted to the specific condition.
  <li> To end with an else block, type else into column B, and the associated text in the row underneath.
  <li> To close the statement, add an empty row afterwords.
<hr>
    
THE RENPY:
<br>![image](https://github.com/user-attachments/assets/7c190e78-186f-4461-ac1c-c0e662c2bc7b)

<li> Export your sheet as .CSV
<li> Download and run sheets2renpy2.py
<li> Paste the file path into the input window
<li> RPY IT!
<li> check the directory where you're keeping the .csv, the exported .rpy will be there!
  
<br>![image](https://github.com/user-attachments/assets/7882c769-49c7-4c2f-8839-65a41887ad7d)
  
<br>![image](https://github.com/user-attachments/assets/209eb3c5-026d-4513-a1c0-d43bb4b2f636)





