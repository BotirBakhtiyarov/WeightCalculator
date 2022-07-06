from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculate weight")
root.config(bg="black")
root.geometry("380x300")
root.resizable(0,0)
#===============================================Button==============================================================
def click():
    mas = float(Mass.get())
    mass_sun = mas * 27.01
    mass_moon = mas * 0.16
    mass_mars = mas * 0.38

    mass_sun1 = str(mass_sun)
    mass_moon1 = str(mass_moon)
    mass_mars1 = str(mass_mars)


    mass_sun_lbl = Label(root, text=mass_sun1+"公斤", bg="black", fg="white")
    mass_sun_lbl.grid(row=3, column=0, pady=10, padx=10)

    mass_moon_lbl = Label(root, text=mass_moon1+"公斤", bg="black", fg="white")
    mass_moon_lbl.grid(row=3, column=1, pady=10, padx=10)

    mass_mars_lbl = Label(root, text=mass_mars1+"公斤", bg="black", fg="white")
    mass_mars_lbl.grid(row=3, column=2, pady=10, padx=10)
#=================================================地球=====================================================
earth = Image.open("earth.png")
resized_earth = earth.resize((100,100), Image.ANTIALIAS)
new_earth = ImageTk.PhotoImage(resized_earth)
earth_lbl = Label(root, image=new_earth, border=0)
earth_lbl.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

intro_lbl = Label(root, text="输入您的地球重量(公斤)：", bg="black", fg="white")
intro_lbl.grid(row=1, column=0)

Mass = Entry(root, border=0, bg="grey", fg="red")
Mass.grid(row=1, column=1)

start = Button(root, text="点击开始", border=0, bg="grey", fg="red", command=click)
start.grid(row=1, column=2)
#================================================太阳======================================================
sun = Image.open("sun.png")
resized_sun = sun.resize((100,100), Image.ANTIALIAS)
new_sun = ImageTk.PhotoImage(resized_sun)
sun_lbl = Label(root, image=new_sun, border=0)
sun_lbl.grid(row=2, column=0, pady=10, padx=10)
#================================================月球======================================================
moon = Image.open("moon.png")
resized_moon = moon.resize((100,100), Image.ANTIALIAS)
new_moon = ImageTk.PhotoImage(resized_moon)
moon_lbl = Label(root, image=new_moon, border=0)
moon_lbl.grid(row=2, column=1, pady=10, padx=10)
#================================================火星======================================================
mars = Image.open("mars.jpg")
resized_mars = mars.resize((100,100), Image.ANTIALIAS)
new_mars = ImageTk.PhotoImage(resized_mars)
mars_lbl = Label(root, image=new_mars, border=0)
mars_lbl.grid(row=2, column=2, pady=10, padx=10)

root.mainloop()
