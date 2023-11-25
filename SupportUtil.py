# Supporttoolkit created by Umakant Tripathi
# Python Support tool kit to create a dashboard in Tkinter with UI input

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from datetime import datetime
main = Tk()
main.title('Support utils');

frame1 = Frame(main)
frame2 = Frame(main)
frame3 = Frame(main)

label = Label(frame1,text='Please finish your course', width=30);
label.pack()

labelName = Label(frame1, text='Please enter your name', width=20);
labelName.pack(padx=10,pady=10,side=LEFT);

entryName = Entry(frame1, width=20)
entryName.pack(padx=10,pady=10,side=RIGHT);

labelMsg = Label(frame2,text='Have you finished task 1,2,3',font='Helvetica 18 bold', width=30);
labelMsg.pack()

labelErr = Label(frame2,text='',font='Helvetica 18 bold',fg='RED', width=30);
labelErr.pack()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def show_message(error='', color='RED'):
    labelErr['text'] = error
    entryName['foreground'] = color

def buttonYesClick():
    #To be called on button click

    #Create message to write to file
    currentTimeStamp = datetime.now();
    confirmMessage = "\n" + currentTimeStamp.strftime("%m/%d/%Y %H:%M:%S") + " | " + entryName.get() + " | " + "Yes, I have finished above tasks 1234"

    # Validate username
    if entryName.get() == "":
        show_message('Please enter a valid name', 'red')
    else:
        # Write to file
        with open('C:/temp/Confirmation.txt', 'a') as f:
            # f.writelines({entryName.get()});
            f.writelines(confirmMessage);
        f.close();
        main.destroy();

    # Label to display once done
    #label = Label(main, text='Confirmed!, your input recorded', width=100);
    #label.pack();

    #nameConfirm = main.entryName.get();

    #print('Text from entry:')
    #print(entryName.get());
    #print(date.today());

def buttonNoClick():
    #To be called on button click

    #Create message to write to file
    currentTimeStamp = datetime.now();
    confirmMessage = "\n" + currentTimeStamp.strftime("%m/%d/%Y %H:%M:%S") + " | " + entryName.get() + " | " + "No , I have finished above tasks 1234"

    #Validate username
    if entryName.get() == "":
        show_message('Please enter a valid name', 'red')
    else:
        # Write to file
        with open('C:/temp/Confirmation.txt', 'a') as f:
            # f.writelines({entryName.get()});
            f.writelines(confirmMessage);
        f.close();
        main.destroy();




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    buttonYes = Button(frame3, text='Yes', width=8,bg='GREEN',font='BOLD', command=buttonYesClick);
    buttonYes.pack(side=LEFT,padx=5);

    buttonNo = Button(frame3, text='No', width=8, bg='RED',font='BOLD', command=buttonNoClick);
    buttonNo.pack(side=RIGHT,padx=5);

    frame1.pack(padx=5, pady=5)
    frame2.pack(padx=1, pady=1)
    frame3.pack(padx=20, pady=20)

    main.mainloop();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
