from tkinter import *


root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()


panelLayout = PanedWindow(orient=VERTICAL)
panelLayout.pack(fill=BOTH,expand=True)

panelMonitor_one = PanedWindow(orient=HORIZONTAL)
#panelMonitor_one.pack(fill=BOTH,expand=True)


panelMonitor_two = PanedWindow(orient=HORIZONTAL)
#panelMonitor_two.pack(fill=BOTH,expand=True)

top = Label(panelLayout,text="Multi Screen Monitoring System for Tonbo")
panelLayout.add(top)

panelLayout.add(panelMonitor_one,weight=1)
panelLayout.add(panelMonitor_two,weight=1)


screen_one = LabelFrame(panelMonitor_one,text="Camera 1",width=640, height=480)
panelMonitor_one.add(screen_one,weight=1)

screen_two = LabelFrame(panelMonitor_one,text="Camera 2",width=640, height=480)
panelMonitor_one.add(screen_two,weight=1)

screen_three = LabelFrame(panelMonitor_two,text="Camera 3",width=640, height=480)
panelMonitor_two.add(screen_three,weight=1)


screen_four = LabelFrame(panelMonitor_two,text="Camera 4",width=640, height=480)
panelMonitor_two.add(screen_four,weight=1)


root.title("Multi Screen Monitoring System for Tonbo")
root.geometry("%dx%d" % (screenWidth,screenHeight))

#root.pack(panel)

panelLayout.pack()

root.mainloop()







