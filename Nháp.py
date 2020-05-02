from PIL import Image, ImageTk
from tkinter import *

class page_1st(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        label = Label(self, text='Cùng nhau học sự kiện lịch sử')
        label.pack_configure()
        button_1st = Button(self, text='Tạo sự kiện', height=2, width=15)
        button_1st.pack_configure(pady=2)
        button_2nd = Button(self, text='Kiểm tra', height=2, width=15)
        button_2nd.pack_configure(pady=2)

class manage_page(Frame):
    def __init__(self):
        Frame.__init__(self, root, bg='#000000', height=269)
        self.pack_configure(fill=BOTH, expand=True)



root = Tk()
root.geometry("300x280+300+300")
app = Frame(root)

root.mainloop()


