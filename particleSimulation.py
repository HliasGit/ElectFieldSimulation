import tkinter as tk
from math import *
import numpy as np


window = tk.Tk()
window.title("Prova campo elettrico")
window.configure(width=900, height=600)
window.configure(bg='lightgray')

# move window center
winWidth = window.winfo_reqwidth()
winHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

# Create a canvas widget
canvas=tk.Canvas(window, width=winWidth, height=winHeight)
canvas.pack()

finitura = 10

# Add grid
for x in range((int)(winHeight/finitura)):
    canvas.create_line(0,x*finitura,winWidth,x*finitura, fill="green", width=2)

for y in range((int)(winWidth/finitura)):
    canvas.create_line(y*finitura,0,y*finitura,winHeight, fill="green", width=2)


#for an electron q = 1,6e-19C
elec_charge = -1.6*10**(-19)
epsilon_0 = float(8.85*10**(-12))

x1=270
y1=180
x2=x1+90
y2=y1+90
x_med = (x2+x1)/2
y_med = (y2+y1)/2

rad=(x2-x1)/2
diam=rad*2
circ=2*pi*rad
area=pi*rad**2

matrix = []

#Add vectors
for x in range((int)(winWidth/finitura)):
    row = []
    for y in range((int)(winHeight/finitura)):
        distance_x = abs(x_med-x*finitura-finitura/2)
        distance_y = abs(y_med-y*finitura-finitura/2)
        distance = sqrt(distance_x**2+distance_y**2)
        if distance > rad:
            field_mag = abs((elec_charge)/(pi*epsilon_0*(distance**2)*4))*1000000000000
        else:
            field_mag = 0
        row.append(field_mag)
    matrix.append(row)
    


for x in range((int)(winWidth/finitura)):
    for y in range((int)(winHeight/finitura)):
        #canvas.create_line(x*finitura,y*finitura,(x+1)*finitura,(y+1)*finitura, fill="red", width=2, arrow=tk.LAST)
        if matrix[x][y]>0.75:
            canvas.create_polygon(x*finitura, y*finitura, (x+1)*finitura,y*finitura, (x+1)*finitura, (y+1)*finitura,x*finitura, (y+1)*finitura, fill='gray')
        elif matrix[x][y]>0.5:
            canvas.create_polygon(x*finitura, y*finitura, (x+1)*finitura,y*finitura, (x+1)*finitura, (y+1)*finitura,x*finitura, (y+1)*finitura, fill='purple')
        elif matrix[x][y]>0.25:
            canvas.create_polygon(x*finitura, y*finitura, (x+1)*finitura,y*finitura, (x+1)*finitura, (y+1)*finitura,x*finitura, (y+1)*finitura, fill='red')
        elif matrix[x][y]>0.10:
            canvas.create_polygon(x*finitura, y*finitura, (x+1)*finitura,y*finitura, (x+1)*finitura, (y+1)*finitura,x*finitura, (y+1)*finitura, fill='pink')
        canvas.create_text(x*finitura+finitura/2,y*finitura+finitura/2, text=round(matrix[x][y],2), font=('Helvetica','5'))

#Add electron
canvas.create_oval(x1,y1,x2,y2, fill="blue")
window.mainloop()