from  tkinter import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import cv2
from pencocokan import *

window = Tk()
window.title("AlgeOwO")
window.geometry("900x600")
window.configure(bg="white")

processed = False

newimagedir=""
def insertimage():
    global newimagedir
    newimagedir = filedialog.askopenfilename(filetypes=[("jpg image","*.jpg"),("png image","*.png")])
    no_image_selected.config(text=newimagedir)
    #print(newimagedir)
    newimage = ImageTk.PhotoImage(Image.open(newimagedir).resize((300,300)))
    pimg_test.config(image=newimage)
    pimg_test.image=newimage

newfolderdir=""
def insertfolderdir():
    global newfolderdir
    newfolderdir = filedialog.askdirectory()
    no_dataset_selected.config(text=newfolderdir)
    

resultpath=""
def processimage():
    #global processed
    resultpath = test_image(newfolderdir,newimagedir)
    #if resultpath:
    resultimage = ImageTk.PhotoImage(Image.open(resultpath).resize((300,300)))
    pimg_result.config(image=resultimage)
    pimg_result.image=resultimage
    #else:
        #no_dataset_selected.config(text="Tidak ada gambar yang cocok")
        #print("Tidak ada gambar yang cocok")
    



# kumpulan label
header = Label(window, text="Face Recognition",bg="white",font=("Arial",24),fg="black")
insert_dataset_text = Label(window, text="Insert Your Dataset ", bg="white",font=("Times New Roman",12),fg="black")
insert_image_text  = Label(window, text="Insert Your Image ", bg="white",font=("Times New Roman",12),fg="black")
no_dataset_selected = Label(window, text="No Dataset Selected", bg="grey",font=("Times New Roman",12),fg="black")
no_image_selected = Label(window, text="No Image Selected", bg="grey",font=("Times New Roman",12),fg="black")

#result_text = insert_dataset = tk.Label(window, text="Result ", bg="white",font=("Times New Roman",12),fg="black")
test_image_text = Label(window, text="Test image ", bg="white",font=("Times New Roman",12),fg="black")
closest_result_text = Label(window, text="Closest Result ", bg="white",font=("Times New Roman",12),fg="black")

execution_time_text = Label(window, text="Execution time : ", bg="white",font=("Times New Roman",12),fg="black")

# kumpulan button
tombol_folder = Button(window, text="Choose file ", fg="blue")
#button_file = ImageTk.PhotoImage(Image.open("choose_file.png").resize((75,20)))
tombol_file = Button(window, text="Choose file ", fg="blue", bg="white")
tombol_process = Button(window, text="Process image", fg="blue")
tombol_file.config(command=lambda:insertimage())
tombol_folder.config(command=lambda:insertfolderdir())
tombol_process.config(command=lambda:processimage())

# kumpulan place
header.place(x=330, y=15)

insert_dataset_text.place(x=550, y=450)
tombol_folder.place(x =550, y = 475)
no_dataset_selected.place(x =550, y=500 )

insert_image_text.place(x=95,y = 450 )
tombol_file.place(x =95, y = 475)
no_image_selected.place(x=95, y = 500)

tombol_process.place(x=430,y=125)

#result_text.place(x=25, y=300)
test_image_text.place(x=120, y=75)
execution_time_text.place(x=250, y=425)
closest_result_text.place(x=575, y=75)

img_test=ImageTk.PhotoImage(Image.open("no_image.png").resize((270,270)))
pimg_test=Label(window)
pimg_test.config(width=300,height=300)
pimg_test.place(x=95,y=100)
pimg_test.config(image=img_test)
#resultimg = Label(window)
#resultimg.config(width=300,height=300)
#pimg_right = Label(window)

img_result=ImageTk.PhotoImage(Image.open("no_image.png").resize((270,270)))
pimg_result=Label(window)
pimg_result.config(width=300,height=300)
pimg_result.place(x=550,y=100)
pimg_result.config(image=img_test)
#pimg_result = Label(window)


window.mainloop()




