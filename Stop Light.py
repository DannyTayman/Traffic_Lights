import tkinter as tk
import time

#New Window
traffic_lights = tk.Tk()
traffic_lights.title("Traffic Lights")
traffic_lights.geometry("1000x700+600+150")
traffic_lights.resizable(False, False)
traffic_lights.iconbitmap("")
traffic_lights.config(bg="white")

#widgets
myCanvas = tk.Canvas(traffic_lights, height=1000, width=700, bg="White")
myCanvas.pack()
myCanvas.create_rectangle(50, 200, 150, 500, fill="#4ea6a1", width=2)
myCanvas.create_rectangle(550, 200, 650, 500, fill="#4ea6a1", width=2)
myCanvas.create_rectangle(300, 10, 400, 310, fill="#4ea6a1", width=2)
myCanvas.create_rectangle(300, 390, 400, 690, fill="#4ea6a1", width=2)
myCanvas.create_oval(50, 300, 150, 400, fill="Black", width = 2)
myCanvas.create_oval(550, 300, 650, 400, fill="Black", width = 2)
myCanvas.create_oval(300, 110, 400, 210, fill="Black", width = 2)
myCanvas.create_oval(300, 490, 400, 590, fill="Black", width = 2)
myCanvas.create_oval(50, 200, 150, 300, fill="Black", width = 2)
myCanvas.create_oval(550, 200, 650, 300, fill="Black", width = 2)
myCanvas.create_oval(300, 210, 400, 310, fill="Black", width = 2)
myCanvas.create_oval(300, 590, 400, 690, fill="Black", width = 2)

a = 10

while True:
    def green():
        i = 0
        while(i < a):
            green = myCanvas.create_oval(50, 400, 150, 500, fill="Green", width = 2)
            green = myCanvas.create_oval(550, 400, 650, 500, fill="Green", width = 2)
            green = myCanvas.create_oval(300, 10, 400, 110, fill="Red", width = 2)
            green = myCanvas.create_oval(300, 390, 400, 490, fill="Red", width = 2)
            traffic_lights.update()
            time.sleep(0.5)
            i = i+1
    def greenb():
        i = 0
        while(i < 2):
            green = myCanvas.create_oval(50, 400, 150, 500, fill="Black", width = 2)
            green = myCanvas.create_oval(550, 400, 650, 500, fill="Black", width = 2)
            green = myCanvas.create_oval(300, 10, 400, 110, fill="Black", width = 2)
            green = myCanvas.create_oval(300, 390, 400, 490, fill="Black", width = 2)
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1
    
    def yellow():
        i = 0
        while(i < a):
            yellow = myCanvas.create_oval(50, 300, 150, 400, fill = "Yellow", width = 2)
            yellow = myCanvas.create_oval(550, 300, 650, 400, fill = "Yellow", width = 2)
            yellow = myCanvas.create_oval(300, 10, 400, 110, fill="Red", width = 2)
            yellow = myCanvas.create_oval(300, 390, 400, 490, fill="Red", width = 2)
            traffic_lights.update()
            time.sleep(0.1)
            i = i+1
    def yellowb():
        i = 0
        while(i < 2):
            yellow = myCanvas.create_oval(50, 300, 150, 400, fill="Black", width = 2)
            yellow = myCanvas.create_oval(550, 300, 650, 400, fill="Black", width = 2)
            yellow = myCanvas.create_oval(300, 10, 400, 110, fill="Black", width = 2)
            yellow = myCanvas.create_oval(300, 390, 400, 490, fill="Black", width = 2)
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1

    def red():
        i = 0
        while(i < a):
            red = myCanvas.create_oval(50, 200, 150, 300, fill = "Red", width = 2)
            red = myCanvas.create_oval(550, 200, 650, 300, fill = "Red", width = 2)
            red = myCanvas.create_oval(300, 210, 400, 310, fill="Green", width = 2)
            red = myCanvas.create_oval(300, 590, 400, 690, fill="Green", width = 2)
            traffic_lights.update()
            time.sleep(0.5)
            i=i+1
    def redb():
        i = 0
        while(i < 2):
            red = myCanvas.create_oval(50, 200, 150, 300, fill="Black", width = 2)
            red = myCanvas.create_oval(550, 200, 650, 300, fill="Black", width = 2)
            red = myCanvas.create_oval(300, 210, 400, 310, fill="Black", width = 2)
            red = myCanvas.create_oval(300, 590, 400, 690, fill="Black", width = 2)
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1
            
    def yellow2():
        i = 0
        while(i < a):
            yellow = myCanvas.create_oval(50, 200, 150, 300, fill = "Red", width = 2)
            yellow = myCanvas.create_oval(550, 200, 650, 300, fill = "Red", width = 2)
            yellow = myCanvas.create_oval(300, 110, 400, 210, fill="Yellow", width = 2)
            yellow = myCanvas.create_oval(300, 490, 400, 590, fill="Yellow", width = 2)
            traffic_lights.update()
            time.sleep(0.1)
            i = i+1
    def yellowb2():
        i = 0
        while(i < 2):
            yellow = myCanvas.create_oval(50, 200, 150, 300, fill="Black", width = 2)
            yellow = myCanvas.create_oval(550, 200, 650, 300, fill="Black", width = 2)
            yellow = myCanvas.create_oval(300, 110, 400, 210, fill="Black", width = 2)
            yellow = myCanvas.create_oval(300, 490, 400, 590, fill="Black", width = 2)
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1

    green()
    greenb()
    yellow()
    yellowb()
    red()
    redb()
    yellow2()
    yellowb2()

traffic_lights.mainloop()