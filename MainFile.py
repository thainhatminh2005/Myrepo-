from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk
from random import Random
import json


def chonmau():
    a, b = askcolor()
    print(b, a)
class top_bar(Frame):
    def __init__(self):
        self.load_image()
        #widget on bar
        Frame.__init__(self, window, bg = '#a4ffa4', border = 1, relief = SUNKEN)
        self.pack_configure(side = TOP, anchor = N, fill = X, padx = 3, pady = 3, expand = True)
        self.back_button = Button(self, image=self.back_disable_imageTk)
        self.back_button.image = self.back_disable_imageTk
        self.back_button.pack_configure(side=LEFT)
        self.next_button = Button(self, image=self.next_disable_imageTk)
        self.next_button.image = self.next_disable_imageTk
        self.next_button.pack_configure(side=RIGHT)
    def load_image(self):
        # load image
        back_able_image = Image.open('back_able.jpg')
        self.back_able_imageTk = ImageTk.PhotoImage(back_able_image)
        back_disable_image = Image.open('back_disable.jpg')
        self.back_disable_imageTk = ImageTk.PhotoImage(back_disable_image)
        next_able_image = Image.open('next_able.jpg')
        self.next_able_imageTk = ImageTk.PhotoImage(next_able_image)
        next_disable_image = Image.open('next_disable.jpg')
        self.next_disable_imageTk = ImageTk.PhotoImage(next_disable_image)
    def disable_next_button(self):
        self.next_button.configure(image = self.next_disable_imageTk)
    def able_next_button(self):
        self.next_button.configure(image = self.next_able_imageTk)
    def disable_back_button(self):
        self.back_button.configure(image = self.back_disable_imageTk)
    def able_button_button(self):
        self.back_button.configure(image = self.back_able_imageTk)

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
    def event(self, combo_name, event_number):
        file_event = open(self.filename, 'r')
        data = json.load(file_event)
        data_event = data[combo_name]
        list_event = data_event.key()
        event = list_event[event_number]
        return event
class manage_page(Frame):
    def __init__(self):
        Frame.__init__(self, window, bg='#000000', height=269)
        self.pack_configure(fill=BOTH, expand=True)
        #Create page
        self.top_bar = top_bar()
        self.page_1st = page_1st(self)
        self.page_change_event = page_change_event(self)
        self.page_choose_combo = page_choose_combo(self)
        self.page_create = page_create(self)
        self.page_create_combo = page_create_combo(self)
        self.page_create_event = page_create_event(self)
        self.page_repair_event = page_repair_event(self)
        self.page_see_combo = page_see_combo(self)
        self.page_see_event = page_see_event(self)
        self.list = [self.page_change_event,self.page_choose_combo,
                     self.page_create, self.page_create_combo, self.page_create_event,
                     self.page_repair_event, self.page_see_combo, self.page_see_event]
        #End create page
        for page in self.list:
            self.page_1st.tkraise(page)
    def show(self, page):
        page.tkraise()
        try:
            self.list_page.index(page)
        except:
            try:
                index_now_page = self.list_page.index(self.page_now)
                index_next_page = index_now_page + 1
                next_page = self.list_page[index_next_page]
                if not page is next_page:
                    del self.list_page[index_next_page:-1]
                self.list_page.append(page)
            except:
                self.list_page = [page]
        self.page_now = page
        self.check_ability()
    def check_ability(self):
        index_now_page = self.list_page.index(self.page_now)
        try:
            index_next_page = index_now_page + 1
            next_page = self.list_page[index_next_page]
            show_next_page = self.show(next_page)
            image = self.top_bar.next_able_imageTk
            self.top_bar.next_button.configure(image = image,command = show_next_page)
        except:
            image = self.top_bar.next_disable_imageTk
            self.top_bar.next_button.configure(image=image, command=None)
        if index_now_page == 0:
            image = self.top_bar.back_disable_imageTk
            self.top_bar.back_button.configure(image=image, command=None)
        else:
            index_back_page = index_now_page - 1
            back_page = self.list_page[index_back_page]
            show_back_page = self.show(back_page)
            image = self.top_bar.back_able_imageTk
            self.top_bar.next_button.configure(image = image,command = show_back_page)

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
        Frame.__init__(self, parent)
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


class page_repair_event(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
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
        text_event = Text(frame_event, height=4, width=50)
        text_event.pack_configure(side=RIGHT)
        text_event.insert(END, '')
        label_event = Label(frame_event, text='Nhập sự kiện')
        label_event.pack_configure(side=LEFT, anchor=N)
        frame_date = Frame(self)
        frame_date.pack_configure()
        label_day = Label(frame_date, text='Ngày')
        label_day.pack_configure(side=LEFT)
        entry_day = Entry(frame_date, width=2)
        entry_day.pack_configure(side=LEFT)
        entry_day.insert(END, '')
        label_month = Label(frame_date, text='Tháng')
        label_month.pack_configure(side=LEFT)
        entry_month = Entry(frame_date, width=2)
        entry_month.pack_configure(side=LEFT)
        entry_month.insert(END, '')
        label_year = Label(frame_date, text='Năm')
        label_year.pack_configure(side=LEFT)
        entry_year = Entry(frame_date, width=4)
        entry_year.pack_configure(side=LEFT)
        entry_year.insert(END, '')
        button = Button(self, text='Save')
        button.pack_configure(side=RIGHT)


class page_create_event(Frame):
    def __init(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        frame_event = Frame(self)
        frame_event.pack_configure()
        text_event = Text(frame_event, height=4, width=50)
        text_event.pack_configure(side=RIGHT)
        label_event = Label(frame_event, text='Nhập sự kiện')
        label_event.pack_configure(side=LEFT, anchor=N)
        frame_date = Frame(self)
        frame_date.pack_configure()
        label_day = Label(frame_date, text='Ngày')
        label_day.pack_configure(side=LEFT)
        entry_day = Entry(frame_date, width=2)
        entry_day.pack_configure(side=LEFT)
        label_month = Label(frame_date, text='Tháng')
        label_month.pack_configure(side=LEFT)
        entry_month = Entry(frame_date, width=2)
        entry_month.pack_configure(side=LEFT)
        label_year = Label(frame_date, text='Năm')
        label_year.pack_configure(side=LEFT)
        entry_year = Entry(frame_date, width=4)
        entry_year.pack_configure(side=LEFT)
        frame_button = Frame(self, border = 1, relief = SUNKEN)
        frame_button.pack_configure(side=BOTTOM, anchor=E, padx=10)
        button_1st = Button(frame_button, text='Tiếp tục')
        button_1st.pack_configure(pady=5, side=RIGHT)
        button_2nd = Button(frame_button, text='hoàn thành')
        button_2nd.pack_configure(side=RIGHT)

class page_create_combo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        label = Label(self, text='Nhập tên bộ')
        label.pack_configure()
        entry = Entry(self, width=50)
        entry.pack_configure()
        button = Button(self, text='Tạo')
        button.pack_configure(pady=5)

class page_choose_combo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        label = Label(self, text='Chọn bộ sự kiện kiểm tra của bạn')
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
        button = Button(self, text='Enter')
        button.pack_configure(pady=5)

class khungtaosk(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(fill=BOTH, expand=True)
        label_question = Label(self, text='')
        label_question.pack_configure()
        frame_answer = Frame(self)
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
        frame_button = Frame(self)
        frame_button.pack_configure(side=BOTTOM, anchor=E, padx=10)
        button_1st = Button(frame_button, text='Tiếp tục')
        button_1st.pack_configure(pady=5, side=RIGHT)
        button_2nd = Button(frame_button, text='hoàn thành')
        button_2nd.pack_configure(side=RIGHT)

class minipage_complete(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack_configure(expand=True)
        label_1st = Label(self, text='Hoàn thành')
        label_1st.pack_configure()
        label_2nd = Label(self, text='Trả lời đúng' + 'trên' + 'câu')
        label_2nd.pack_configure()

#TAO MAN HINH
window = Tk()
window.wm_title('History Event')
window.wm_resizable(0,0)
window.wm_geometry('500x300+400+200')
Example = manage_page()

window.mainloop()
