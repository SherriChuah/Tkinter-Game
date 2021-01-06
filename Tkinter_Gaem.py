from tkinter import Frame, Tk, Label, Button, Canvas, Text, messagebox, END, PhotoImage
import random
import time
from operator import itemgetter


class Game(Tk):
	def __init__(self, *args, **kwargs):
		'''Initialise standard Frame for other pages in game'''
		Tk.__init__(self, *args, **kwargs)
		self.title("My Game")
		self.geometry("1536x864")		
		self.resizable(0,0)
		self.frames = {}

		# custom keys
		self.custom_up = 'Up'

		container = Frame(self)
		container.pack_propagate(0)
		container.pack(fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)	
		# different frames for game
		for F in (SPage, RPage, MainPage, GamePage, IPage, LPage, QPage, StartPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			frame.config(bg='orangered4')
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		#####CHANGE THIS BACK REMEMBER############
		self.show("StartPage")

	def show(self, page_name):
		''' Show the frame for the page_name '''
		frame = self.frames[page_name]
		frame.tkraise()

		frame.event_generate("<<ShowFrame>>")

	def get_page(self, classname):
		'''Return the page with classname as its name'''
		return self.frames[classname]


class StartPage(Frame):
	'''Introduction Page Before Main Page'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller 

		label = Label(self, text="Greetings....", fg='antiquewhite3', bg='orangered4', font=("Fixedsys",70))
		label.place(rely=0.3, relx=0.5, anchor='n')
		text = """
		You Have Been Chosen To 
		Play My Game Without Choice
		"""
		label = Label(self, text=text, fg='antiquewhite3', bg='orangered4', font=("Fixedsys",40), justify='center')
		label.place(rely=0.5, relx=0.32, anchor='n')
		
		# Delete widgets to put new ones to continue with introduction
		self.after(3000, self.clear)
		self.after(3000, self.display)
		self.after(5500, lambda: controller.show("MainPage"))

	def clear(self):
		'''Remove All labels in Frame'''
		for child in self.winfo_children():
			child.destroy()

	def display(self):
		art = """
		_____________________8888888888_______________________
		_______________8888888________8888888_________________ 
		___________8888____________________8888_______________ 
		__________888__________888888___________888___________ 
		________88______88888888888888888888______888_________ 
		______888____88888888888888888888888888_____88________ 
		_____88_____88888888888888888888888888888____88_______ 
		____888___888888888888888888888888888888888___888_____ 
		__8888___88888888888888888888888888888888888___8888___ 
		_88888__888888888888888888888888888888888888___88888__ 
		_88888__8888888888____8888888888___88888888888__88888_ 
		_88888_88888888888____888888888____888888888888_88888_ 
		_88888_88888888888____888888888____888888888888_88888_ 
		_88888_888888888888888888888888888888888888888__88888_
		_88888_888888888888888888888888888888888888888__88888_
		_88888__8888__8888888888888888888888888_888888__88888_
		_88888__888888_8888888888888888888888__888888___88888_ 
		___8_____8888888__8888888888888888___8888888______8___ 
		__________8888888888____________8888888888____________ 
		____________88888888888888888888888888888_____________
		______________8888888888888888888888888_______________ 
		_________________8888888888888888888__________________
		"""
		label = Label(self, text=art, bg='orangered4', fg='antiquewhite3', font=("Fixedsys",16))
		label.place(rely=0.08, relx=0.45, anchor='n')
		label = Label(self, text="HAVE FUN!", bg='orangered4', fg='antiquewhite3', font=("Fixedsys",60))
		label.place(rely=0.78, relx=0.5, anchor='n')
		self.after(2500, self.clear)


class MainPage(Frame):
	'''Main Page of the Game where Play, Instruction, Leaderboards buttons are'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.add_image()

		# create buttons that connects to other frames and place them
		play = Button(self, text="PLAY", fg="black", bg='darkolivegreen4', font=("Fixedsys",40), command=lambda: self.check_resume())
		instruction = Button(self, text="INSTRUCTION", fg="black", bg='dark goldenrod', font=("Fixedsys",40), command=lambda: controller.show("IPage"))
		leaderboard = Button(self, text="LEADERBOARD", fg="black", bg='dark khaki', font=("Fixedsys",40), command=lambda: controller.show("LPage"))
		quit = Button(self, text="QUIT", fg="black", bg='sienna3', font=("Fixedsys",40), command=lambda: controller.show("QPage"))
		setting = Button(self, text="SETTINGS", fg="black", bg='bisque3', font=("Fixedsys",40), command=lambda: controller.show("SPage"))

		play.place(rely=0.35, relx=0.5, anchor='center')
		instruction.place(rely=0.48, relx=0.5, anchor='center')		
		leaderboard.place(rely=0.61, relx=0.5, anchor='center')		
		quit.place(rely=1.0, relx=0.0, anchor='sw')
		setting.place(rely=0.0, relx=0.0, anchor='nw')

	def add_image(self):
		# add image to frame
		self.virus = PhotoImage(file='virus.png').zoom(2,2)
		l_virus = Label(self, image=self.virus, bg='orangered4', height=800, width=800)
		l_virus.place(rely=0.5, relx=0.5, anchor='center')

		self.virus1 = PhotoImage(file='virus.png').subsample(2)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.4, relx=0.05, anchor='w')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.3, relx=0.9, anchor='e')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.9, relx=0, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.7, relx=1, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.9, relx=0.75, anchor='center')

		self.virus3 = PhotoImage(file='virus.png').subsample(5)
		l_virus = Label(self, image=self.virus3, bg='orangered4', height=100, width=100)
		l_virus.place(rely=0.65, relx=0.2, anchor='center')

		l_virus = Label(self, image=self.virus3, bg='orangered4', height=100, width=100)
		l_virus.place(rely=0.1, relx=0.7, anchor='center')

		l_virus = Label(self, image=self.virus3, bg='orangered4', height=100, width=100)
		l_virus.place(rely=0.05, relx=0.25, anchor='center')

	def check_resume(self):
		'''check to see if resume or not to resume'''
		if self.controller.get_page("GamePage").is_save == True:
			self.controller.show("GamePage")
		else:
			self.controller.show("RPage")	


class RPage(Frame):
	'''Register User name for the game'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.add_image()

		name = Label(self, text="NAME", fg="antiquewhite3", bg='orangered4', font=("Fixedsys",60))
		name.place(rely=0.35, relx=0.5, anchor='center')
		self.inputbox = Text(self, width=10, height=1, font=("Fixedsys",40))
		self.inputbox.place(rely=0.45, relx=0.5, anchor='center')

		# back and ready button
		back = Button(self, text="BACK", fg="black", bg='yellow4', font=("Fixedsys",40), command=lambda: controller.show("MainPage")) #to main page
		ready = Button(self, text="READY", fg="black", bg='salmon3', font=("Fixedsys",40), command= lambda: self.validate_name(self.inputbox))
		back.place(rely=0.58, relx=0.43, anchor='center')
		ready.place(rely=0.58, relx=0.57, anchor='center')

	def validate_name(self, inputbox):
		# ensure user does not leave the input box empty
		name = inputbox.get("1.0", 'end-1c')

		if name == "":
			warn = Label(self, text="Error: Name cannot be empty!", bg='orangered4', font=("Fixedsys",10), fg="Red")
			warn.place(rely=0.65, relx=0.5, anchor='center')
		else:
			self.controller.show("GamePage")

	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(1)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.2, relx=0.05, anchor='w')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.65, relx=0.6, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.9, relx=0.1, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.1, relx=0.85, anchor='center')

		self.virus2 = PhotoImage(file='virus.png').subsample(2)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.5, relx=0.05, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.9, relx=0.9, anchor='center')

		self.virus3 = PhotoImage(file='virus.png').subsample(4)
		l_virus = Label(self, image=self.virus3, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.1, relx=0.55, anchor='center')

		l_virus = Label(self, image=self.virus3, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.9, relx=0.35, anchor='center')


class GamePage(Frame):
	'''Game Play Frame'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		self.parent = parent

		self.add_image()

		# executes on_show_frame evertime frame is raised
		self.bind("<<ShowFrame>>", lambda e: self.on_show_frame(e))

		# for leaderboard
		self.is_new_record = False
		self.L_name = ''
		self.L_time = ''

		# for random x,y for virus movement
		self.moves = [18, 19, 20, 21, 22, 23]

		# check if game wants to be resumes
		self.is_save = False
		
	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(2)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.2, relx=0.05, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.05, relx=0.3, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.2, relx=0.65, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.15, relx=0.9, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.55, relx=0.95, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.9, relx=0.97, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.95, relx=0.45, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.85, relx=0.02, anchor='center')

		self.virus2 = PhotoImage(file='virus.png').subsample(5)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.95, relx=0.6, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.97, relx=0.25, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.4, relx=0.06, anchor='center')

	def on_show_frame(self, event):
		if self.is_save == False: # start new game
			# keep the list of virus
			self.virus_lst = []

			# size of virus <- This increases the difficulty
			self.size = 40

			# flag to trigger generation of virus
			self.is_generate = False

			# flag to show game pause
			self.is_pause = False

			# game over flag
			self.game_over = False
			
			# for leaderboard
			self.is_new_record = False

			# custom keys
			self.custom_up = 'Up'
			self.custom_down = 'Down'
			self.custom_left = 'Left'
			self.custom_right = 'Right'

			# Pause Button
			self.Bpause = Button(self, text="||", fg="orangered4", bg='bisque3', font=("Fixedsys",38), width=2, command= lambda : self.pause())
			self.Bpause.place(rely=0, relx=0.97, anchor='n')
			
			
			# Survival Time Label
			self.sTime = Label(self, text= '0', fg="bisque3", bg='orangered4', font=("Fixedsys",65))
			self.sTime.place(rely=0.01, relx=0.5, anchor='n')
			# survival timing
			self.count = 0		

			# survival time words
			stime = Label(self, text="SURVIVAL TIMING", fg="bisque3", bg='orangered4', font=("Fixedsys",15))
			stime.place(rely=0.12, relx=0.5, anchor='n')

			# Create a canvas
			self.platform = Canvas(self, bg="orangered4", width=1300, height=650, highlightthickness=0)
			self.platform.place(rely=0.17, relx=0.5, anchor='n')			

			self.platform.focus_set()

			# character
			body = self.platform.create_oval(630, 305, 670, 345, outline='black', fill="coral1", tags=("character","c_hitpoint"))
			eye1 = self.platform.create_oval(640, 315, 645, 320, fill='black', tags="character")
			eye2 = self.platform.create_oval(655, 315, 660, 320, fill='black', tags="character")
			smile = self.platform.create_arc(645, 325, 655, 335, extent=(-180), style='arc', width=1.5, tags=("character"))
			
			# check for cheat code
			if self.controller.get_page("SPage").is_apply: # correct cheat code
				# change colour of character
				self.platform.itemconfig(body, fill='paleturquoise1')
				# change random x y movement for virus so that virus moves slower
				self.moves = [14, 15, 16, 17, 18, 19]

			# borders for canvas
			self.platform.create_line(0, 0, 1300, 0, width=10, dash=(60,40), fill="bisque3") #top
			self.platform.create_line(0, 0, 0, 650, width=10, dash=(60,40), fill="bisque3") #left
			self.platform.create_line(0, 650, 1300, 650, width=10, dash=(60,40), fill="bisque3") #bottom
			self.platform.create_line(1300, 0, 1300, 650, width=10, dash=(60,40), fill="bisque3") #right

			# bind arrow keys to character
			self.custom_up = self.controller.get_page("SPage").custom_up
			self.custom_down = self.controller.get_page("SPage").custom_down
			self.custom_left = self.controller.get_page("SPage").custom_left
			self.custom_right = self.controller.get_page("SPage").custom_right
			

			self.controller.bind('<' + self.custom_left + '>', lambda e: self.left(e))
			self.controller.bind('<' + self.custom_right + '>', lambda e: self.right(e))
			self.controller.bind('<' + self.custom_up + '>', lambda e: self.up(e))
			self.controller.bind('<' + self.custom_down + '>', lambda e: self.down(e))
			
			# to take care movement in x and y direction
			self.x = 0
			self.y = 0

			# move object
			self.movement()	

		else:	
			# check for cheat code
			if self.controller.get_page("SPage").is_apply: # correct cheat code
				# change colour of character
				self.platform.itemconfig(body, fill='paleturquoise1')

				# change random x y movement for virus so that virus moves slower
				self.moves = [14, 15, 16, 17, 18, 19]

	def pause(self):
		global pFrame		
		# halt all movements (character and virus)
		self.is_pause = True

		pFrame = Frame(self, bg='bisque3', highlightbackground="black", highlightthickness=3, bd=0, height=500, width=400)
		pFrame.place(rely=0.5, relx=0.5, anchor='center')

		pFrame.tkraise()

		# disable pause button
		self.Bpause.config(state='disabled')

		# disable arrow keys so that object doesnt move
		self.controller.unbind('<' + self.custom_left + '>')
		self.controller.unbind('<' + self.custom_right + '>')
		self.controller.unbind('<' + self.custom_up + '>')
		self.controller.unbind('<' + self.custom_down + '>')

		# Pause label
		Lpause = Label(pFrame, text="PAUSE", bg="bisque3", fg='black', font=("Fixedsys",60))
		Lpause.place(rely=0.15, relx=0.5, anchor='n')

		# Resume button
		resume = Button(pFrame, text='RESUME', fg='black', bg='darkolivegreen4', font=("Fixedsys",35), command= lambda: self.resume(pFrame))
		resume.place(rely=0.4, relx=0.5, anchor='n')

		# Main Menu button
		to_home = Button(pFrame, text='TO MAIN', fg='black', bg='dark khaki', font=("Fixedsys",35), command= lambda: self.to_main(pFrame))
		to_home.place(rely=0.63, relx=0.5, anchor='n')

	def resume(self, frame):
		# destroy pause frame
		frame.destroy()

		self.Bpause.config(state='normal')
		self.controller.bind('<' + self.custom_left + '>', lambda e: self.left(e))
		self.controller.bind('<' + self.custom_right + '>', lambda e: self.right(e))
		self.controller.bind('<' + self.custom_up + '>', lambda e: self.up(e))
		self.controller.bind('<' + self.custom_down + '>', lambda e: self.down(e))
		self.is_pause = False

	def to_main(self, frame):
		# message box to ask whether user wants to save the game
		reply = messagebox.askyesno(title='Save', message='SAVE GAME?',)
		if reply == True:
			self.is_save = True
		else:
			self.is_save = False
			# destroy pause frame
			frame.destroy()
			self.platform.destroy()
			self.update_leaderboard()
		
		self.controller.show("MainPage")
		
	def update_clock(self):
		def increase():
			# game over if true
			if self.game_over == True:
				return

			# temporarily stop clock
			while self.is_pause:
				self.wait_window(pFrame)

			# increase difficulty every 100 time only 5 levels
			time = int(self.sTime['text'])
			if time > 200:
				self.size = 95
			elif time > 150:
				self.size = 80
			elif time > 100:
				self.size = 65
			elif time > 50:
				self.size = 50

			self.sTime['text'] = str(self.count)
			self.sTime.after(600,increase)
			self.count += 1						
		increase()

	def virus(self, canvas, I):

		def gen_virus():
			# temporarily stop movement of viruses
			while self.is_pause:			
				for v in self.virus_lst:
					self.platform.move(v[1],0,0)
				self.wait_window(pFrame)

			# move depending on which side of canvas virus is generated from
			for v in self.virus_lst:
				if v[4] < 650 and v[5] < 20: # top left
					self.platform.move(v[1],v[2],v[3])
				elif v[4] >650 and v[5] < 20: # top right
					self.platform.move(v[1],-v[2],v[3])
				elif v[4] < 30: # left side
					self.platform.move(v[1],v[2],0)
				elif v[4] >1250: # right side
					self.platform.move(v[1],-v[2],0)
				else: # anywhere else other than listed above
					self.platform.move(v[1],v[2],v[3])

				# remove virus when it goes off frame
				virus_wall = self.platform.bbox(v[0])
				if virus_wall == None or (virus_wall[0] <= 7) or (virus_wall[1] <= 7) or (virus_wall[2] >= 1293) or (virus_wall[3] >= 643) :
					self.virus_lst.remove(v)
					self.platform.delete(v[1])


			# Creation of virus shape
			x = random.randint(0,1270)
			if 20 < x < 1250: #top or bottom part of canvas
				y = random.randint(5,30)
			else: # from sides
				y = random.randint(0,570)

			circle = canvas.create_oval(x, y, x+I, y+I, outline='#FFFFFF', fill='grey80', tags=('v_hitpoint' + str(self.count), 'virus' + str(self.count)))
			# triangle
			triangle1 = canvas.create_polygon(x+(I/2), y, x+(3*I/4), y-(I/2), x+(I/4), y-(I/2), fill='Red2', tags='virus' + str(self.count)) #top
			triangle2 = canvas.create_polygon(x, y+(I/2), x-(I/2), y+(1*I/4), x-(I/2), y+(3*I/4), fill='Red2', tags='virus' + str(self.count)) #left
			triangle3 = canvas.create_polygon(x+(I/2), y+I, x+(I/4), y+(3*I/2), x+(3*I/4), y+(3*I/2), fill='Red2', tags='virus' + str(self.count)) #bottom
			triangle4 = canvas.create_polygon(x+I, y+(I/2), x+(3*I/2), y+(3*I/4), x+(3*I/2), y+(I/4), fill='Red2', tags='virus' + str(self.count)) #right

			# move virus
			xmove = random.choice(self.moves)
			ymove = random.choice(self.moves)

			self.virus_lst += [['v_hitpoint' + str(self.count), 'virus' + str(self.count), xmove, ymove, x, y]]

			self.virus(self.platform, self.size)

		# game over if true
		if self.game_over == True:
			self.is_generate = False
			return

		self.is_generate = True
		self.platform.after(260,gen_virus)

	def movement(self): # movement of character + GAMEOVER handling
		# temporarily stop movement of character
		while self.is_pause:
			self.platform.move('character', 0, 0)
			self.wait_window(pFrame)	

		self.platform.move('character', self.x, self.y)	
		#Get list of coordinate to detect collision
		character_wall = self.platform.bbox("c_hitpoint")
		
		# Edge Collision detection
		if (character_wall[0] <= 7) or (character_wall[1] <= 7) or (character_wall[2] >= 1293) or (character_wall[3] >= 643):
			self.x = 0
			self.y = 0

		# Virus collision detection
		obj = self.platform.find_closest((character_wall[0] + character_wall[2])/2 , (character_wall[1] + character_wall[3])/2 , halo=20)

		# character id is 4 so any number other than 4 means collision 
		# game over
		if obj != (4,):
			self.game_over = True
			# Game over label
			gameover = Label(self.platform, text="GAME OVER", fg='tan2', bg='orangered4', font=("Fixedsys",90))
			gameover.place(rely=0.25, relx=0.5, anchor='n')
			# Disable pause when game over
			self.Bpause.config(state='disabled')
			# to Main Menu button
			to_home = Button(self.platform, text='TO MAIN', fg='orangered4', bg='tan2', font=("Fixedsys",55), command= lambda: [self.controller.show("MainPage"), self.Bpause.config(state='normal'), self.update_leaderboard()])
			to_home.place(rely=0.55, relx=0.5, anchor='n')
			return

		self.platform.after(50, self.movement)

	def update_leaderboard(self):
		# make cheat code false
		self.controller.get_page("SPage").is_apply = False

		# make is_save false
		self.is_save = False

		self.is_new_record = True
		# leaderboard time and name
		self.L_time = self.sTime['text']
		self.L_name = self.controller.get_page("RPage").inputbox.get("1.0", 'end-1c')

		# delete time label widget
		self.sTime.destroy()

		# delete name input in register
		self.controller.get_page("RPage").inputbox.delete("1.0", END)

		# update the leaderboard
		self.controller.get_page("LPage").on_show_frame(None)

	# move depending on direction
	def left(self, event):
		if self.sTime.cget('text') == '0':
			self.update_clock()
		if self.is_generate == False:
			self.virus(self.platform, self.size)

		self.x = -13
		self.y = 0

	def right(self, event):
		if self.sTime.cget('text') == '0':
			self.update_clock()
		if self.is_generate == False:
			self.virus(self.platform, self.size)

		self.x = 13
		self.y = 0

	def up(self, event):
		if self.sTime.cget('text') == '0':
			self.update_clock()
		if self.is_generate == False:
			self.virus(self.platform, self.size)

		self.x = 0
		self.y = -13

	def down(self, event):
		if self.sTime.cget('text') == '0':
			self.update_clock()
		if self.is_generate == False:
			self.virus(self.platform, self.size)

		self.x = 0
		self.y = 13


class IPage(Frame):
	'''Intruction page on how to play the game'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.add_image()

		back = Button(self, text="BACK", fg="black", bg='yellow4', font=("Fixedsys",40), command=lambda: controller.show("MainPage")) #to main page
		back.place(rely=0.0, relx=0.0, anchor='nw')

		header = Label(self, text="HOW TO PLAY?", fg="antiquewhite3", bg='orangered4', font=("Fixedsys",50))
		header.place(rely=0.10, relx=0.5, anchor='n')

		############## Panel 4 weirdly if I tab this it wouldnt work###################
		step4 = '''SURVIVE AS LONG
AS YOU CAN!
GOOD LUCK'''
		step4 = Label(self, text=step4, font=("Fixedsys",45), fg="antiquewhite3", bg='orangered4', justify='center')
		step4.place(rely=0.75, relx=0.55, anchor='w')
		
		############## Panel 1 for instruction on how to play the game ############
		step1 = '''
		USE ARROW KEYS 
		TO MOVE AND DODGE  
		THE VIRUS
		'''
		step1 = Label(self, text=step1, bg='antiquewhite3', font=("Fixedsys",20), justify='left')
		step1.place(rely=0.42, relx=0.07, anchor='w')
		c = self.panel(180)
		c.place(rely=0.42, relx=0.07, anchor='w')
		
		# randomly generate virus in the panel
		for i in range(5):
			c = self.virus(c, 15)

		############### Panel 2 about virus grow bigger in size as time passes ####################
		step2 = '''
		VIRUS GETS 
		BIGGER AS TIME  
		PASSES...
		'''
		step2 = Label(self, text=step2, bg='antiquewhite3', font=("Fixedsys",20), justify='left')
		step2.place(rely=0.42, relx=0.55, anchor='w')
		c = self.panel(180)
		c.place(rely=0.42, relx=0.55, anchor='w')

		for i in range(5):
			c = self.virus(c, 30)

		################## Panel 3 about game over if touch virus ########################
		step3 = '''
		DO NOT TOUCH       
		THE VIRUS!!!
		'''
		step3 = Label(self, text=step3, bg='antiquewhite3', font=("Fixedsys",20), justify='left')
		step3.place(rely=0.75, relx=0.07, anchor='w')
		c = self.panel(-180)
		c = self.specific_virus(c, 68, 73)
		c.place(rely=0.75, relx=0.07, anchor='w')
		
		for i in range(3):
			c = self.virus(c, 20)

	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(1)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.05, relx=0.8, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.95, relx=0.45, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.3, relx=0.25, anchor='center')

		self.virus2 = PhotoImage(file='virus.png').subsample(4)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.43, relx=0.5, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.6, relx=0.9, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.53, relx=0.08, anchor='center')

	def panel(self, mood):
		c = Canvas(self, bg="wheat4", width=200, height=200)
		# border lines for canvas
		borderL = c.create_line(0, 0, 0, 200, width=7)
		borderR = c.create_line(200, 0, 200, 200, width=5)
		borderT = c.create_line(0, 0, 200, 0, width=7)
		borderB = c.create_line(0, 200, 200, 200, width=3)

		# character (smiley face)
		body = c.create_oval(80, 80, 120, 120, outline='black', fill="coral1")
		eyes = c.create_oval(90, 90, 95, 95, fill='black')
		eyes = c.create_oval(105, 90, 110, 95, fill='black')
		smile = c.create_arc(93, 100, 105, 110, extent=-(mood), style='arc', width=1.5)
		return c

	def virus(self, canvas, I):
		# Creation of virus shape
		x = random.randint(0,170)
		if 20 < x < 180: #top or bottom part of canvas
			lst = [random.randint(0,20), random.randint(170,180)]
			choice = random.randint(0,1)
			y = lst[choice]
		else: # from sides
			y = random.randint(20,180)

		circle = canvas.create_oval(x, y, x+I, y+I, outline='#FFFFFF', fill='grey80')
		# triangle
		canvas.create_polygon(x+(I/2), y, x+(3*I/4), y-(I/2), x+(I/4), y-(I/2), fill='Red2') #top
		canvas.create_polygon(x, y+(I/2), x-(I/2), y+(1*I/4), x-(I/2), y+(3*I/4), fill='Red2') #left
		canvas.create_polygon(x+(I/2), y+I, x+(I/4), y+(3*I/2), x+(3*I/4), y+(3*I/2), fill='Red2') #bottom
		canvas.create_polygon(x+I, y+(I/2), x+(3*I/2), y+(3*I/4), x+(3*I/2), y+(I/4), fill='Red2') #right
		return canvas

	def specific_virus(self, canvas, x, y):
		# the one virus that touches the character
		circle = canvas.create_oval(x, y, x+20, y+20, outline='#FFFFFF', fill='grey80')
		# triangle
		canvas.create_polygon(x+10, y, x+15, y-10, x+5, y-10, fill='Red2') #top
		canvas.create_polygon(x, y+10, x-10, y+5, x-10, y+15, fill='Red2') #left
		canvas.create_polygon(x+10, y+20, x+5, y+30, x+15, y+30, fill='Red2') #bottom
		canvas.create_polygon(x+20, y+10, x+30, y+15, x+30, y+5, fill='Red2') #right
		return canvas


class LPage(Frame):
	'''Leaderboard page'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.add_image()

		back = Button(self, text="BACK", fg="black", bg='yellow4', font=("Fixedsys",40), command=lambda: controller.show("MainPage")) #to main page
		back.place(rely=0.0, relx=0.0, anchor='nw')

		header = Label(self, text="LEADERBOARD", fg="antiquewhite3", bg='orangered4', font=("Fixedsys",50))
		header.place(rely=0.10, relx=0.5, anchor='n')

		# table headers for records
		H_player = Label(self, text='PLAYER', fg='dark goldenrod', bg='orangered4', font=("Fixedsys",35))
		H_player.place(rely=0.25, relx=0.3, anchor='n')

		H_score = Label(self, text='SCORE', fg='dark goldenrod', bg='orangered4', font=("Fixedsys",35))
		H_score.place(rely=0.25, relx=0.7, anchor='n')

		# dictionary to keep the records
		self.records = []

		# executes on_show_frame evertime frame is raised
		self.bind("<<ShowFrame>>", lambda e: self.on_show_frame(e))

		# create a frame to put records
		self.record_frame = Frame(self, bg='orangered4', height=500, width=1100, bd=0)
		self.record_frame.place(rely=0.63, relx=0.5, anchor='center')

	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(1)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.9, relx=0.1, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.4, relx=0.9, anchor='center')

		self.virus2 = PhotoImage(file='virus.png').subsample(3)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0, relx=0.2, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.05, relx=0.8, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=200, width=200)
		l_virus.place(rely=0.85, relx=0.8, anchor='center')

		self.virus3 = PhotoImage(file='virus.png').subsample(4)
		l_virus = Label(self, image=self.virus3, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.3, relx=0.1, anchor='center')

		l_virus = Label(self, image=self.virus3, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.95, relx=0.8, anchor='center')

		self.virus4 = PhotoImage(file='virus.png').subsample(5)
		l_virus = Label(self, image=self.virus4, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.95, relx=0.35, anchor='center')


	def on_show_frame(self, event):
		'''display updated leaderboard''' 
		# starting value for rely to put records
		y = 0

		# check if there is a new record
		if self.controller.get_page("GamePage").is_new_record:
			# delete previous frame
			self.record_frame.destroy()

			# another frame to keep the records
			self.record_frame = Frame(self, bg='orangered4', height=500, width=1100, bd=0)
			self.record_frame.place(rely=0.63, relx=0.5, anchor='center')

			# get name and score
			n = self.controller.get_page("GamePage").L_name
			s = self.controller.get_page("GamePage").L_time

			# add record to dictionary
			self.records += [[n,int(s)]]

			# sort the record 
			sorted_records = sorted(self.records, key=itemgetter(1), reverse=True)

			# put records in the leaderboard page
			for i in sorted_records:
				name = Label(self.record_frame, text=i[0], fg="antiquewhite3", bg='orangered4', font=("Fixedsys",30))
				name.place(rely=y, relx=0.22, anchor='n')
				score = Label(self.record_frame, text=str(i[1]), fg="antiquewhite3", bg='orangered4', font=("Fixedsys",30))
				score.place(rely=y, relx=0.78, anchor='n')
				# increment rely for next record
				y += 0.1

			self.controller.get_page("GamePage").is_new_record = False

		else:
			return


class QPage(Frame):
	'''Quit game'''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.add_image()

		text = '''
		YOU ARE LEAVING ALREADY? 
		ARE YOU REALLY LEAVING?
			  :(
		'''
		canvas = Canvas(self, bg='orangered4', bd=0, highlightthickness=0, width=1200, height=300)
		canvas.place(rely=0.4, relx=0.5, anchor='center')
		header = canvas.create_text(250, 150, fill='antiquewhite3', text=text, font=("Fixedsys",60))	

		# yes and no button
		yes = Button(self, text="Yup Goodbye!", fg="black", bg='yellow4', font=("Fixedsys",40), command=lambda: exit()) 
		no = Button(self, text="Nah I'm Staying!", fg="black", bg='salmon3', font=("Fixedsys",40), command= lambda: controller.show("MainPage")) #to main page
		yes.place(rely=0.64, relx=0.3, anchor='center')
		no.place(rely=0.64, relx=0.65, anchor='center')

	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(1)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.65, relx=0.6, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.9, relx=0.1, anchor='center')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.1, relx=0.9, anchor='center')

		self.virus2 = PhotoImage(file='virus.png').subsample(3)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.7, relx=0.95, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.2, relx=0.05, anchor='center')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.1, relx=0.4, anchor='center')


class SPage(Frame):
	'''Settings page + cheat code '''
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		self.parent = parent

		self.add_image()

		# detects if user types in key
		self.detect = False

		# custom keys
		self.custom_up = 'Up'
		self.custom_down = 'Down'
		self.custom_left = 'Left'
		self.custom_right = 'Right'

		# cheat code HERETOCHEAT
		self.cheat_code = "HERETOCHEAT"
		self.is_apply = False

		self.back = Button(self, text="BACK", fg="black", bg='yellow4', font=("Fixedsys",40), command=lambda: [controller.show("MainPage"), self.remove()]) #to main page
		self.back.place(rely=0.0, relx=0.0, anchor='nw')

		header = Label(self, text="CONTROLS", fg="antiquewhite3", bg='orangered4', font=("Fixedsys",40))
		header.place(rely=0.10, relx=0.2, anchor='n')

		c = Canvas(self, bg="orangered4", highlightcolor='white', highlightthickness=3, bd=0, width=1200, height=280)
		c.place(rely=0.35, relx=0.5, anchor='center')

		# place label at the left side
		up = Label(c, text='Move UP', fg='antiquewhite3', bg='orangered4', font=("Fixedsys",30))
		down = Label(c, text='Move DOWN', fg='antiquewhite3', bg='orangered4', font=("Fixedsys",30))
		left = Label(c, text='Move LEFT', fg='antiquewhite3', bg='orangered4', font=("Fixedsys",30))
		right = Label(c, text='Move RIGHT', fg='antiquewhite3', bg='orangered4', font=("Fixedsys",30))
		up.place(rely=0.16, relx=0.05, anchor='w')
		down.place(rely=0.39, relx=0.05, anchor='w')
		left.place(rely=0.62, relx=0.05, anchor='w')
		right.place(rely=0.85, relx=0.05, anchor='w')

		# label to tell player what to do to change key
		text = '''
		*hover mouse over key,
		click and change key
		'''
		label = Label(self, text=text, fg="antiquewhite3", bg='orangered4', pady=0, bd=0, font=("Fixedsys",9))
		label.place(rely=0.115, relx=0.56, anchor='n')

		# place label at the right side 
		self.l_up = Label(c, text='Up', fg='antiquewhite3', bg='orangered4', cursor='hand1', font=("Fixedsys",30))
		self.l_down = Label(c, text='Down', fg='antiquewhite3', bg='orangered4', cursor='hand1', font=("Fixedsys",30))
		self.l_left = Label(c, text='Left', fg='antiquewhite3', bg='orangered4', cursor='hand1', font=("Fixedsys",30))
		self.l_right = Label(c, text='Right', fg='antiquewhite3', bg='orangered4', cursor='hand1', font=("Fixedsys",30))
		self.l_up.place(rely=0.16, relx=0.6, anchor='w')
		self.l_down.place(rely=0.39, relx=0.6, anchor='w')
		self.l_left.place(rely=0.62, relx=0.6, anchor='w')
		self.l_right.place(rely=0.85, relx=0.6, anchor='w')

		# change colour when hover
		self.l_up.bind("<Enter>", lambda e : e.widget.config(fg='black'))
		self.l_up.bind("<Leave>", lambda e : e.widget.config(fg='antiquewhite3'))
		self.l_down.bind("<Enter>", lambda e : e.widget.config(fg='black'))
		self.l_down.bind("<Leave>", lambda e : e.widget.config(fg='antiquewhite3'))
		self.l_left.bind("<Enter>", lambda e : e.widget.config(fg='black'))
		self.l_left.bind("<Leave>", lambda e : e.widget.config(fg='antiquewhite3'))
		self.l_right.bind("<Enter>", lambda e : e.widget.config(fg='black'))
		self.l_right.bind("<Leave>", lambda e : e.widget.config(fg='antiquewhite3'))

		# change key
		self.l_up.bind("<Button-1>", lambda e, obj=self.l_up : self.changeKey(e, obj))
		self.l_down.bind("<Button-1>", lambda e, obj=self.l_down : self.changeKey(e, obj))
		self.l_left.bind("<Button-1>", lambda e, obj=self.l_left : self.changeKey(e, obj))
		self.l_right.bind("<Button-1>", lambda e, obj=self.l_right : self.changeKey(e, obj))

		# label for cheat code
		l_cheat = Label(self, text="CODE", fg="antiquewhite3", bg='orangered4', font=("Fixedsys",40))
		l_cheat.place(rely=0.58, relx=0.16, anchor='n')

		self.code = Text(self, width=15, height=1, font=("Fixedsys",40))
		self.code.place(rely=0.68, relx=0.27, anchor='n')

		apply_code = Button(self, text="APPLY", fg="black", bg='darkolivegreen4', font=("Fixedsys",30), command= lambda: self.validate_code(self.code))
		apply_code.place(rely=0.685, relx=0.5, anchor='n')

		# label for msg for cheat code
		self.msg = ''
	
	def add_image(self):
		self.virus1 = PhotoImage(file='virus.png').subsample(1)
		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.2, relx=0, anchor='w')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.6, relx=0.65, anchor='w')

		l_virus = Label(self, image=self.virus1, bg='orangered4', height=500, width=500)
		l_virus.place(rely=0.95, relx=0.25, anchor='w')

		self.virus2 = PhotoImage(file='virus.png').subsample(3)
		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.95, relx=0.8, anchor='w')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.15, relx=0.85, anchor='w')

		l_virus = Label(self, image=self.virus2, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.8, relx=0.1, anchor='w')

		self.virus3 = PhotoImage(file='virus.png').subsample(4)
		l_virus = Label(self, image=self.virus3, bg='orangered4', height=150, width=150)
		l_virus.place(rely=0.53, relx=0.4, anchor='w')

	def remove(self):
		# delete the input box content if anything is present
		self.code.delete("1.0", END)
		# delete the label shown below assuming player types in a code
		try:
			self.msg.destroy()
		except:
			pass

	def validate_code(self, code):
		# delete previous 
		try:
			self.msg.destroy()
		except:
			pass

		your_code = code.get("1.0", 'end-1c')

		if your_code == self.cheat_code:
			# code already applied
			if self.is_apply == True:
				text = 'Code Already Applied.'
			else:				
				# code correct, cheat applied
				self.is_apply = True
				text = "Successful. Code Applied"
		else:
			# code incorrect
			text = "Code Invalid"

		self.msg = Label(self, text=text, fg="yellow", bg='orangered4', font=("Fixedsys",10))
		self.msg.place(rely=0.78, relx=0.11, anchor='w')


	def pressed_key(self, event):
		if self.detect:
			event.widget['text'] = str(event.keysym)
			self.detect = False

		# enable the binding again
		self.l_up.bind("<Button-1>", lambda e, obj=self.l_up : self.changeKey(e, obj))
		self.l_down.bind("<Button-1>", lambda e, obj=self.l_down : self.changeKey(e, obj))
		self.l_left.bind("<Button-1>", lambda e, obj=self.l_left : self.changeKey(e, obj))
		self.l_right.bind("<Button-1>", lambda e, obj=self.l_right : self.changeKey(e, obj))

		# # update the custom key
		if event.widget == self.l_up:
			self.custom_up = str(event.keysym)
		elif event.widget == self.l_down:
			self.custom_down = str(event.keysym)
		elif event.widget == self.l_left:
			self.custom_left = str(event.keysym)
		else:
			self.custom_right = str(event.keysym)

		# activate BACK button again
		self.back.config(state='normal')

	def changeKey(self, event, label):
		# disable other Button-1 binding
		self.l_up.unbind("<Button-1>")
		self.l_down.unbind("<Button-1>")
		self.l_left.unbind("<Button-1>")
		self.l_right.unbind("<Button-1>")

		# disable BACK button
		self.back.config(state='disabled')

		label["text"] = "--"
		# keyboard focus on widget
		label.focus_set()

		label.bind("<Key>", self.pressed_key)

		if self.detect == False:
			self.detect = True

		
if __name__ == "__main__":
	game = Game()
	game.mainloop()
