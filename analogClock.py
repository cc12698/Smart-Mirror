try:
    import Tkinter
except:
    import tkinter as Tkinter

import math
import time

class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x=250
        self.y=250
        self.length=100
        self.createFuncTrigger()

    def createFuncTrigger(self):
        self.createsCanvasForShapes()
        self.createBackground()
        self.createSticks()
        return

    def createBackground(self):
        self.image = Tkinter.PhotoImage(file = 'clock6.gif')#Tkinter.PhotoImage does not support JPG
        self.canvas.create_image(250,250, image=self.image)
        return
    
    def createsCanvasForShapes(self):
        self.canvas=Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes',fill='both')
        return
    
    def createSticks(self):
        self.sticks=[]
        for i in range(3):
            store=self.canvas.create_line(self.x, self.y, self.x+self.length, self.y+self.length, width =2, fill = 'green')
            self.sticks.append(store)
        return

    def updateClass(self):
        now=time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t))* 5
        now = (hour, now.tm_min, now.tm_sec)

        for n,i in enumerate(now):
            x,y=self.canvas.coords(self.sticks[n])[0:2]
            cr=[x,y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
        return

if __name__ == '__main__':
    root=main()

while True:
    root.update()
    root.update_idletasks()
    root.updateClass()


