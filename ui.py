import tkinter as tk
from tkinter import ttk
import os
import _thread
from AliceCore import *

learning_rate=0.001
epochs=int(10E3)

LARGE_FONT= ("Helvetica", 12)

class mainframe(tk.Tk):

	def __init__(self, *args, **kwargs):
	
		tk.Tk.__init__(self, *args, **kwargs)

	       # tk.Tk.iconbitmap(self, default="clienticon.ico")
		tk.Tk.wm_title(self, "ALICE CORE Main Frame")
	
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		container.configure(background='white')

		self.frames = {}

		for F in (StartPage, cores, Kernel_Matrix, Alice):

		    frame = F(container, self)

		    self.frames[F] = frame

		    frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

	
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="MainFrame", font=LARGE_FONT)
		label.pack()

		button = ttk.Button(self, text="Cores",
				    command=lambda: controller.show_frame(cores))
		button.pack()

		button2 = ttk.Button(self, text="Kernel Matrix",
				    command=lambda: controller.show_frame(Kernel_Matrix))
		button2.pack()

		start_mainframe = ttk.Button(self, text="Wake up Alice ?",
				    command=lambda: controller.show_frame(Alice))

		start_mainframe.pack()

class cores(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Cores Analysis", font=LARGE_FONT)
		label.pack()

		home = ttk.Button(self, text="Back to Home",
				    command=lambda: controller.show_frame(StartPage))
		home.pack(side='top', anchor='w')
		


class Kernel_Matrix(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Kernel Matrix Analysis", font=LARGE_FONT)
		label.pack()

		home = ttk.Button(self, text="Back to Home",
				    command=lambda: controller.show_frame(StartPage))
		home.pack(side='top', anchor='w')

class Alice(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Alice MainFrame", font=LARGE_FONT)
		label.pack()

		wake_up = tk.Button(self, text="Wake Up Alice", 
				    command=lambda: _thread.start_new_thread( AliceCore.begin, (learning_rate,epochs) ) )
		wake_up.pack() 

		get = tk.Button(self, text="get Alice data", 
				    command=lambda: _thread.start_new_thread( AliceCore.evaluate_data, ('not', [1])))
		get.pack()

		home = tk.Button(self, text="Back to Home",
				    command=lambda: controller.show_frame(StartPage))
		home.pack(side='top', anchor='w')



mainframe_app = mainframe()
mainframe_app.minsize(600,500)
mainframe_app.mainloop()
