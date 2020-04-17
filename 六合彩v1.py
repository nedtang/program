# uncompyle6 version 3.6.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)]
# Embedded file name: E:\new\666\min\迷你联通.py
# Size of source mod 2**32: 327379 bytes
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
root = Tk()
root.title('主界面')
g1 = Frame(root)
g2 = Frame(root)
g3 = Frame(root)
root.geometry('1600x800+100+100')
ft = tkFont.Font(size=15)
total101 = 0
total102 = 0
total103 = 0
total104 = 0
total105 = 0
total106 = 0
total107 = 0
total108 = 0
total109 = 0
total110 = 0
total111 = 0
total112 = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0
total8 = 0
total9 = 0
total10 = 0
total11 = 0
total12 = 0
total13 = 0
total14 = 0
total15 = 0
total16 = 0
total17 = 0
total18 = 0
total19 = 0
total20 = 0
total21 = 0
total22 = 0
total23 = 0
total24 = 0
total25 = 0
total26 = 0
total27 = 0
total28 = 0
total29 = 0
total30 = 0
total31 = 0
total32 = 0
total33 = 0
total34 = 0
total35 = 0
total36 = 0
total37 = 0
total38 = 0
total39 = 0
total40 = 0
total41 = 0
total42 = 0
total43 = 0
total44 = 0
total45 = 0
total46 = 0
total47 = 0
total48 = 0
total49 = 0
Lt = Label(g1, text='总', font=ft).grid(row=0, column=12)
LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
Lx = Label(g1, text='肖总', font=ft).grid(row=1, column=12)
LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)
Lz = Label(g1, text='字总', font=ft).grid(row=2, column=12)
LZ = Label(g1, font=ft, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49)).grid(row=2, column=13)
try:
    L101 = Label(g1, text=total101, font=ft).grid(row=1, column=0)

    def create101():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total101
            x = e1.get()
            if x == '':
                x = 0
            total101 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入鼠+' + x), font=24, width=20).grid(row=0, column=0)
            L1 = Label(g1, text=total101, font=ft).grid(row=1, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B101 = Button(g1, text=' 鼠 ', command=create101, font=ft).grid(row=0, column=0)
    L102 = Label(g1, text=total102, font=ft).grid(row=1, column=1)

    def create102():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total102
            global x
            x = e1.get()
            if x == '':
                x = 0
            total102 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入牛+' + x), font=24, width=20).grid(row=0, column=0)
            L102 = Label(g1, text=total102, font=ft).grid(row=1, column=1)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B102 = Button(g1, text=' 牛 ', command=create102, font=ft).grid(row=0, column=1)
    L103 = Label(g1, text=total103, font=ft).grid(row=1, column=2)

    def create103():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total103
            global x
            x = e1.get()
            if x == '':
                x = 0
            total103 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入虎+' + x), font=24, width=20).grid(row=0, column=0)
            L103 = Label(g1, text=total103, font=ft).grid(row=1, column=2)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B103 = Button(g1, text=' 虎 ', command=create103, font=ft).grid(row=0, column=2)
    L104 = Label(g1, text=total104, font=ft).grid(row=1, column=3)

    def create104():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total104
            global x
            x = e1.get()
            if x == '':
                x = 0
            total104 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入兔+' + x), font=24, width=20).grid(row=0, column=0)
            L104 = Label(g1, text=total104, font=ft).grid(row=1, column=3)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B104 = Button(g1, text=' 兔 ', command=create104, font=ft).grid(row=0, column=3)
    L105 = Label(g1, text=total105, font=ft).grid(row=1, column=4)

    def create105():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total105
            global x
            x = e1.get()
            if x == '':
                x = 0
            total105 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入龙+' + x), font=24, width=20).grid(row=0, column=0)
            L105 = Label(g1, text=total105, font=ft).grid(row=1, column=4)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B105 = Button(g1, text=' 龙 ', command=create105, font=ft).grid(row=0, column=4)
    L106 = Label(g1, text=total106, font=ft).grid(row=1, column=5)

    def create106():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total106
            global x
            x = e1.get()
            if x == '':
                x = 0
            total106 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入蛇+' + x), font=24, width=20).grid(row=0, column=0)
            L106 = Label(g1, text=total106, font=ft).grid(row=1, column=5)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B106 = Button(g1, text=' 蛇 ', command=create106, font=ft).grid(row=0, column=5)
    L107 = Label(g1, text=total107, font=ft).grid(row=1, column=6)

    def create107():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total107
            global x
            x = e1.get()
            if x == '':
                x = 0
            total107 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入马+' + x), font=24, width=20).grid(row=0, column=0)
            L107 = Label(g1, text=total107, font=ft).grid(row=1, column=6)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B107 = Button(g1, text=' 马 ', command=create107, font=ft).grid(row=0, column=6)
    L108 = Label(g1, text=total108, font=ft).grid(row=1, column=7)

    def create108():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total108
            global x
            x = e1.get()
            if x == '':
                x = 0
            total108 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入羊+' + x), font=24, width=20).grid(row=0, column=0)
            L108 = Label(g1, text=total108, font=ft).grid(row=1, column=7)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=7)
        f2.pack()


    B108 = Button(g1, text=' 羊 ', command=create108, font=ft).grid(row=0, column=7)
    L109 = Label(g1, text=total109, font=ft).grid(row=1, column=8)

    def create109():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total109
            global x
            x = e1.get()
            if x == '':
                x = 0
            total109 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入猴+' + x), font=24, width=20).grid(row=0, column=0)
            L109 = Label(g1, text=total109, font=ft).grid(row=1, column=8)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B109 = Button(g1, text=' 猴 ', command=create109, font=ft).grid(row=0, column=8)
    L110 = Label(g1, text=total110, font=ft).grid(row=1, column=9)

    def create110():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total110
            global x
            x = e1.get()
            if x == '':
                x = 0
            total110 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入鸡+' + x), font=24, width=20).grid(row=0, column=0)
            L110 = Label(g1, text=total110, font=ft).grid(row=1, column=9)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B110 = Button(g1, text=' 鸡 ', command=create110, font=ft).grid(row=0, column=9)
    L111 = Label(g1, text=total111, font=ft).grid(row=1, column=10)

    def create111():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total111
            global x
            x = e1.get()
            if x == '':
                x = 0
            total111 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入狗+' + x), font=24, width=20).grid(row=0, column=0)
            L111 = Label(g1, text=total111, font=ft).grid(row=1, column=10)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B111 = Button(g1, text=' 狗 ', command=create111, font=ft).grid(row=0, column=10)
    L112 = Label(g1, text=total112, font=ft).grid(row=1, column=11)

    def create112():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total112
            global x
            x = e1.get()
            if x == '':
                x = 0
            total112 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入猪+' + x), font=24, width=20).grid(row=0, column=0)
            L112 = Label(g1, text=total112, font=ft).grid(row=1, column=11)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LX = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112), font=ft).grid(row=1, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B112 = Button(g1, text=' 猪 ', command=create112, font=ft).grid(row=0, column=11)
    L12 = Label(g1, text=total12, font=ft).grid(row=3, column=0)

    def create1():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total1
            global x
            x = e1.get()
            if x == '':
                x = 0
            total1 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入01+' + x), font=24, width=20).grid(row=0, column=0)
            L1 = Label(g1, text=total1, font=ft).grid(row=3, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B1 = Button(g1, text='(01)', command=create1, font=ft).grid(row=2, column=0)
    L11 = Label(g1, text=total11, font=ft).grid(row=3, column=2)

    def create11():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total11
            global x
            x = e1.get()
            if x == '':
                x = 0
            total11 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入11+' + x), font=24, width=20).grid(row=0, column=0)
            L2 = Label(g1, text=total11, font=ft).grid(row=3, column=2)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B11 = Button(g1, text='(11)', command=create11, font=ft).grid(row=2, column=2)
    L10 = Label(g1, text=total10, font=ft).grid(row=3, column=3)

    def create10():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total10
            global x
            x = e1.get()
            if x == '':
                x = 0
            total10 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入10+' + x), font=24, width=20).grid(row=0, column=0)
            L10 = Label(g1, text=total10, font=ft).grid(row=3, column=3)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B10 = Button(g1, text='(10)', command=create10, font=ft).grid(row=2, column=3)
    L9 = Label(g1, text=total9, font=ft).grid(row=3, column=4)

    def create9():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total9
            global x
            x = e1.get()
            if x == '':
                x = 0
            total9 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入09+' + x), font=24, width=20).grid(row=0, column=0)
            L9 = Label(g1, text=total9, font=ft).grid(row=3, column=4)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B9 = Button(g1, text='(09)', command=create9, font=ft).grid(row=2, column=4)
    L8 = Label(g1, text=total8, font=ft).grid(row=3, column=5)

    def create8():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total8
            global x
            x = e1.get()
            if x == '':
                x = 0
            total8 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入08+' + x), font=24, width=20).grid(row=0, column=0)
            L8 = Label(g1, text=total8, font=ft).grid(row=3, column=5)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B8 = Button(g1, text='(08)', command=create8, font=ft).grid(row=2, column=5)
    L7 = Label(g1, text=total7, font=ft).grid(row=3, column=6)

    def create7():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total7
            global x
            x = e1.get()
            if x == '':
                x = 0
            total7 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入07+' + x), font=24, width=20).grid(row=0, column=0)
            L7 = Label(g1, text=total7, font=ft).grid(row=3, column=6)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B7 = Button(g1, text='(07)', command=create7, font=ft).grid(row=2, column=6)
    L6 = Label(g1, text=total6, font=ft).grid(row=3, column=7)

    def create6():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total6
            global x
            x = e1.get()
            if x == '':
                x = 0
            total6 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入06+' + x), font=24, width=20).grid(row=0, column=0)
            L6 = Label(g1, text=total6, font=ft).grid(row=3, column=7)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B6 = Button(g1, text='(06)', command=create6, font=ft).grid(row=2, column=7)
    L5 = Label(g1, text=total5, font=ft).grid(row=3, column=8)

    def create5():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total5
            global x
            x = e1.get()
            if x == '':
                x = 0
            total5 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入05+' + x), font=24, width=20).grid(row=0, column=0)
            L5 = Label(g1, text=total5, font=ft).grid(row=3, column=8)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B5 = Button(g1, text='(05)', command=create5, font=ft).grid(row=2, column=8)
    L4 = Label(g1, text=total4, font=ft).grid(row=3, column=9)

    def create4():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total4
            global x
            x = e1.get()
            if x == '':
                x = 0
            total4 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入04+' + x), font=24, width=20).grid(row=0, column=0)
            L4 = Label(g1, text=total4, font=ft).grid(row=3, column=9)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B4 = Button(g1, text='(04)', command=create4, font=ft).grid(row=2, column=9)
    L3 = Label(g1, text=total3, font=ft).grid(row=3, column=10)

    def create3():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total3
            global x
            x = e1.get()
            if x == '':
                x = 0
            total3 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入03+' + x), font=24, width=20).grid(row=0, column=0)
            L3 = Label(g1, text=total3, font=ft).grid(row=3, column=10)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B3 = Button(g1, text='(03)', command=create3, font=ft).grid(row=2, column=10)
    L2 = Label(g1, text=total2, font=ft).grid(row=3, column=11)

    def create2():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total2
            global x
            x = e1.get()
            if x == '':
                x = 0
            total2 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入02+' + x), font=24, width=20).grid(row=0, column=0)
            L2 = Label(g1, text=total2, font=ft).grid(row=3, column=11)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B2 = Button(g1, text='(02)', command=create2, font=ft).grid(row=2, column=11)
    L12 = Label(g1, text=total12, font=ft).grid(row=3, column=1)

    def create12():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total12
            global x
            x = e1.get()
            if x == '':
                x = 0
            total12 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入12+' + x), font=24, width=20).grid(row=0, column=0)
            L12 = Label(g1, text=total12, font=ft).grid(row=3, column=1)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B1 = Button(g1, text='(12)', command=create12, font=ft).grid(row=2, column=1)
    L24 = Label(g1, text=total24, font=ft).grid(row=5, column=1)

    def create24():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total24
            global x
            x = e1.get()
            if x == '':
                x = 0
            total24 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入24+' + x), font=24, width=20).grid(row=0, column=0)
            L24 = Label(g1, text=total24, font=ft).grid(row=5, column=1)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B24 = Button(g1, text='(24)', command=create24, font=ft).grid(row=4, column=1)
    L23 = Label(g1, text=total24, font=ft).grid(row=5, column=2)

    def create23():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total23
            global x
            x = e1.get()
            if x == '':
                x = 0
            total23 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入23+' + x), font=24, width=20).grid(row=0, column=0)
            L23 = Label(g1, text=total23, font=ft).grid(row=5, column=2)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B23 = Button(g1, text='(23)', command=create23, font=ft).grid(row=4, column=2)
    L22 = Label(g1, text=total22, font=ft).grid(row=5, column=3)

    def create22():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total22
            global x
            x = e1.get()
            if x == '':
                x = 0
            total22 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入22+' + x), font=24, width=20).grid(row=0, column=0)
            L22 = Label(g1, text=total22, font=ft).grid(row=5, column=3)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=2)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B22 = Button(g1, text='(22)', command=create22, font=ft).grid(row=4, column=3)
    L21 = Label(g1, text=total21, font=ft).grid(row=5, column=4)

    def create21():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total21
            global x
            x = e1.get()
            if x == '':
                x = 0
            total21 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入21+' + x), font=24, width=20).grid(row=0, column=0)
            L21 = Label(g1, text=total21, font=ft).grid(row=5, column=4)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B21 = Button(g1, text='(21)', command=create21, font=ft).grid(row=4, column=4)
    L20 = Label(g1, text=total20, font=ft).grid(row=5, column=5)

    def create20():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total20
            global x
            x = e1.get()
            if x == '':
                x = 0
            total20 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入20+' + x), font=24, width=20).grid(row=0, column=0)
            L20 = Label(g1, text=total20, font=ft).grid(row=5, column=5)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B20 = Button(g1, text='(20)', command=create20, font=ft).grid(row=4, column=5)
    L19 = Label(g1, text=total19, font=ft).grid(row=5, column=6)

    def create19():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total19
            global x
            x = e1.get()
            if x == '':
                x = 0
            total19 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入19+' + x), font=24, width=20).grid(row=0, column=0)
            L19 = Label(g1, text=total19, font=ft).grid(row=5, column=6)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B19 = Button(g1, text='(19)', command=create19, font=ft).grid(row=4, column=6)
    L18 = Label(g1, text=total18, font=ft).grid(row=5, column=7)

    def create18():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total18
            global x
            x = e1.get()
            if x == '':
                x = 0
            total18 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入18+' + x), font=24, width=20).grid(row=0, column=0)
            L18 = Label(g1, text=total18, font=ft).grid(row=5, column=7)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B18 = Button(g1, text='(18)', command=create18, font=ft).grid(row=4, column=7)
    L17 = Label(g1, text=total17, font=ft).grid(row=5, column=8)

    def create17():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total17
            global x
            x = e1.get()
            if x == '':
                x = 0
            total17 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入17+' + x), font=24, width=20).grid(row=0, column=0)
            L17 = Label(g1, text=total17, font=ft).grid(row=5, column=8)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B17 = Button(g1, text='(17)', command=create17, font=ft).grid(row=4, column=8)
    L16 = Label(g1, text=total16, font=ft).grid(row=5, column=9)

    def create16():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total16
            global x
            x = e1.get()
            if x == '':
                x = 0
            total16 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入16+' + x), font=24, width=20).grid(row=0, column=0)
            L16 = Label(g1, text=total16, font=ft).grid(row=5, column=9)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B16 = Button(g1, text='(16)', command=create16, font=ft).grid(row=4, column=9)
    L15 = Label(g1, text=total15, font=ft).grid(row=5, column=10)

    def create15():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total15
            global x
            x = e1.get()
            if x == '':
                x = 0
            total15 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入15+' + x), font=24, width=20).grid(row=0, column=0)
            L15 = Label(g1, text=total15, font=ft).grid(row=5, column=10)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B15 = Button(g1, text='(15)', command=create15, font=ft).grid(row=4, column=10)
    L14 = Label(g1, text=total14, font=ft).grid(row=5, column=11)

    def create14():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total14
            global x
            x = e1.get()
            if x == '':
                x = 0
            total14 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入14+' + x), font=24, width=20).grid(row=0, column=0)
            L14 = Label(g1, text=total14, font=ft).grid(row=5, column=11)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B14 = Button(g1, text='(14)', command=create14, font=ft).grid(row=4, column=11)
    L13 = Label(g1, text=total13, font=ft).grid(row=5, column=0)

    def create13():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total13
            global x
            x = e1.get()
            if x == '':
                x = 0
            total13 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入13+' + x), font=24, width=20).grid(row=0, column=0)
            L13 = Label(g1, text=total13, font=ft).grid(row=5, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B13 = Button(g1, text='(13)', command=create13, font=ft).grid(row=4, column=0)
    L36 = Label(g1, text=total36, font=ft).grid(row=7, column=1)

    def create36():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total36
            global x
            x = e1.get()
            if x == '':
                x = 0
            total36 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入36+' + x), font=24, width=20).grid(row=0, column=0)
            L36 = Label(g1, text=total36, font=ft).grid(row=7, column=1)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B36 = Button(g1, text='(36)', command=create36, font=ft).grid(row=6, column=1)
    L35 = Label(g1, text=total35, font=ft).grid(row=7, column=2)

    def create35():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total35
            global x
            x = e1.get()
            if x == '':
                x = 0
            total35 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入35+' + x), font=24, width=20).grid(row=0, column=0)
            L35 = Label(g1, text=total35, font=ft).grid(row=7, column=2)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B35 = Button(g1, text='(35)', command=create35, font=ft).grid(row=6, column=2)
    L34 = Label(g1, text=total34, font=ft).grid(row=7, column=3)

    def create34():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total34
            global x
            x = e1.get()
            if x == '':
                x = 0
            total34 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入34+' + x), font=24, width=20).grid(row=0, column=0)
            L34 = Label(g1, text=total34, font=ft).grid(row=7, column=3)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B34 = Button(g1, text='(34)', command=create34, font=ft).grid(row=6, column=3)
    L33 = Label(g1, text=total33, font=ft).grid(row=7, column=4)

    def create33():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total33
            global x
            x = e1.get()
            if x == '':
                x = 0
            total33 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入33+' + x), font=24, width=20).grid(row=0, column=0)
            L33 = Label(g1, text=total33, font=ft).grid(row=7, column=4)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B33 = Button(g1, text='(33)', command=create33, font=ft).grid(row=6, column=4)
    L32 = Label(g1, text=total32, font=ft).grid(row=7, column=5)

    def create32():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total32
            global x
            x = e1.get()
            if x == '':
                x = 0
            total32 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入32+' + x), font=24, width=20).grid(row=0, column=0)
            L32 = Label(g1, text=total32, font=ft).grid(row=7, column=5)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B32 = Button(g1, text='(32)', command=create32, font=ft).grid(row=6, column=5)
    L31 = Label(g1, text=total31, font=ft).grid(row=7, column=6)

    def create31():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total31
            global x
            x = e1.get()
            if x == '':
                x = 0
            total31 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入31+' + x), font=24, width=20).grid(row=0, column=0)
            L31 = Label(g1, text=total31, font=ft).grid(row=7, column=6)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B31 = Button(g1, text='(31)', command=create31, font=ft).grid(row=6, column=6)
    L30 = Label(g1, text=total30, font=ft).grid(row=7, column=7)

    def create30():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total30
            global x
            x = e1.get()
            if x == '':
                x = 0
            total30 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入30+' + x), font=24, width=20).grid(row=0, column=0)
            L30 = Label(g1, text=total30, font=ft).grid(row=7, column=7)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B30 = Button(g1, text='(30)', command=create30, font=ft).grid(row=6, column=7)
    L29 = Label(g1, text=total29, font=ft).grid(row=7, column=8)

    def create29():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total29
            global x
            x = e1.get()
            if x == '':
                x = 0
            total29 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入29+' + x), font=24, width=20).grid(row=0, column=0)
            L29 = Label(g1, text=total29, font=ft).grid(row=7, column=8)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B29 = Button(g1, text='(29)', command=create29, font=ft).grid(row=6, column=8)
    L28 = Label(g1, text=total36, font=ft).grid(row=7, column=9)

    def create28():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total28
            global x
            x = e1.get()
            if x == '':
                x = 0
            total28 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入28+' + x), font=24, width=20).grid(row=0, column=0)
            L28 = Label(g1, text=total28, font=ft).grid(row=7, column=9)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B28 = Button(g1, text='(28)', command=create28, font=ft).grid(row=6, column=9)
    L27 = Label(g1, text=total27, font=ft).grid(row=7, column=10)

    def create27():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total27
            global x
            x = e1.get()
            if x == '':
                x = 0
            total27 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入27+' + x), font=24, width=20).grid(row=0, column=0)
            L27 = Label(g1, text=total27, font=ft).grid(row=7, column=10)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B27 = Button(g1, text='(27)', command=create27, font=ft).grid(row=6, column=10)
    L26 = Label(g1, text=total26, font=ft).grid(row=7, column=11)

    def create26():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total26
            global x
            x = e1.get()
            if x == '':
                x = 0
            total26 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入26+' + x), font=24, width=20).grid(row=0, column=0)
            L26 = Label(g1, text=total26, font=ft).grid(row=7, column=11)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B26 = Button(g1, text='(26)', command=create26, font=ft).grid(row=6, column=11)
    L25 = Label(g1, text=total25, font=ft).grid(row=7, column=0)

    def create25():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total25
            global x
            x = e1.get()
            if x == '':
                x = 0
            total25 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入25+' + x), font=24, width=20).grid(row=0, column=0)
            L25 = Label(g1, text=total25, font=ft).grid(row=7, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B25 = Button(g1, text='(25)', command=create25, font=ft).grid(row=6, column=0)
    L48 = Label(g1, text=total48, font=ft).grid(row=9, column=1)

    def create48():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total48
            global x
            x = e1.get()
            if x == '':
                x = 0
            total48 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入48+' + x), font=24, width=20).grid(row=0, column=0)
            L48 = Label(g1, text=total48, font=ft).grid(row=9, column=1)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B48 = Button(g1, text='(48)', command=create48, font=ft).grid(row=8, column=1)
    L47 = Label(g1, text=total47, font=ft).grid(row=9, column=2)

    def create47():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total47
            global x
            x = e1.get()
            if x == '':
                x = 0
            total47 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入47+' + x), font=24, width=20).grid(row=0, column=0)
            L47 = Label(g1, text=total47, font=ft).grid(row=9, column=2)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B47 = Button(g1, text='(47)', command=create47, font=ft).grid(row=8, column=2)
    L46 = Label(g1, text=total46, font=ft).grid(row=9, column=3)

    def create46():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total46
            global x
            x = e1.get()
            if x == '':
                x = 0
            total46 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入46+' + x), font=24, width=20).grid(row=0, column=0)
            L46 = Label(g1, text=total46, font=ft).grid(row=9, column=3)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B46 = Button(g1, text='(46)', command=create46, font=ft).grid(row=8, column=3)
    L45 = Label(g1, text=total45, font=ft).grid(row=9, column=4)

    def create45():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total45
            global x
            x = e1.get()
            if x == '':
                x = 0
            total45 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入45+' + x), font=24, width=20).grid(row=0, column=0)
            L45 = Label(g1, text=total45, font=ft).grid(row=9, column=4)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B45 = Button(g1, text='(45)', command=create45, font=ft).grid(row=8, column=4)
    L44 = Label(g1, text=total44, font=ft).grid(row=9, column=5)

    def create44():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total44
            global x
            x = e1.get()
            if x == '':
                x = 0
            total44 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入44+' + x), font=24, width=20).grid(row=0, column=0)
            L44 = Label(g1, text=total44, font=ft).grid(row=9, column=5)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B44 = Button(g1, text='(44)', command=create44, font=ft).grid(row=8, column=5)
    L43 = Label(g1, text=total43, font=ft).grid(row=9, column=6)

    def create43():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total43
            global x
            x = e1.get()
            if x == '':
                x = 0
            total43 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入43+' + x), font=24, width=20).grid(row=0, column=0)
            L43 = Label(g1, text=total43, font=ft).grid(row=9, column=6)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B43 = Button(g1, text='(43)', command=create43, font=ft).grid(row=8, column=6)
    L42 = Label(g1, text=total42, font=ft).grid(row=9, column=7)

    def create42():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total42
            global x
            x = e1.get()
            if x == '':
                x = 0
            total42 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入42+' + x), font=24, width=20).grid(row=0, column=0)
            L42 = Label(g1, text=total42, font=ft).grid(row=9, column=7)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B42 = Button(g1, text='(42)', command=create42, font=ft).grid(row=8, column=7)
    L41 = Label(g1, text=total41, font=ft).grid(row=9, column=8)

    def create41():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total41
            global x
            x = e1.get()
            if x == '':
                x = 0
            total41 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入41+' + x), font=24, width=20).grid(row=0, column=0)
            L41 = Label(g1, text=total41, font=ft).grid(row=9, column=8)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B41 = Button(g1, text='(41)', command=create41, font=ft).grid(row=8, column=8)
    L40 = Label(g1, text=total40, font=ft).grid(row=9, column=9)

    def create40():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total40
            global x
            x = e1.get()
            if x == '':
                x = 0
            total40 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入40+' + x), font=24, width=20).grid(row=0, column=0)
            L40 = Label(g1, text=total40, font=ft).grid(row=9, column=9)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B40 = Button(g1, text='(40)', command=create40, font=ft).grid(row=8, column=9)
    L39 = Label(g1, text=total39, font=ft).grid(row=9, column=10)

    def create39():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total39
            global x
            x = e1.get()
            if x == '':
                x = 0
            total39 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入39+' + x), font=24, width=20).grid(row=0, column=0)
            L39 = Label(g1, text=total39, font=ft).grid(row=9, column=10)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B39 = Button(g1, text='(39)', command=create39, font=ft).grid(row=8, column=10)
    L38 = Label(g1, text=total38, font=ft).grid(row=9, column=11)

    def create38():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total38
            global x
            x = e1.get()
            if x == '':
                x = 0
            total38 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入38+' + x), font=24, width=20).grid(row=0, column=0)
            L38 = Label(g1, text=total38, font=ft).grid(row=9, column=11)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B38 = Button(g1, text='(38)', command=create38, font=ft).grid(row=8, column=11)
    L37 = Label(g1, text=total37, font=ft).grid(row=9, column=0)

    def create37():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total37
            global x
            x = e1.get()
            if x == '':
                x = 0
            total37 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            top.destroy()
            Label(g2, text=('上一次输入37+' + x), font=24, width=20).grid(row=0, column=0)
            L37 = Label(g1, text=total37, font=ft).grid(row=9, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B37 = Button(g1, text='(37)', command=create37, font=ft).grid(row=8, column=0)
    L49 = Label(g1, text=total49, font=ft).grid(row=11, column=0)

    def create49():
        top = Toplevel()
        top.geometry('500x400+500+400')
        top.title('+')

        def save_num(event=None):
            global total49
            global tt
            global x
            x = e1.get()
            if x == '':
                x = 0
            total49 += int(x)
            tt = {'01':total1 + total101 / 5,  '02':total2 + total112 / 4,  '03':total3 + total111 / 4,  '04':total4 + total110 / 4,  '05':total5 + total109 / 4,  '06':total6 + total108 / 4,  '07':total7 + total107 / 4,  '08':total8 + total106 / 4,  '09':total9 + total105 / 4,  '10':total10 + total104 / 4,  '11':total11 + total103 / 4,  '12':total12 + total102 / 4,  '13':total13 + total101 / 5,  '14':total14 + total112 / 4,  '15':total15 + total111 / 4,  '16':total16 + total110 / 4,  '17':total17 + total109 / 4,  '18':total18 + total108 / 4,  '19':total19 + total107 / 4,  '20':total20 + total106 / 4,  '21':total21 + total105 / 4,  '22':total22 + total104 / 4,  '23':total23 + total103 / 4,  '24':total24 + total102 / 4,  '25':total25 + total101 / 5,  '26':total26 + total112 / 4,  '27':total27 + total111 / 4,  '28':total28 + total110 / 4,  '29':total29 + total109 / 4,  '30':total30 + total108 / 4,  '31':total31 + total107 / 4,  '32':total32 + total106 / 4,  '33':total33 + total105 / 4,  '34':total34 + total104 / 4,  '35':total35 + total103 / 4,  '36':total36 + total102 / 4,  '37':total37 + total101 / 5,  '38':total38 + total112 / 4,  '39':total39 + total111 / 4,  '40':total40 + total110 / 4,  '41':total41 + total109 / 4,  '42':total42 + total108 / 4,  '43':total43 + total107 / 4,  '44':total44 + total106 / 4,  '45':total45 + total105 / 4,  '46':total46 + total104 / 4,  '47':total47 + total103 / 4,  '48':total48 + total102 / 4,  '49':total49 + total101 / 5}
            ttt = sorted((tt.items()), key=(lambda item: item[1]), reverse=True)
            tttt = ''
            tttt2 = ''
            tttt3 = ''
            for i in ttt[:17]:
                tttt = tttt + ''.join(str(i)) + '\n'

            for i in ttt[17:34]:
                tttt2 = tttt2 + ''.join(str(i)) + '\n'

            for i in ttt[34:49]:
                tttt3 = tttt3 + ''.join(str(i)) + '\n'

            top.destroy()
            Label(g3, text=tttt, font=ft).grid(row=0, column=1)
            Label(g3, text=tttt2, font=ft).grid(row=0, column=2)
            Label(g3, text=tttt3, font=ft).grid(row=0, column=3)
            Label(g2, text=('上一次输入49+' + x), font=24, width=20).grid(row=0, column=0)
            L49 = Label(g1, text=total49, font=ft).grid(row=11, column=0)
            LT = Label(g1, text=(total101 + total102 + total103 + total104 + total105 + total106 + total107 + total108 + total109 + total110 + total111 + total112 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=0, column=13)
            LZ = Label(g1, text=(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17 + total18 + total19 + total20 + total21 + total22 + total23 + total24 + total25 + total26 + total27 + total28 + total29 + total30 + total31 + total32 + total33 + total34 + total35 + total36 + total37 + total38 + total39 + total40 + total41 + total42 + total43 + total44 + total45 + total46 + total47 + total48 + total49), font=ft).grid(row=2, column=13)

        f1 = Frame(top)
        e1 = Entry(f1, width=10, font=ft)
        e1.focus()
        e1.bind('<Return>', save_num)
        e1.grid(row=1, column=0, padx=20, pady=20)
        Button(f1, text='ok', command=save_num, font=ft).grid(row=1, column=1)
        f1.pack()
        f2 = Frame(top)

        def insert_point_0():
            e1.insert('insert', 0)

        Button(f2, text=0, font=ft, command=insert_point_0).grid(row=0, column=0)

        def insert_point_1():
            e1.insert('insert', 1)

        Button(f2, text=1, font=ft, command=insert_point_1).grid(row=0, column=1)

        def insert_point_2():
            e1.insert('insert', 2)

        Button(f2, text=2, font=ft, command=insert_point_2).grid(row=0, column=2)

        def insert_point_3():
            e1.insert('insert', 3)

        Button(f2, text=3, font=ft, command=insert_point_3).grid(row=0, column=3)

        def insert_point_4():
            e1.insert('insert', 4)

        Button(f2, text=4, font=ft, command=insert_point_4).grid(row=0, column=4)

        def insert_point_5():
            e1.insert('insert', 5)

        Button(f2, text=5, font=ft, command=insert_point_5).grid(row=1, column=0)

        def insert_point_6():
            e1.insert('insert', 6)

        Button(f2, text=6, font=ft, command=insert_point_6).grid(row=1, column=1)

        def insert_point_7():
            e1.insert('insert', 7)

        Button(f2, text=7, font=ft, command=insert_point_7).grid(row=1, column=2)

        def insert_point_8():
            e1.insert('insert', 8)

        Button(f2, text=8, font=ft, command=insert_point_8).grid(row=1, column=3)

        def insert_point_9():
            e1.insert('insert', 9)

        Button(f2, text=9, font=ft, command=insert_point_9).grid(row=1, column=4)

        def del_point():
            e1.delete(int(len(e1.get())) - 1)

        Button(f2, text='删除', font=ft, command=del_point, width=3).grid(row=0, column=5)
        f2.pack()


    B49 = Button(g1, text='(49)', command=create49, font=ft).grid(row=10, column=0)
except:
    pass
else:
    g1.grid(row=0, column=0)
    g2.grid(row=1, column=0)
    g3.grid(row=0, column=1)
    root.mainloop()
