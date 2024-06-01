from tkinter import *
import pyttsx3
run=run1=run2=0








screen= Tk()
screen.title("MY FIRST GAMING PROGRAM")
screen.geometry("1000x1000")
screen.resizable(False,False)
screen_lable = Label(screen,bg = "purple")


welcome_text = Label( text = '''WELCOME
TO
HOTEL HAYAT''',fg = "gold",bg = "purple",height = 5 , width = 500,font =("Algerian",60,"bold"))    
welcome_text.pack()

canvas = Canvas(width = 2000,height = 400, bg ="purple")

canvas.pack()
def main():
    

    def run():
        screen.destroy()
        screen2= Tk()
        screen2.title("MY FIRST GAMING PROGRAM")
        screen2.geometry("1000x1000")
        screen2.resizable(False,False)
        
        f2 = Frame(screen2, borderwidth=8, bg="gold", relief=SUNKEN)


        f2.pack(side=TOP, fill="x")


        l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


        l.pack()


        canvas = Canvas(width = 2000,height = 1000, bg ="purple")
        canvas.pack()

        def run1():
            screen2.destroy()
            root = Tk()
            root.geometry('1000x1000')
            root.title("Create an acount")
            root.resizable(False,False)
            f2 = Frame(root, borderwidth=8, bg="gold", relief=SUNKEN)


            f2.pack(side=TOP, fill="x")


            l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


            l.pack()


            welcome_text = Label( root,text = '''CREATE AN ACCOUNT''',fg = "gold",bg = "purple",height = 5 , width = 200,font =("Algerian",40,"bold"))    
            welcome_text.pack()

            canvas = Canvas(root,width = 2000,height = 1000, bg ="purple")

            canvas.pack()


            label_1 = Label(root, text="Username",width=20, bg ="purple",font=("bold", 15))
            label_1.place(x=300,y=390)

            entry_1 = Entry(root)
            entry_1.place(x=490,y=390)

            label_2 = Label(root, text="Password",width=20, bg ="purple",font=("bold", 15))
            label_2.place(x=300,y=430)

            entry_2 = Entry(root)
            entry_2.place(x=490,y=430)

            def run4():

                root.destroy()
                root1 = Tk()
                root1.geometry('1000x1000')
                root1.title("Create an acount")
                root1.resizable(False,False)
                f2 = Frame(root1, borderwidth=8, bg="gold", relief=SUNKEN)


                f2.pack(side=TOP, fill="x")


                l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


                l.pack()


                welcome_text = Label( root1,text = '''Booking''',fg = "gold",bg = "purple",height = 5 , width = 200,font =("Algerian",40,"bold"))    
                welcome_text.pack()

                canvas = Canvas(root1,width = 2000,height = 1000, bg ="purple")

                canvas.pack()

                def run5():

                    root1.destroy()
                    root2 = Tk()
                    root2.geometry('1000x1000')
                    root2.title("Create an acount")
                    root2.resizable(False,False)
                    f2 = Frame(root2, borderwidth=8, bg="gold", relief=SUNKEN)


                    f2.pack(side=TOP, fill="x")


                    l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


                    l.pack()


                    welcome_text = Label( root2,text = '''Booking''',fg = "gold",bg = "purple",height = 5 , width = 200,font =("Algerian",40,"bold"))    
                    welcome_text.pack()

                    canvas = Canvas(root2,width = 2000,height = 1000, bg ="purple")

                    canvas.pack()

                    def run6():

                        root2.destroy()
                        root3 = Tk()
                        root3.geometry('1000x1000')
                        root3.title("Create an acount")
                        root3.resizable(False,False)
                        f2 = Frame(root3, borderwidth=8, bg="gold", relief=SUNKEN)


                        f2.pack(side=TOP, fill="x")


                        l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


                        l.pack()


                        welcome_text = Label( root3,text = '''Restaurant Booking''',fg = "gold",bg = "purple",height = 5 , width = 200,font =("Algerian",40,"bold"))    
                        welcome_text.pack()

                        canvas = Canvas(root3,width = 2000,height = 1000, bg ="purple")

                        canvas.pack()


                    click_me = Button(root2,text = "Restaurant Booking", fg = "red", bg = "orange",height = 1 ,width = 15,font =("Georgia",20,"bold"),command = run1)
                    click_me.place(x = 210,y = 520)

                    click_me = Button(text = "Room Booking", fg = "red", bg = "orange",height = 1 ,width = 15,font =("Georgia",20,"bold"),command = exit)
                    click_me.place(x = 500,y = 520)




                click_me = Button(root1,text = "Booking", fg = "red", bg = "orange",height = 1 ,width = 9,font =("Georgia",20,"bold"),command = run5)
                click_me.place(x = 310,y = 520)

                click_me = Button(text = "Exit", fg = "red", bg = "orange",height = 1 ,width = 9,font =("Georgia",20,"bold"),command = exit)
                click_me.place(x = 500,y = 520)


                            
            Button(root, text='Submit',width=20,bg='brown',fg='white',command = run4).place(x=420,y=530)
            Button(root, text='Back',width=10,bg='brown',fg='white', command = run).place(x=500,y=570)
            Button(root, text='Exit',width=10,bg='brown',fg='white',command = exit).place(x=420,y=570)
            

            root.mainloop()
        click_me = Button(text = "LOGIN", fg = "red", bg = "orange",height = 1 ,width = 9,font =("Georgia",20,"bold"),command = run1)
        click_me.place(x = 310,y = 520)

        def run2():
            screen2.destroy()
            root = Tk()
            root.geometry('1000x1000')
            root.title("Create an acount")
            root.resizable(False,False)
            f2 = Frame(root, borderwidth=8, bg="gold", relief=SUNKEN)


            f2.pack(side=TOP, fill="x")


            l= Label(f2, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


            l.pack()


            welcome_text = Label( text = '''CREATE AN ACCOUNT''',fg = "gold",bg = "purple",height = 5 , width = 200,font =("Algerian",40,"bold"))    
            welcome_text.pack()

            canvas = Canvas(width = 2000,height = 1000, bg ="purple")

            canvas.pack()


            label_1 = Label(root, text="FullName",width=20, bg ="purple",font=("bold", 15))
            label_1.place(x=300,y=390)

            entry_1 = Entry(root)
            entry_1.place(x=490,y=390)

            label_2 = Label(root, text="Email",width=20, bg ="purple",font=("bold", 15))
            label_2.place(x=300,y=430)

            entry_2 = Entry(root)
            entry_2.place(x=490,y=430)

            label_2 = Label(root, text="Phone.no",width=20, bg ="purple",font=("bold", 15))
            label_2.place(x=300,y=470)

            entry_2 = Entry(root)
            entry_2.place(x=490,y=470)

            label_2 = Label(root, text="Address",width=20, bg ="purple",font=("bold", 15))
            label_2.place(x=300,y=510)

            entry_2 = Entry(root)
            entry_2.place(x=490,y=510)

            label_3 = Label(root, text="Gender",width=20, bg ="purple",font=("bold", 15))
            label_3.place(x=300,y=550)
            var = IntVar()
            Radiobutton(root, text="Male",padx = 20, variable=var, value=1, bg ="purple",font=("bold", 15)).place(x=455,y=550)
            Radiobutton(root, text="Female",padx = 20, variable=var, value=2, bg ="purple",font=("bold", 15)).place(x=555,y=550)

            label_4 = Label(root, text="Country",width=20, bg ="purple",font=("bold", 15))
            label_4.place(x=300,y=590)

            list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
            c=StringVar()
            droplist=OptionMenu(root,c, *list1)
            droplist.config(width=20, bg ="purple")
            c.set('select your country') 
            droplist.place(x=490,y=590)

            Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=420,y=630)
            Button(root, text='Back',width=10,bg='brown',fg='white', command = run).place(x=500,y=670)
            Button(root, text='Exit',width=10,bg='brown',fg='white',command = exit).place(x=420,y=670)
            





            root.mainloop()


        click_me = Button(text = "CREATE AN ACCOUNT", fg = "red", bg = "orange",height = 1 ,width = 21,font =("Georgia",20,"bold"),command = run2)
        click_me.place(x = 300,y = 600)

        def run3():
            screen2.destroy()
            screen5= Tk()
            screen5.title("MY FIRST GAMING PROGRAM")
            screen5.geometry("1000x1000")
            screen5.resizable(False,False)
            f3 = Frame(screen5, borderwidth=8, bg="gold", relief=SUNKEN)


            f3.pack(side=TOP, fill="x")


            l= Label(f3, text="ACCESS THE CITY FROM OUR GLAMOROUS : THE HOTEL HAYAT", font="algerian 20 bold",bg="purple",fg="yellow", pady=10)


            l.pack()

            
            welcome_text = Label( text = '''THANK YOU
SIR/MA'AM
FOR APPEARING HERE''',fg = "gold",bg = "purple",height = 5 , width = 500,font =("Algerian",50,"bold"))    
            welcome_text.pack()

            
            canvas = Canvas(width = 2000,height = 1000, bg ="purple")
            canvas.pack()
            click_me = Button(text = "EXIT", fg = "red", bg = "white",height = 1 ,width = 10,font =("Georgia",20,"bold"),command = exit)
            click_me.place(x = 410,y = 600)

            def main1():
                fun= pyttsx3.init()
                fun.say('''THANK YOU       SIR OR MA'AM       FOR APPEARING HERE''')

                fun.runAndWait()

            screen.after(1000,main1)
            screen.after(1000,run3)

            
        click_me = Button(text = "CANCEL", fg = "red", bg = "orange",height = 1 ,width = 9,font =("Georgia",20,"bold"),command = run3)
        click_me.place(x = 500,y = 520)




    click_me = Button(text = "NEXT", fg = "red", bg = "orange",height = 1 ,width = 10,font =("Georgia",20,"bold"),command = run)
    click_me.place(x = 425,y = 550)

    
def main1():
    f= pyttsx3.init()
    f.say('''WELCOME        TO    HOTEL   HAYAT''')

    f.runAndWait()

screen.after(1000,main1)
screen.after(2000,main)




