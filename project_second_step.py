from tkinter import *


class Example:
    def __init__(self):
        self.master = Tk()
        self.wm = WordsMassive()
        self.label = Label(self.master, text='')
        self.label['font'] = 'Arial 20'
        self.label.grid(row=0, column=1)
        self.button_choose1 = Button(self.master, text='', command=self.change_button_colour_green)
        self.button_choose1.config(bg='lavender')
        self.button_choose1['font'] = 'Arial 17'
        self.button_choose1.grid(row=1, column=0)
        self.button_choose2 = Button(self.master, text='', command=self.change_button_colour_red)
        self.button_choose2.config(bg='lavender')
        self.button_choose2['font'] = 'Arial 17'
        self.button_choose2.grid(row=1, column=2)
        self.button_enter = Button(self.master, text='Начать', command=self.change_enter_word)
        self.button_enter.config(bg='CornflowerBlue')
        self.button_enter['font'] = 'Arial 15'
        self.button_enter.grid(row=3, column=1)
        self.master.mainloop()

    def change_enter_word(self):
        if self.button_enter:
            self.button_enter.config(text='Далее')

    def change_button_colour_green(self):
        if self.button_choose1:
            self.button_choose1.config(bg='green')
            self.label.config(text='')

    def change_button_colour_red(self):
        self.button_choose2.config(bg='red')
        self.label.config(text='донЕльзя')


class Word:
    def __init__(self, var, correct):
        self.variants = var
        self.correct = correct


class WordsMassive:
    def __init__(self):
        self.all_words = []
        for s in open('../../Downloads/words.txt').readlines():
            s = s.split()
            cor = s[0]
            var = s[:2]
            # перемешать
            self.all_words.append(Word(var, cor))
        print(self.all_words)





Example()
