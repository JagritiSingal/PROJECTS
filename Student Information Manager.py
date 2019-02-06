from tkinter import *
from tkinter import messagebox
import pandas
import statistics
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MyInterface:

    LABEL_TEXT = ['This is the Interface package.',
                  'This is the main class for GUI,']

    def __init__(self, master):
        self.master = master
        master.title('Student Validator')
        master.attributes('-fullscreen', True) #for full Screen Window
        #master.geometry("500x700")

        # Declaration of Variables used in  Entry Widget
        self.Roll_No = StringVar()
        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.Phone_Number = StringVar()
        self.Department = StringVar()
        self.Email_Id = StringVar()
        self.Python_Marks = StringVar()
        self.DS_Marks = StringVar()
        self.ADBMS_Marks = StringVar()
        self.Total_Marks = StringVar()
        self.Search_Roll_No = StringVar()
        self.Drop_Down = StringVar()
        self.body()

    #Fuction for labels,entry_box and buttons
    def body(self):

        # Label
        top_bar = Frame(bg = "#465454", width="1366", height="56").place(x=0, y=0)
        top_lab = Label(self.master, text='Student Information Statistics', anchor=W, font=200,
                     width=24).place(x=560, y=15)

        #border = Frame(bg = "#465454", width="3", height="700").place(x=580, y=56)

        bottom_bar = Frame(bg = "#465454", width="1366", height="20").place(x=0, y=747)

        lab1 = Label(self.master, text='Roll No', anchor=W, font=55,
                     width=15).place(x=60, y=100)
        lab2 = Label(self.master, text='First Name', anchor=W, font=55,
                     width=15).place(x=60, y=140)
        lab3 = Label(self.master, text='Last Name', anchor=W, font=55,
                     width=15).place(x=60, y=180)
        lab4 = Label(self.master, text='Phone Number', anchor=W,
                     font=55, width=12).place(x=60, y=220)
        lab5 = Label(self.master, text='Department', anchor=W, font=55,
                     width=15).place(x=60, y=260)
        lab6 = Label(self.master, text='Email Id', anchor=W, font=55,
                     width=15).place(x=60, y=300)
        lab7 = Label(self.master, text='Python Marks', anchor=W,
                     font=55, width=15).place(x=60, y=340)
        lab8 = Label(self.master, text='DS Marks', anchor=W, font=55,
                     width=15).place(x=60, y=380)
        lab9 = Label(self.master, text='ADBMS Marks', anchor=W,
                     font=55, width=15).place(x=60, y=420)

        Search_lab = Label(self.master, text='Search :', anchor=W,
                     font=55, width=15).place(x=60, y=580)
        
        Python_lab = Label(self.master, text='Python', anchor=W,
                     font=70, width=15).place(x=870, y=100)
        DS_lab = Label(self.master, text='DS', anchor=W,
                     font=70, width=15).place(x=980, y=100)
        ADBMS_lab = Label(self.master, text='ADBMS', anchor=W,
                     font=70, width=15).place(x=1060, y=100)

        # Entry

        ent1 = Entry(self.master, textvariable=self.Roll_No,
                     width=30).place(x=250, y=100)
        ent2 = Entry(self.master, textvariable=self.First_Name,
                     width=30).place(x=250, y=140)
        ent3 = Entry(self.master, textvariable=self.Last_Name,
                     width=30).place(x=250, y=180)
        ent4 = Entry(self.master, textvariable=self.Phone_Number,
                     width=30).place(x=250, y=220)
        ent5 = Entry(self.master, textvariable=self.Department,
                     width=30).place(x=250, y=260)
        ent6 = Entry(self.master, textvariable=self.Email_Id,
                     width=30).place(x=250, y=300)
        ent7 = Entry(self.master, textvariable=self.Python_Marks,
                     width=30).place(x=250, y=340)
        ent8 = Entry(self.master, textvariable=self.DS_Marks,
                     width=30).place(x=250, y=380)
        ent9 = Entry(self.master, textvariable=self.ADBMS_Marks,
                     width=30).place(x=250, y=420)

        search_ent = Entry(self.master, textvariable=self.Search_Roll_No,
                     width=62).place(x = 60, y=625)

        # Button
        exit_button = Button(self.master, text='Exit', width=15, height=3)
        exit_button.place(x =1250 ,y = 0)
        exit_button.bind('<Button-1>', self.closeGUI)


        reset_button = Button(self.master, text='Reset', width=15, height=3)
        reset_button.place(x = 80 ,y = 480)
        reset_button.bind('<Button-1>', self.resetEntry)

        save_button = Button(self.master, text='Save', width=15, height=3)
        save_button.place(x = 280 ,y = 480)
        save_button.bind('<ButtonRelease-1>', self.saveEntry)

        search_button = Button(self.master, text='Search', width=15, height=3)
        search_button.place(x = 180 ,y = 670)
        search_button.bind('<ButtonRelease-1>', self.search)



        total_button = Button(self.master, text='Total', width=15, height=3)
        total_button.place(x = 650, y = 150)
        total_button.bind('<Button-1>', self.total)

        average_button = Button(self.master, text='Average', width=15, height=3)
        average_button.place(x = 650, y = 220)
        average_button.bind('<Button-1>', self.average)

        max_button = Button(self.master, text='Max', width=15, height=3)
        max_button.place(x = 650, y = 290)
        max_button.bind('<Button-1>', self.maximum)

        min_button = Button(self.master, text='Min', width=15, height=3)
        min_button.place(x = 650, y = 360)
        min_button.bind('<Button-1>', self.minimum)

        median_button = Button(self.master, text='Median', width=15, height=3)
        median_button.place(x = 650, y = 360+70)
        median_button.bind('<Button-1>', self.median)

        mode_button = Button(self.master, text='Mode', width=15, height=3)
        mode_button.place(x = 650, y = 360+140)
        mode_button.bind('<Button-1>', self.mode)

        stat_button = Button(self.master,text="Graphs and Statistics", width=40, height=4)
        stat_button.place(x = 850, y  = 630)
        stat_button.bind("<Button-1>", self.statistics)
        

    #Closing the GUI window
    def closeGUI(self, event):
        self.master.destroy()
        
    #If the user leave any entry box empty
    def authenticateEntry(self, event):
        if self.Roll_No.get() == '' or self.First_Name.get() == '' \
            or self.Last_Name.get() == '' or self.Phone_Number.get() \
            == '' or self.Department.get() == '' \
            or self.Email_Id.get() == '' or self.Python_Marks.get() \
            == '' or self.DS_Marks.get() == '' \
            or self.ADBMS_Marks.get() == '':
            messagebox.showerror('Error!','You can not leave any field empty!')
            return 0
        else:
            return 1
    
    #Searching the record of any Student and displaying the details
    def search(self, event):
        if(self.Search_Roll_No.get() == ''):
            messagebox.showerror('Error!','Please Enter Roll No')
        else:
            df = pandas.DataFrame(pandas.read_csv('demo.csv'))
            abc = 'Roll_No ==' + self.Search_Roll_No.get()
            file = df.query(abc)
            if(file.empty):
                messagebox.showerror('Error!','Entry not found! Please Enter again')
            else:
                root1 = Tk()
                root1.title("Search Record")
                root1.geometry("1200x700")
            
                lab01 = Label(root1, text='Roll No', anchor=W, font=55,
                         width=15).place(x=60, y=100)
                lab02 = Label(root1, text='First Name', anchor=W, font=55,
                         width=15).place(x=60, y=140)
                lab03 = Label(root1, text='Last Name', anchor=W, font=55,
                         width=15).place(x=60, y=180)
                lab04 = Label(root1, text='Phone Number', anchor=W,
                         font=55, width=12).place(x=60, y=220)
                lab05 = Label(root1, text='Department', anchor=W, font=55,
                         width=15).place(x=60, y=260)
                lab06 = Label(root1, text='Email Id', anchor=W, font=55,
                         width=15).place(x=60, y=300)
                lab07 = Label(root1, text='Python Marks', anchor=W,
                         font=55, width=15).place(x=60, y=340)
                lab08 = Label(root1, text='DS Marks', anchor=W, font=55,
                         width=15).place(x=60, y=380)
                lab09 = Label(root1, text='ADBMS Marks', anchor=W,
                         font=55, width=15).place(x=60, y=420)
                lab010 = Label(root1, text='Percentage', anchor=W,
                         font=55, width=15).place(x=60, y=460)
            
                file1 = list(file.values.flatten())
                temp = sum(file1[6:])/3
                percent = str(round(temp, 2)) + ' %'

                lab11 = Label(root1, text=int(file1[0]), anchor=W, font=55,
                     width=15).place(x=250, y=100)
                lab12 = Label(root1, text=file1[1], anchor=W, font=55,
                     width=15).place(x=250, y=140)
                lab13 = Label(root1, text=file1[2], anchor=W, font=55,
                     width=15).place(x=250, y=180)
                lab14 = Label(root1, text=int(file1[3]), anchor=W,
                     font=55, width=12).place(x=250, y=220)
                lab15 = Label(root1, text=file1[4], anchor=W, font=55,
                        width=15).place(x=250, y=260)
                lab16 = Label(root1, text=file1[5], anchor=W, font=55,
                     width=25).place(x=250, y=300)
                lab17 = Label(root1, text=file1[6], anchor=W,
                     font=55, width=15).place(x=250, y=340)
                lab18 = Label(root1, text=file1[7], anchor=W, font=55,
                     width=15).place(x=250, y=380)
                lab19 = Label(root1, text=file1[8], anchor=W,
                     font=55, width=15).place(x=250, y=420)
                lab010 = Label(root1, text=percent, anchor=W,
                     font=55, width=15).place(x=250, y=460)

                #Bar graph of the student comparing max_marks,student's_marks,avg_marks in each subject
                col_count = 3
                bar_width = .2
                
                max1 = self.stat_values('max')
                mark = file1[6:]
                avg1 = self.stat_values('average')
                
                index=np.arange(col_count)
                
                f = Figure(figsize=(6, 5), dpi=100)
                a = f.add_subplot(111)
                m1=a.bar(index,max1,bar_width,alpha=.4,label="Max")
                m2=a.bar(index+0.2,mark,bar_width,alpha=.4,label="Marks")
                m3=a.bar(index+0.4,avg1,bar_width,alpha=.4,label="Average")

                
                def CreateLabels(data):
                    for i in data:
                        height=i.get_height()
                        a.text(i.get_x() + i.get_width() / 2., height*1, '%d' % int(height), ha='center',va='bottom')
                        
                CreateLabels(m1)
                CreateLabels(m2)
                CreateLabels(m3)
                a.set_xticks(index + .3/2)
                a.set_xticklabels(('Python','DS','ADBMS'))
                a.set_xlabel('Subjects')
                a.set_ylabel('Marks')
                a.set_title('Comparision between Max_Marks,Student_Marks,Average_Marks')
                a.legend()
                a.grid(True)
                canvas = FigureCanvasTkAgg(f, master=root1)
                canvas.get_tk_widget().place(x =500 ,y = 100)
                root1.mainloop()
                
    #Function to check for duplicate values in the csv file
    def checkForDuplicate(self, event):
        row = StringVar()
        file = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                columns=['Roll_No'])
        roll = list(file.values.T.flatten())
        for row in roll:
            if row == int(self.Roll_No.get()):
                messagebox.showerror('Error!','Redundancy Found!')
                return 0

        return 1
    
    #Function to reset the Entry boxes
    def resetEntry(self,event):
        self.Roll_No.set('') 
        self.First_Name.set('')
        self.Last_Name.set('')
        self.Phone_Number.set('')
        self.Department.set('')
        self.Email_Id.set('')
        self.Python_Marks.set('')
        self.DS_Marks.set('')
        self.ADBMS_Marks.set('')
        
    #Function to save the data in csv file
    def saveEntry(self, event):
        if self.authenticateEntry(event) == 1 \
            and self.checkForDuplicate(event) == 1:

            msg = messagebox.askyesno('Check',
                    'Do you want to save?')
            print (msg)

            data = [[
                self.Roll_No.get(),
                self.First_Name.get(),
                self.Last_Name.get(),
                self.Phone_Number.get(),
                self.Department.get(),
                self.Email_Id.get(),
                self.Python_Marks.get(),
                self.DS_Marks.get(),
                self.ADBMS_Marks.get(),
                ]]

            df = pandas.DataFrame(data, columns=[
                'Roll_No',
                'First_Name',
                'Last_Name',
                'Phone_Number',
                'Department',
                'Email_Id',
                'Python_Marks',
                'DS_Marks',
                'ADBMS_Marks',
                ])

            df.to_csv('demo.csv', mode='a', index=False, header=False)
            self.resetEntry(self)
        else:
            print ('No')

    

    
    #Function to display Pie Charts
    def pie_graph(self, file, text):
        count1 = count2 = 0
        pass1 = fail1 = 0
        for i in file:
            if i >= 33:
                pass1 += 1
            else:
                fail1 += 1
        per1 = int(pass1 * 100 / (pass1 + fail1))
        per2 = int(fail1 * 100 / (pass1 + fail1))
        
        labels = 'Pass','Fail'
        sizes = [per1,per2]
        seperated = [0,.1]
        f = Figure(figsize=(3, 3), dpi=85)
        a = f.add_subplot(111)
        a.set_title(text)
        a.pie(sizes,labels=labels,autopct='%1.1f%%',
              colors=[(152/255,251/255,152/255),(147/255,112/255,219/255)],shadow=True,explode=seperated)
        return f
    
    #Function to display Line Graphs
    def line_graph(self, file1,file2,file3,text):
        x=[10,20,30,40,50,60,70,80,90,100]
        u1 = pandas.unique(file1)
        u2 = pandas.unique(file2)
        u3 = pandas.unique(file3)
        s1 = pandas.Series(u1)
        s2 = pandas.Series(u2)
        s3 = pandas.Series(u3)
        top1 = s1.nlargest(10).values.flatten()
        top2 = s2.nlargest(10).values.flatten()
        top3 = s3.nlargest(10).values.flatten()
        bottom1 = s1.nsmallest(10).values.flatten()
        bottom2 = s2.nsmallest(10).values.flatten()
        bottom3 = s3.nsmallest(10).values.flatten()
        f = Figure(figsize=(7, 4), dpi=90)
        a = f.add_subplot(111)
        a.plot(x,top1,marker='4',label='python top 10')
        a.plot(x,top2,marker='4',label='ds top 10')
        a.plot(x,top3,marker='4',label='adbms top 10')
        a.plot(x,bottom1,marker='4',label='python bottom 10')
        a.plot(x,bottom2,marker='4',label='ds bottom 10')
        a.plot(x,bottom3,marker='4',label='adbms bottom 10')
        legend = a.legend(loc='best', shadow=True, fontsize='small',frameon=True)
        a.set_xlabel('Marks')
        a.grid(True)
        a.set_title(text)
        return f
    
    #Function to display Scatter Plot Graph
    def scatter_plot(self):
        df = pandas.DataFrame(pandas.read_csv("demo.csv"), columns = ['Roll_No','Python_Marks','DS_Marks','ADBMS_Marks'])
        df['total']=df['Python_Marks']+df['DS_Marks']+df['ADBMS_Marks']
        
        f = Figure(figsize=(7, 4), dpi=70)
        a = f.add_subplot(111)
        a.set_title('Scatter Plot of Roll_No vs \nTotal Marks of each Student')
        a.set_xlabel('Roll_No')
        a.set_ylabel('Total Marks')
        a.scatter(df['Roll_No'],df['total'],alpha=0.5)
        a.grid(True)
        return f
    
    #Function to display Bar Graph       
    def bar_graph(self,text):
        col_count = 3
        bar_width = .2
        mean = self.stat_values('average')
        median = self.stat_values('median')
        mode = self.stat_values('mode')
                
        index = np.arange(col_count)
                
        f = Figure(figsize=(8, 4), dpi=90)
        a = f.add_subplot(111)
        m1 = a.bar(index, mean, bar_width, alpha=.4, label="Mean")
        m2 = a.bar(index + 0.2, median,bar_width, alpha=.4, label="Median")
        m3 = a.bar(index + 0.4, mode,bar_width, alpha=.4, label="Mode")
    
        def CreateLabels(data):
            for i in data:
                height=i.get_height()
                a.text(i.get_x() + i.get_width() / 2., height*1, '%d' % int(height), ha='center',va='bottom')
 
        CreateLabels(m1)
        CreateLabels(m2)
        CreateLabels(m3)
        a.set_xticks(index + .3/2)
        a.set_xticklabels(('Python','DS','ADBMS'))
        a.legend()
        a.set_xlabel('Subjects')
        a.set_title(text)
        a.grid(True)
        return f
    
    #Function to display Various Graphs in other GUI window
    def graph_plot(self, f1, f2, f3, f4, f5, f6):
        graph = Tk()
        graph.title("Graphs and Statistics")
        graph.geometry('1300x800')
        graph.configure(background='#ffffff')
        canvas = FigureCanvasTkAgg(f1, master=graph)
        canvas.get_tk_widget().place(x = 20, y = 20 )
        canvas = FigureCanvasTkAgg(f2, master=graph)
        canvas.get_tk_widget().place(x = 280, y = 20)
        canvas = FigureCanvasTkAgg(f3, master=graph)
        canvas.get_tk_widget().place(x = 560, y = 20)
        canvas = FigureCanvasTkAgg(f4, master=graph)
        canvas.get_tk_widget().place(x = 580+260, y = 20)
        canvas = FigureCanvasTkAgg(f5, master=graph)
        canvas.get_tk_widget().place(x = 20, y = 315)
        canvas = FigureCanvasTkAgg(f6, master=graph)
        canvas.get_tk_widget().place(x = 620, y = 315)
        graph.mainloop()
        

    def statistics(self, event):
        file1 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['Python_Marks']).values.T.flatten()
        file2 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['DS_Marks']).values.T.flatten()
        file3 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['ADBMS_Marks']).values.T.flatten()

        f1 = self.pie_graph(file1, 'Python')
        f2 = self.pie_graph(file2, 'DS')
        f3 = self.pie_graph(file3, 'ADBMS')
        f4 = self.scatter_plot()
        f5 = self.line_graph(file1, file2, file3,'Top 10 and Bottom 10 Marks in each subject')
        f6 = self.bar_graph('Mean,Median,Mode in each Subject')


        self.graph_plot(f1, f2, f3, f4, f5, f6)
            

    #Function to calculate various opertions such as total,average,median,mode,maximum,minimum
    def stat_values(self, data):
        file1 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['Python_Marks'])  
        file2 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['DS_Marks'])  
        file3 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['ADBMS_Marks'])  

        list1 = file1.values.T.flatten()
        list2 = file2.values.T.flatten()
        list3 = file3.values.T.flatten()

        if(data == 'max'):
            max1 = file1.values.max()
            max2 = file2.values.max()
            max3 = file3.values.max()
            return [max1, max2, max3]
        
        elif(data == 'min'):
            min1 = file1.values.min()
            min2 = file2.values.min()
            min3 = file3.values.min()
            return [min1, min2, min3]
        
        elif(data == 'median'):
            median1 = statistics.median(list1)
            median2 = statistics.median(list2)
            median3 = statistics.median(list3)
            return [median1, median2, median3]
        
        elif(data == 'mode'):
            mode1 = statistics.mode(list1)
            mode2 = statistics.mode(list2)
            mode3 = statistics.mode(list3)
            return [mode1, mode2, mode3]
        
        elif(data == 'total'):
            sum1 = file1.values.sum()
            sum2 = file2.values.sum()
            sum3 = file3.values.sum()
            return [sum1, sum2, sum3]
        
        elif(data == 'average'):
            mean1 = round(file1.values.mean(), 2)
            mean2 = round(file2.values.mean(), 2)
            mean3 = round(file3.values.mean(), 2)
            return [mean1, mean2, mean3]
        
        else:
            print('No Function Found')
            

    def total(self, event):
        sum1 = self.stat_values('total')

        python_total = Label(self.master, text=sum1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=150)
        ds_total = Label(self.master, text=sum1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=150)
        adbms_total = Label(self.master, text=sum1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=150)

    def average(self, event):
        mean1 = self.stat_values('average')

        python_avg = Label(self.master, text=mean1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=220)
        ds_avg = Label(self.master, text=mean1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=220)
        adbms_avg = Label(self.master, text=mean1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=220)


    def maximum(self, event):
        max1 = self.stat_values('max') 
        python_max = Label(self.master, text=max1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=290)
        ds_max = Label(self.master, text=max1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=290)
        adbms_max = Label(self.master, text=max1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=290)


    def minimum(self, event):
        min1 = self.stat_values('min') 

        python_min = Label(self.master, text=min1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360)
        ds_min = Label(self.master, text=min1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360)
        adbms_min = Label(self.master, text=min1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360)

    def median(self, event):
        median1 = self.stat_values('median')

        python_med = Label(self.master, text=median1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360+70)
        ds_med = Label(self.master, text=median1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360+70)
        adbms_med = Label(self.master, text=median1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360+70)

    def mode(self, event):
        mode1 = self.stat_values('mode')
 

        python_mode = Label(self.master, text=mode1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360+140)
        ds_mode = Label(self.master, text=mode1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360+140)
        adbms_mode = Label(self.master, text=mode1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360+140)


root = Tk() #Tkinter Window
obj = MyInterface(root)
root.mainloop()
