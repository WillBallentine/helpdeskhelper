#!/usr/bin/env python

#HelpDesk Helper

""" 
### NOTES SECTION ###
Things I want to add:
1. Server functions
	a. find scheduled tasks
2. Network Functions
3. Exterior App functions (ipscan)
4. Config Troubleshooting
5. commands such as dns things, gp things, etc
6. 365 management
7. Linux functions
--Add more as I think of it
"""


import os, subprocess, traceback, smtplib, types
from tkinter import *
import platform
import time
import smtplib, ssl, string



#------------------------------------------------------------Jank Disappear Functions---------------------------------------------------------#
def close():
	options = Label(helper, text='''                           \n                                                                                    \n                                                                                                                                                                                                        ''', fg="Black", relief="flat", font=("Helvetica", 12,"bold")).place(x=100, y=105)

def close2():
	options = Label(helper, text='''                           \n                                                                                    \n                                                                                                    \n                                                       \n                                                                                                                                                                   ''', fg="Black", relief="flat", font=("Helvetica", 12,"bold")).place(x=300, y=275)


#------------------------------------------------------------Execution of Selection---------------------------------------------------------#
#----------------------------------------------------------------------CMD------------------------------------------------------------------#
def sfc():
	os.system('cmd /c "sfc /scannow"')

def dism():
	os.system('cmd /c "dism /online /cleanup-image /checkhealth"')

def og():
	os.system('cmd /c "dism /online /cleanup-image /restorehealth && sfc /scannow"')

def user():
	os.system('cmd /c "net user"')
	
def print_functions():
	os.system('cmd /c "net stop spooler && del %%systemroot%\\System32\\spool\\printers\\* /Q /F /S && net start spooler"')

def local_admin_add():
	user_var = StringVar()
	passwrd_var = StringVar()
	def go3():
		user = user_var.get()
		passwrd = passwrd_var.get()
		os.system('cmd /c "net user /add %s %s"' % (user, passwrd))
		os.system('cmd /c "net localgroup administrators %s /add"' % (user))
		helper.after(5000, close2)

	userentry = Entry(helper, textvariable=user_var, fg ="black", bg = "white", width = 20).place(x=300, y=300)
	passentry = Entry(helper, textvariable=passwrd_var, fg ="black", bg = "white", width = 20).place(x=600, y=300)
	addlabel = Label(helper, text="Username", fg="black", width=20).place(x=300, y=275)
	passlabel = Label(helper, text="Password", fg="black", width=20).place(x=600, y=275)
	userbutton = Button(helper, text="Go", fg="black", width =20, command = go3).place(x=450, y=325)


def local_admin_remove():
	user2_var = StringVar()
	def go4():
		user2 = user2_var.get()
		os.system('cmd /c "net localgroup administrators %s /delete"' % (user2))
		helper.after(5000, close2)

	user2entry = Entry(helper, textvariable=user2_var, fg ="black", bg = "white", width = 20).place(x=450, y=300)
	add2label = Label(helper, text="Username", fg="black", width=20).place(x=450, y=275)
	user2button = Button(helper, text="Go", fg="black", width =20, command = go4).place(x=440, y=325)

def boot_state():
	os.system('wmic COMPUTERSYSTEM GET BootupState')




#------------------------------------------------------------CMD More---------------------------------------------------------#
def restart():
	os.system('shutdown /r')

def ipconfig():
	os.system('ipconfig')

def ipconfigall():
	os.system('ipconfig /all')

def ipconfigrel():
	os.system('ipconfig /release')

def ipconfigrenew():
	os.system('ipconfig /renew')

def ipconfigdns():
	os.system('ipconfig /flushdns')

def ipconfigdisplaydns():
	os.system('ipconfig /displaydns')

def traceroute():
	ip_var = StringVar()
	def go2():
		ip = ip_var.get()
		os.system("cmd /c tracert %s" % (ip))
		helper.after(5000, close2)

	ipentry = Entry(helper, textvariable=ip_var, fg ="black", bg = "white", width = 20).place(x=450, y=300)
	tracelabel = Label(helper, text="IP or Web Address", fg="black", width=20).place(x=300, y=275)
	tracebutton = Button(helper, text="Go", fg="black", width =20, command = go2).place(x=450, y=325)





#------------------------------------------------------------Uninstall---------------------------------------------------------#
def unadobe():
	os.system('cmd /c "wmic product where name="Adobe Acrobat Reader DC" call uninstall"')

def un365():
	os.system('cmd /c "wmic cmd /c "product where name="Office 16" call uninstall"')







#------------------------------------------------------------Repair---------------------------------------------------------#
def off32():
	os.system('cmd /c ""C:\\Program Files\\Microsoft Office 15\\ClientX64\\OfficeClicktoRun.exe" scenario=repair platform=x64 culture=en-us DisplayLevel=True"')

def off64():
	os.system('cmd /c ""C:\\Program Files\\Microsoft Office 15\\ClientX64\\OfficeClicktoRun.exe" scenario=repair platform=x86 culture=en-us DisplayLevel=True"')

def adorep():
	os.system('cmd /c ""C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe" scenario=repair platform=x64 DisplayLevel=True"')

def chrorep():
	os.system('cmd /c ""C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" scenario=repair platform=64 DisplayLevel=True"')







#------------------------------------------------------------Remote Desktop---------------------------------------------------------#
def rd_enable():
	os.system('reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f')

def rd_disable():
	os.system('reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f')

def remote_desktop_app():
	os.system('MSTSC')



		
#------------------------------------------------------------Server---------------------------------------------------------#

def robo():
	origin_var = StringVar()
	destination_var = StringVar()
	def go():
		origin = origin_var.get()
		destination = destination_var.get()
		os.system("cmd /c robocopy %s %s /E /Z /B" % (origin, destination))
		helper.after(5000, close2)
	


	oringinlabel = Label(helper, text="Origin", fg="black", width=20).place(x=300, y=275)
	destinationlabel = Label(helper, text="Destination", fg="black", width=20).place(x=600, y=275)
	originentry = Entry(helper, textvariable=origin_var, fg ="black", bg = "white", width = 20).place(x=300, y=300)
	destinationentry = Entry(helper, textvariable= destination_var, fg ="black", bg = "white", width = 20).place(x=600, y=300)
	robobutton = Button(helper, text="Go", fg="black", width =20, command = go).place(x=450, y=325)




#------------------------------------------------------------Feedback---------------------------------------------------------#
def feedback():
	port = 465 #for ssl
	smtp_server = "smtp.gmail.com"
	password = "yfDV9pqW8S8Tedu"

	sender_email = "travisjohnny43@gmail.com"
	receiver_email = "travisjohnny43@gmail.com"




	#create a secture SSL context
	context = ssl.create_default_context()



	#this is our actual function that sends the emails
	usermessage_var = StringVar()

	def report():
			usermessage = usermessage_var.get()
			message = """%s""" % (usermessage)

			with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
				server.login("travisjohnny43@gmail.com", password)
				server.sendmail(sender_email, receiver_email, message)
			helper.after(5000, close2)


	usermessagelabel = Label(helper, text="Feedback", fg="black", width=20).place(x=450, y=275)
	usermessageentry = Entry(helper, textvariable= usermessage_var, fg ="black", bg = "white", width = 20).place(x=450, y=300)
	#Multi line entry eventually#
	reportbutton = Button(helper, text="Send", fg="black", width =20, command = report).place(x=440, y=325)





#------------------------------------------------------------Button Layers---------------------------------------------------------#
#------------------------------------------------------------Upper Layers---------------------------------------------------------#
def more1():
	ip1 = Button(helper, text="ipconfig", fg="black", width =20, command=ipconfig).place(x=100, y=100)
	ip2 = Button(helper, text="ipconfig all", fg="black", width =20, command=ipconfigall).place(x=100, y=150)
	ip3 = Button(helper, text="ipconfig release", fg="black", width =20, command=ipconfigrel).place(x=100, y=200)
	ip4 = Button(helper, text="ipconfig renew", fg="black", width =20, command=ipconfigrenew).place(x=100, y=250)
	ip5 = Button(helper, text="ipconfig flushdns", fg="black", width =20, command=ipconfigdns).place(x=100, y=300)
	ip6 = Button(helper, text="ipconfig DNS info", fg="black", width =20, command=ipconfigdisplaydns).place(x=100, y=350)
	trace = Button(helper, text="traceroute", fg="black", width =20, command=traceroute).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	blank7 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=550)
	bk = Button(helper, text="Back", fg="black", width=20, command=cmd).place(x=100, y=600)

def more2():
	print("not built")

def more3():
	print("not built")

def more4():
	print("not built")


def server():
	robocopy = Button(helper, text="Robocopy", fg="black", width = 20, command = robo).place(x=100,y=100)
	blank = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=150)
	blank0 = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=200)
	blank1 = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=250)
	blank2 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=300)
	blank3 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)		
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	blank7 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=550)


def cmd():
	sffc = Button(helper, text="SFC", fg="black", width =20, command=sfc).place(x=100, y=100)
	dizm = Button(helper, text="dism", fg="black", width =20, command=dism).place(x=100, y=150)
	ol = Button(helper, text="Ol Gabehart", fg="black", width =20, command=og).place(x=100, y=200)
	ul = Button(helper, text="User List", fg="black", width =20, command=user).place(x=100, y=250)
	pf = Button(helper, text="Print Functions", fg="black", width =20, command=print_functions).place(x=100, y=300)
	la = Button(helper, text="Add Local Admin", fg="black", width =20, command=local_admin_add).place(x=100, y=350)
	lr = Button(helper, text="Remove Local Admin", fg="black", width =20, command=local_admin_remove).place(x=100, y=400)
	bs = Button(helper, text="Get Boot State", fg="black", width =20, command=boot_state).place(x=100, y=450)
	rs = Button(helper, text="Restart", fg="black", width=20, command=restart).place(x=100, y=500)
	mr = Button(helper, text="More", fg="black", width=20, command=more1).place(x=100, y=550)
	bk = Button(helper, text="Back", fg="black", width=20, command=job).place(x=100, y=600)

def uninstall():
	un = Button(helper, text="Uninstall Adobe", width = 20, command= unadobe).place(x=100,y=100)
	un2 = Button(helper, text="Uninstall Office 365", width = 20, command= un365).place(x=100,y=150)
	blank0 = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=200)
	blank1 = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=250)
	blank2 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=300)
	blank3 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	mr2 = Button(helper, text="More", fg="black", width=20, command=more2).place(x=100, y=550)
	bk = Button(helper, text="Back", fg="black", width=20, command=job).place(x=100, y=600)

def repair():
	o32 = Button(helper, text="32 Bit", width=20, command=off32).place(x=100,y=100)
	o64 = Button(helper, text="64 Bit", width=20, command=off64).place(x=100,y=150)
	adob = Button(helper, text="Adobe", width=20, command=adorep).place(x=100,y=200)
	chro = Button(helper, text="Chrome", width=20, command=chrorep).place(x=100,y=250)
	blank2 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=300)
	blank3 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	mr3 = Button(helper, text="More", fg="black", width=20, command=more3).place(x=100, y=550)
	bk = Button(helper, text="Back", fg="black", width=20, command=job).place(x=100, y=600)

def remote_desktop():
	rden = Button(helper, text="Enable", width=20, command=rd_enable).place(x=100, y=100)
	rddis = Button(helper, text="Disable", width=20, command=rd_disable).place(x=100, y=150)
	rda = Button(helper, text="Remote Desktop App", fg="black", width = 20, command = remote_desktop_app).place(x=100,y=200)
	blank1 = Button(helper, text="", fg="black", width = 20, command = job).place(x=100,y=250)
	blank2 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=300)
	blank3 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	mr4 = Button(helper, text="More", fg="black", width=20, command=more4).place(x=100, y=550)
	bk = Button(helper, text="Back", fg="black", width=20, command=job).place(x=100, y=600)




#------------------------------------------------------------Main Level---------------------------------------------------------#
def job():
	prompt = Button(helper, text="CMD", fg="black", width = 20, command = cmd).place(x=100,y=100)
	remove = Button(helper, text="Uninstall", fg="black", width = 20, command = uninstall).place(x=100,y=150)
	rep = Button(helper, text="App Repair", fg="black", width = 20, command = repair).place(x=100,y=200)
	remote = Button(helper, text="Remote Desktop", fg="black", width = 20, command = remote_desktop).place(x=100,y=250)
	serv = Button(helper, text="Server", fg="black", width =20, command=server).place(x=100, y=300)
	beta = Button(helper, text="Feedback", fg="black", width =20, command=feedback).place(x=100, y=350)
	blank4 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=400)
	blank5 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=450)		
	blank6 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=500)
	blank7 = Button(helper, text="", fg="black", width =20, command=job).place(x=100, y=550)


def options():
	options = Label(helper, text='''This tool is to help HelpDesk Engineers troubleshoot and resolve simple issues. \n Make a selection from the Function Selector on the left depending on the issue.''', fg="Black", relief="raised", font=("Helvetica", 12,"bold")).place(x=100, y=105)
	helper.after(5000, close)
	#Eventually want to make the options disappear after clicking


def helpdeskquit():
	exit()




#------------------------------------------------------------UI Main Definitions---------------------------------------------------------#
helper = Tk()

helper.title("HelpDesk Helper")
helper.geometry("800x800")


setYourJob = Label(helper, text="What do you want to do?", fg="Black", relief="raised", font=("Helevetica",20,"bold")).place(x=200, y=29)
job_format = Label(helper, text="Select your function:", fg="white", bg="black", font="Ariel")




submit = Button(helper, text = "Select Function", fg="black", width = 20, command = job).place(x=100,y=70)
options = Button(helper, text = "Show Options", fg= "black", width = 20, command= options).place(x=335, y=70)
quit = Button(helper, text='Quit', fg="black", width = 20, command=helpdeskquit).place(x=550, y=70) 

helper.mainloop()
