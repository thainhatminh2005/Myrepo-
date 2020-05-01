from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk
from random import Random
import json


def chonmau():
    a, b = askcolor()
    print(b, a)
def manhinhtren():
    back_image = Image.open('back.jpg')
    back_imageTk = ImageTk.PhotoImage(back_image)
    next_image = Image.open('next.jpg')
    next_imageTk = ImageTk.PhotoImage(next_image)

    frame = Frame(window, bg = '#a4ffa4', border = 1, relief = SUNKEN)
    frame.pack_configure(side = TOP, anchor = N, fill = X, padx = 3, pady = 3, expand = True)
    back_button = Button(frame, image=back_imageTk)
    back_button.image = back_imageTk
    back_button.pack_configure(side=LEFT)
    next_button = Button(frame, image=next_imageTk)
    next_button.image = next_imageTk
    next_button.pack_configure(side=RIGHT)
#filename: eventfile
class different_random():
    def __init__(self):
        self.list_number = []
    def different_random(self, end):
        while True:
            random_number = Random().randint(0, end)
            if not random_number in self.list_number:
                break
        self.list_number.append(random_number)
        return random_number
    def renew(self):
        self.list_number = []

class handling_file():
    def __init__(self, filename):
        self.filename = filename + '.json'
        try:
            open(self.filename)
        except:
            json.dump({},open(self.filename, 'w+'))
    def list_combo_event(self):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        return data.keys()
    def dictionary_event(self, combo_name):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        return data[combo_name]
    def add_event(self, combo_name, event, date):
        combo_event = self.dictionary_event(combo_name)
        combo_event[event] = date
        file_event = open(self.filename, 'w')
        json.dump(combo_event, file_event)
    def add_combo_event(self, combo_name):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        data[combo_name] = {}
        file_event = open(self.filename, 'w')
        json.dump(data, file_event)
# {combo:{event:[day, month, year]}}
    def delete_event(self,combo_name, event_number):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        data_event = data[combo_name]
        list_event = data_event.key()
        event = list_event[event_number]
        del event
    def count_event(self, combo_name):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        data_event = data[combo_name]
        number_of_event = len(data_event)
        return number_of_event

class manage_page(Frame):
    # All pages
    page_1st = page_1st(self)
    page_create = page_create(self)
    page_see_combo = page_see_combo(self)
    page_see_event = page_see_event(self)
    before_page = next_page = None
    def __init__(self):
        Frame.__init__(self, window, bg='#000000', height=269)
        self.pack_configure(fill=BOTH, expand=True)
        self.list_page = []
    def show(self, page):
        page.tkraise()
        self.now_page = page
    def add_page(self, new_page):
        if not self.next_page is new_page:
            del self.list_page[self.list_page.index([self.next_page]):-1]

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

class page_create(Frame):
    def __init__(self, parent):
        Frame.__init__ (self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        button_1st = Button(self, text='Tạo bộ mới', height=2, width=15)
        button_1st.pack_configure(pady=2)
        button_2nd = Button(self, text='Xem các bộ\nsự kiện đã có', height=2, width=15)
        button_2nd.pack_configure(pady=2)

class page_see_combo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        label = Label(self, text='Các bộ sự kiện đã có')
        label.pack_configure() 
        frame = Frame(self, width=300, height=200, bg='#00ffff')
        frame.pack_configure()
        scrollbar = Scrollbar(frame)
        scrollbar.pack_configure(side=RIGHT, fill=Y)
        listbox = Listbox(frame, width=75, yscrollcommand=scrollbar.set)
        for i in range(1, 10):
           listbox.insert(END, i)
        listbox.pack_configure(side=LEFT)
        scrollbar.configure(command=listbox.yview)
        button = Button(self, text='Xem')
        button.pack_configure(pady=5)


class page_see_event(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent())
        self.pack_configure(fill=BOTH, expand=True)
        label = Label(self, text='Các sự kiện')
        label.pack_configure()
        frame = Frame(self, width=300, height=200, bg='#00ffff')
        frame.pack_configure()
        scrollbar = Scrollbar(frame)
        scrollbar.pack_configure(side=RIGHT, fill=Y)
        listbox = Listbox(frame, width=75, yscrollcommand=scrollbar.set)
        for i in range(1, 100):
           listbox.insert(END, i)
        listbox.pack_configure(side=LEFT)
        scrollbar.configure(command=listbox.yview)
        button_1st = Button(self, text='Xem')
        button_1st.pack_configure(pady=5)
        button_2nd = Button(self, text='Thêm sự kiện')
        button_2nd.pack_configure(pady=5)


class page_create_event(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.pack_configure(fill=BOTH, expand=True)
        label_event = Label(self)
        label_event.pack_configure()
        label_date = Label(self)
        label_date.pack_configure()
        frame = Frame(self, border = 1, relief = SUNKEN)
        frame.pack_configure(fill=X, side=BOTTOM)
        button_1st = Button(frame, text='Xóa')
        button_1st.pack_configure(side=LEFT)
        button_2nd = Button(frame, text='Sửa')
        button_2nd.pack_configure(side=LEFT)
        button_3rd = Button(frame, text='Trước')
        button_3rd.pack_configure(side=RIGHT)
        button_4th = Button(frame, text='Sau')
        button_4th.pack_configure(side=RIGHT)


class page_change_event(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        frame_event = Frame(self)
        frame_event.pack_configure()
        text_event = Text(frame2, height=4, width=50)
        text_event.pack_configure(side=RIGHT)
        text_event.insert(END, '')
        label_event = Label(frame2, text='Nhập sự kiện')
        label_event.pack_configure(side=LEFT, anchor=N)
        frame_date = Frame(self)
        frame_date.pack_configure()
        label_day = Label(frame3, text='Ngày')
        label_day.pack_configure(side=LEFT)
        entry_day = Entry(frame3, width=2)
        entry_day.pack_configure(side=LEFT)
        entry_day.insert(END, '')
        label_month = Label(frame3, text='Tháng')
        label_month.pack_configure(side=LEFT)
        entry_month = Entry(frame3, width=2)
        entry_month.pack_configure(side=LEFT)
        entry_month.insert(END, '')
        label_year = Label(frame3, text='Năm')
        label_year.pack_configure(side=LEFT)
        entry_year = Entry(frame3, width=4)
        entry_year.pack_configure(side=LEFT)
        entry_year.insert(END, '')
        button = Button(frame, text='Save')
        button.pack_configure(side=RIGHT)


def khungtaosk(self):
    frame = Frame(self.frame)
    frame.pack_configure(fill=BOTH, expand=True)
    frame2 = Frame(frame)
    frame2.pack_configure()
    text_sk = Text(frame2, height=4, width=50)
    text_sk.pack_configure(side=RIGHT)
    label_sk = Label(frame2, text='Nhập sự kiện')
    label_sk.pack_configure(side=LEFT, anchor=N)
    frame3 = Frame(frame)
    frame3.pack_configure()
    label_day = Label(frame3, text='Ngày')
    label_day.pack_configure(side=LEFT)
    entry_day = Entry(frame3, width=2)
    entry_day.pack_configure(side=LEFT)
    label_month = Label(frame3, text='Tháng')
    label_month.pack_configure(side=LEFT)
    entry_month = Entry(frame3, width=2)
    entry_month.pack_configure(side=LEFT)
    label_year = Label(frame3, text='Năm')
    label_year.pack_configure(side=LEFT)
    entry_year = Entry(frame3, width=4)
    entry_year.pack_configure(side=LEFT)
    frame4 = Frame(frame)
    frame4.pack_configure(side=BOTTOM, anchor=E, padx=10)
    button1 = Button(frame4, text='Tiếp tục')
    button1.pack_configure(pady=5, side=RIGHT)
    button2 = Button(frame4, text='hoàn thành')
    button2.pack_configure(side=RIGHT)


def taobomoi(self):
    frame = Frame(self.frame)
    frame.pack_configure(fill=BOTH, expand=True)
    label_day = Label(frame, text='Nhập tên bộ')
    label_day.pack_configure()
    entry_day = Entry(frame, width=50)
    entry_day.pack_configure()
    button1 = Button(frame, text='Enter')
    button1.pack_configure(pady=5)


def chonbokt(self):
    frame = Frame(self.frame)
    frame.pack_configure(fill=BOTH, expand=True)
    label = Label(frame, text='Chọn bộ sự kiện kiểm tra của bạn')
    label.pack_configure()
    frame2 = Frame(frame, width=300, height=200, bg='#00ffff')
    frame2.pack_configure()
    scrollbar = Scrollbar(frame2)
    scrollbar.pack_configure(side=RIGHT, fill=Y)
    listbox = Listbox(frame2, width=75, yscrollcommand=scrollbar.set)
    for i in range(1, 100):
        listbox.insert(END, i)
    listbox.pack_configure(side=LEFT)
    scrollbar.configure(command=listbox.yview)
    button = Button(frame, text='Enter')
    button.pack_configure(pady=5)


def khungtaosk(self):
    frame = Frame(self.frame)
    frame.pack_configure(fill=BOTH, expand=True)
    label_question = Label(frame, text='')
    label_question.pack_configure()
    frame_answer = Frame(frame)
    frame_answer.pack_configure()
    label_day = Label(frame_answer, text='Ngày')
    label_day.pack_configure(side=LEFT)
    entry_day = Entry(frame_answer, width=2)
    entry_day.pack_configure(side=LEFT)
    label_month = Label(frame_answer, text='Tháng')
    label_month.pack_configure(side=LEFT)
    entry_month = Entry(frame_answer, width=2)
    entry_month.pack_configure(side=LEFT)
    label_year = Label(frame_answer, text='Năm')
    label_year.pack_configure(side=LEFT)
    entry_year = Entry(frame_answer, width=4)
    entry_year.pack_configure(side=LEFT)
    frame4 = Frame(frame)
    frame4.pack_configure(side=BOTTOM, anchor=E, padx=10)
    button1 = Button(frame4, text='Tiếp tục')
    button1.pack_configure(pady=5, side=RIGHT)
    button2 = Button(frame4, text='hoàn thành')
    button2.pack_configure(side=RIGHT)


def ht(self):
    frame = Frame(self.frame)
    frame.pack_configure(expand=True)
    label = Label(frame, text='Hoàn thành')
    label.pack_configure()
    label2 = Label(frame, text='Trả lời đúng' + 'trên' + 'câu')


#TAO MAN HINH
window = Tk()
window.wm_title('History Event')
window.wm_resizable(0,0)
window.wm_geometry('500x300+400+200')
manhinhtren()
jp = page1st()
window.mainloop()
