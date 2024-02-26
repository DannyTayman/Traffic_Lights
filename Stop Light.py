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
myCanvas.create_line(175, 200, 175, 500, arrow="both", fill="Black")
myCanvas.create_line(525, 200, 525, 500, arrow="both", fill="Black")
myCanvas.create_line(300, 330, 400, 330, arrow="both", fill="Black")
myCanvas.create_line(300, 370, 400, 370, arrow="both", fill="Black")

shape1={'bounds': [245, 260, 300, 220, 300, 300], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape1.values())[0],fill='black',outline='black')
shape2={'bounds': [455, 260, 400, 220, 400, 300], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape2.values())[0],fill='black',outline='Black')
shape3={'bounds': [245, 650, 300, 610, 300, 690], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape3.values())[0],fill='black',outline='black')
shape4={'bounds': [455, 650, 400, 610, 400, 690], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape4.values())[0],fill='black',outline='Black')

shape5={'bounds': [50, 200, 150, 200, 100, 135], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape5.values())[0],fill='black',outline='black')
shape6={'bounds': [50, 500, 150, 500, 100, 565], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape6.values())[0],fill='black',outline='Black')
shape7={'bounds': [550, 200, 650, 200, 600, 135], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape7.values())[0],fill='black',outline='black')
shape8={'bounds': [550, 500, 650, 500, 600, 565], 'kind': 'tri', 'fill': True}
myCanvas.create_polygon(list(shape8.values())[0],fill='black',outline='Black')

a = 10

while True:
    def ew_green():
        i = 0
        while(i < a):
            green = myCanvas.create_oval(50, 400, 150, 500, fill="Green", width = 2)
            green = myCanvas.create_oval(550, 400, 650, 500, fill="Green", width = 2)
            green = myCanvas.create_oval(300, 10, 400, 110, fill="Red", width = 2)
            green = myCanvas.create_oval(300, 390, 400, 490, fill="Red", width = 2)
            green = myCanvas.create_line(300, 330, 400, 330, arrow="both", fill="Green")
            green = myCanvas.create_line(300, 370, 400, 370, arrow="both", fill="Green")
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
            green = myCanvas.create_line(300, 330, 400, 330, arrow="both", fill="Black")
            green = myCanvas.create_line(300, 370, 400, 370, arrow="both", fill="Black")
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1
    
    def ew_yellow():
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
            red = myCanvas.create_line(175, 200, 175, 500, arrow="both", fill="Green")
            red = myCanvas.create_line(525, 200, 525, 500, arrow="both", fill="Green")
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
            red = myCanvas.create_line(175, 200, 175, 500, arrow="both", fill="Black")
            red = myCanvas.create_line(525, 200, 525, 500, arrow="both", fill="Black")
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
    def ew_l_green_ns_r_green():
        i = 0
        while(i<a):
            green = myCanvas.create_polygon(list(shape1.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape4.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape5.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape8.values())[0],fill='green',outline='black')
            traffic_lights.update()
            time.sleep(0.5)
            i = i+1
    def ew_r_green_ns_l_green():
        i = 0
        while(i<a):
            green = myCanvas.create_polygon(list(shape2.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape3.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape6.values())[0],fill='green',outline='black')
            green = myCanvas.create_polygon(list(shape7.values())[0],fill='green',outline='black')
            traffic_lights.update()
            time.sleep(0.5)
            i = i+1
    def ew_l_green_ns_r_greenb():
        i = 0
        while(i<2):
            green = myCanvas.create_polygon(list(shape1.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape4.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape5.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape8.values())[0],fill='black',outline='black')
            traffic_lights.update()
            time.sleep(0.00000001)
            i = i+1
    def ew_r_green_ns_l_greenb():
        i = 0
        while(i<2):
            green = myCanvas.create_polygon(list(shape2.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape3.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape6.values())[0],fill='black',outline='black')
            green = myCanvas.create_polygon(list(shape7.values())[0],fill='black',outline='black')
            traffic_lights.update()
            time.sleep(0.00000001)
            i = i+1

    def ew_yellow2():
        i = 0
        while(i < a):
            yellow = myCanvas.create_oval(50, 300, 150, 400, fill = "Yellow", width = 2)
            yellow = myCanvas.create_oval(550, 300, 650, 400, fill = "Yellow", width = 2)
            traffic_lights.update()
            time.sleep(0.1)
            i = i+1
    def ew_yellowb2():
        i = 0
        while(i < 2):
            yellow = myCanvas.create_oval(50, 300, 150, 400, fill="Black", width = 2)
            yellow = myCanvas.create_oval(550, 300, 650, 400, fill="Black", width = 2)
            traffic_lights.update()
            time.sleep(0.000001)
            i = i+1

    
    ew_green()
    greenb()
    ew_yellow()
    yellowb()
    ew_r_green_ns_l_green()
    ew_r_green_ns_l_greenb()
    ew_yellow2()
    ew_yellowb2()
    red()
    redb()
    yellow2()
    yellowb2()
    ew_l_green_ns_r_green()
    ew_l_green_ns_r_greenb()
    ew_yellow()
    yellowb()

traffic_lights.mainloop()