# specially designed for theodore use
# importing packages for Gui
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
from time import sleep
from timeit import timeit
class Recommender ( tk.Tk ):
    'Class for the Gui'
    def __init__(self , *args , **kwargs):
        'class constructor'
        tk.Tk.__init__ ( self , *args , **kwargs )
        self.title('Recommender System')
        self.resizable(0, 0)
        self.geometry('%dx%d+%d+%d' % (500, 300, 300, 10))
        self.main()
        self.Time_to_run()
    
    def main(self):
        Frame = ttk.LabelFrame(self, text='Dialogue')
        Frame.pack(expand=1, fill='both')

        # creating the entry boxes
        self.vcmd = (self.register (self.validator ) , '%P' , '%d')
        self.vcmd2 = (self.register (self.validator3 ) , '%P' , '%d')
        self.txt1 = tk.Label(Frame, text='Music Id:')
        self.txt1.place(relx=0.01, rely=0.05)
        self.txt2 = tk.Label(Frame, text='Artist Id:')
        self.txt2.place(relx=0.01, rely=0.15)
        
        self.id1 = tk.Entry(Frame, width=26, state='disabled',validate = 'key' , validatecommand = self.vcmd2)
        self.id1.place(relx=0.15, rely=0.05)

        self.id2 = tk.Entry(Frame, width=26, validate = 'key' , validatecommand = self.vcmd, state='disabled')
        self.id2.place(relx= 0.15, rely=0.15)

        # creating the dropdown menu for the metrics
        #tk.Label(Frame, text='Metric:').place(relx=0.58, rely=0.154)
        OPTIONS = ['Cosine','Euclidean','Jaccard','manhattan','pearson']
        self.metric = tk.StringVar()
        self.metric.set(OPTIONS[2]) # default value
        option = tk.OptionMenu(Frame,self.metric, *OPTIONS)
        option.configure(width=13)
        option.place(relx= 0.59, rely=0.14)

        # creating the radiobuttons for choosing the similarites you want to check, either between music id or artists id or artist and music 
        Frame2 = tk.Frame(Frame)
        Frame2.place(relx=0.01, rely=0.25)
        tk.Label(Frame, text='Similarites Between').place(relx=0.01, rely=0.25)
        self.sim_choosen = tk.IntVar()
        similarities_opt = [('Musics', 1),('Artists', 2),("Artist & Musics",3)]
        for similarity, val in similarities_opt:
                tk.Radiobutton(Frame2, 
                                text=similarity,
                                variable=self.sim_choosen,command=self.getter 
                                ,value=val).pack(side='left', pady=20)

        # creating the spinbox that would indicate how many no of similarities do want to see..
        # this would only work if you are trying to only show the n similarity to an artist or music 
        tk.Label(Frame, text='N:').place(relx=0.58, rely=0.05)
        self.N = tk.Spinbox ( Frame , from_ = 1 , to = 100 , width = 15, state='disabled')
        self.N.place(relx= 0.61, rely =0.05)
        

        # creating the calculate button
        button = tk.Button(Frame, text='Calculate Similarity', width=16, command = lambda: [f () for f in [self.validator2]])
        button.place(relx = 0.50, rely=0.30)

        # creating the evalution button
        self.eval_button = tk.Button(Frame, text='Evaluation', width=10, state='disabled', command=self.evaluate)
        self.eval_button.place(relx = 0.80, rely=0.30)
        
        # progress bar
        self.progress_Bar = ttk.Progressbar(Frame, orient='horizontal', length=495, mode='determinate')
        self.progress_Bar.place(relx=0.00, rely=0.53)
        self.tips = tk.Label(Frame, text='Tips!!')
        self.tips.place(relx = 0.45, rely=0.44)
        
        # result panel
        tk.Label(Frame, text='Results').place(relx = 0.01, rely=0.62)
        tk.Label(Frame, text='Similarity Score:').place(relx=0.03, rely=0.72)

        self.Score = tk.Label(Frame, text='')
        self.Score.place(relx=0.25, rely=0.72)

        # creating the text area for displaying results
        Frame2 = tk.Frame(Frame)
        Frame2.place(relx=0.50, rely=0.62)
        h = tk.Scrollbar(Frame2, orient = 'horizontal')
        h.pack(side ='bottom', fill = 'x') 
        v = tk.Scrollbar(Frame2)
        v.pack(side = 'right', fill = 'y')
        self.t = tk.Text(Frame2, width = 33, height = 7.4,xscrollcommand = h.set,  
                 yscrollcommand = v.set, state='normal')
        self.t.pack(side='top')
        h.config(command=self.t.xview)
        v.config(command=self.t.yview)
    
    def validator(self, e, Type):
        'validating the entries given'
        if Type == '1':
            if e == '':
                self.N.configure(state ='normal')
                return True
            elif e != None:
                self.N.configure(from_ = 0 , to = 100)
                self.N.configure(state ='disabled')
        elif Type == '0':
            if e == '':
                self.N.configure(state ='normal')
        return True
    
    def validator3(self, e, Type):
        'validating the entries given'
        if Type == '1':
            if e == '':
                self.N.configure(state ='readonly')
                return True
            elif e != None:
                self.N.configure(state ='readonly')
        elif Type == '0':
            if e == '':
                self.N.configure(state ='disabled')
        return True

    def calculate(self):
        'callback that is called when you press calculate button'
        self.t.configure(state='normal')
        self.t.delete("1.0","end")
        self.t.insert('end','{}\t{}\n'.format(self.id1.get(), self.id2.get()))
        self.t.insert('end', 'metric:\t{}\n'.format(self.metric.get()))
        self.t.insert('end','N: {}\n'.format(self.N.get()))
        self.t.insert('end','option {}\n'.format(self.sim_choosen.get()))
        self.t.insert
        self.t.configure(state='disabled')
        self.ProgressBar()
        self.eval_button.configure(state='normal')

    
    def evaluate(self):
        'callback for the evaluation button'
        self.eval_button.configure(state='disabled')
    
    def getter(self):
        'this changes the text for the entries depending on the similarity radiobutton choosen'
        if self.sim_choosen.get() == 1:
            self.txt1.configure(text='Music id 1')
            self.txt2.configure(text='Music id 2')
            self.id1.configure(state='normal')
            self.id2.configure(state='normal')
        elif self.sim_choosen.get() == 2:
            self.txt1.configure(text='Artist id 1')
            self.txt2.configure(text='Artist id 2')
            self.id1.configure(state='normal')
            self.id2.configure(state='normal')
        elif self.sim_choosen.get() == 3:
            self.txt1.configure(text='Artist id 1')
            self.txt2.configure(text='')
            self.id1.configure(state='normal')
            self.id2.configure(state='disabled')
        else:
            pass 

    def validator2(self):
        'use this with the calculate button'
        try:
            if self.id1.get() == '':
                msg.showerror('Error', 'You cant give a value for a N when finding just the similarities between two artist or music')
            else:
                self.calculate()        
        except Exception:
            msg.showerror('Error', 'You cant give a value for a N when finding just the similarities between two artist or music')

    def ProgressBar(self):
        'This is the callback for the progress bar'
        self.progress_Bar['maximum'] = 100
        for i  in range(100):
            sleep(self.time_taken/100)
            self.progress_Bar['value'] = i
            self.progress_Bar.update()
            self. progress_Bar['value'] = 0
        self.tips.configure(text='Completed')
    
    def Time_to_run(self):
        'calculates the total time the code takes to run, uses it in the progress bar'
        Code_to_test ="""def calculate(self):
        print(self.variable.get())
        print(self.sim_choosen.get())
        print(self.N.get())
        print(self.id1.get(), self.id2.get())"""
        self.time_taken = timeit(Code_to_test)



Recommender().mainloop()