import tkinter as tk
from faceDetection import image_detector

root = tk.Tk()

root.title('Image loader')

WIDTH = 1080
HEIGHT = 480

scaleFactor_var = tk.IntVar()
minNeighbors_var = tk.IntVar()

canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(canvas, bg = 'white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# creating a label for scalFactor_ var
scaleFactor_label = tk.Label(frame, text = "Scale Factor", font = ('colibre', 10, 'normal'),padx=10, pady=10)
scaleFactor_label.pack()
# creating a label for name using widget Label
scaleFactor_entry = tk.Entry(frame, textvariable = scaleFactor_var, font=('calibre',10,'normal'))
scaleFactor_entry.pack()

# creating a label for scalFactor_ var
minNeighbors_label = tk.Label(frame, text = "Scale Factor", font = ('colibre', 10, 'normal'),padx=10, pady=10)
minNeighbors_label.pack()
# creating a label for name using widget Label
minNeighbors_entry = tk.Entry(frame, textvariable = minNeighbors_var , font=('calibre',10,'normal'))
minNeighbors_entry.pack()

sub_btn = tk.Button(frame, text = "Submit")


btn = tk.Button(root, text="Select an image", command = image_detector)
btn.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")



root.mainloop()