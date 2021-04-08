# importing packages
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

root = tk.Tk() # the main window frame
root.title('Recommender System')
root.resizable(0, 0)
root.title('Recommender system') 
root.geometry('%dx%d+%d+%d' % (500, 300, 300, 10))

Frame = ttk.Frame(root)
Frame.pack(expand=1, fill='both')

def calculate():
    #print(id1.get(),id2.get())
    print(variable.get())
    print(sim_choosen.get())
    print(N.get())
    print(id1.get(), id2.get())

def validator(e, Type):
    'validating the entries given'
    if Type == '1':
        if not e.isdigit ():
            self.bell ()
            return False
        if e == '0':
            self.bell ()
            return False
    return True


# creating the entry boxes
vcmd = (tk.register (validator ) , '%P' , '%d')
tk.Label(Frame, text='Music Id:').place(relx=0.01, rely=0.15)
tk.Label(Frame, text='Artist Id:').place(relx=0.01, rely=0.25)
id1 = tk.Entry(Frame, width=26)
id1.place(relx=0.15, rely=0.15, validate = 'key' , validatecommand = vcmd)
id2 = tk.Entry(Frame, width=26)
id2.place(relx= 0.15, rely=0.25)

# creating the dropdown menu for the metrics
tk.Label(Frame, text='Metric:').place(relx=0.01, rely=0.58)
OPTIONS = ['Cosine','Euclidean','Jaccard','manhattan','pearson']
variable = tk.StringVar()
variable.set(OPTIONS[2]) # default value
option = tk.OptionMenu(Frame,variable, *OPTIONS)
option.place(relx= 0.15, rely=0.56)

# creating the radiobuttons for choosing the similarites you want to check, either between music id or artists id or artist and music 
tk.Label(Frame, text='Similarites Between').place(relx=0.01, rely=0.38)
sim_choosen = tk.IntVar()
similarities_opt = [('Musics', 1),('Artists', 2),("Artist & Musics",3)]
for similarity, val in similarities_opt:
    tk.Radiobutton(Frame, 
                   text=similarity,
                   variable=sim_choosen, 
                   value=val).pack(side='left')

# creating the spinbox that would indicate how many no of similarities do want to see..
# this would only work if you are trying to only show the n similarity to an artist or music 
tk.Label(Frame, text='N').place(relx=0.01, rely=0.68)
N = tk.Spinbox ( Frame , from_ = 0 , to = 100 , width = 15, state='disabled' )
N.place(relx= 0.08, rely =0.68)

# creating the calculate button
button = tk.Button(Frame, text='Calculate Similarity', width=20, command=calculate)
button.place(relx = 0.10, rely=0.78)

while id2.get() == None:
    N.state = tk.DISABLED
root.mainloop()