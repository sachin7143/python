import tkinter as tk

root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

def paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

canvas.bind("<B1-Motion>", paint)
root.mainloop()
