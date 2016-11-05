from __future__ import division
import easygui
from easygui import *
import tkinter
from tkinter import *
import os
import csv
from tkinter import filedialog
import sys
import pickle
import subprocess
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet


class Meaning:

    

    def __init__(self, form):
        form.resizable(0,0)
        form.minsize(100, 100)
        form.title('DEFINATION')

        pad_x = 5
        pad_y = 5
        self.label1 = Label(form, text="Hello")
        self.textbox1 = Entry(form, width = 53)
        self.textbox1.focus_set()
        self.button1 = Button(form, text='Defination', command = self.Defination)
                
        self.scrollbar1 = Scrollbar(form)
        self.textarea2 = Text(form, width=40, height=10)
        self.textarea2.focus_set()
        self.textarea2.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textarea2.yview)

        self.textarea2.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky=W)
        #scrollbar1.grid(row=0, column=2, padx=pad_x, pady=pad_y, sticky=W)
        self.textbox1.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky=W)
        self.button1.grid(row=1, column=2, padx=pad_x, pady=pad_y, sticky=W)
        form.bind("<Return>", lambda x: self.Defination())


        form.mainloop()

    def Defination(self):
        txt = self.textbox1.get()
        word = txt.split(" ")
        lenght = len(word)
        for i in word:
            if(lenght<2):
                for a, b in enumerate(txt.split()):
                    print("Single word: ",b)
                    syns = wordnet.synsets(b)
                    example = (syns[0].examples())
                    example = (syns[0].examples())
                    tarea = self.textarea2.insert(END,"\n"+ b)
                    tarea = self.textarea2.insert(END,"\n"+(syns[0].definition()))
                    tarea = self.textarea2.insert(END,"\n"+ example)
                    self.textbox1.delete(0, END)
                    
            else:
                Error = "***Error: Single word Expected***"
                print(Error)
                tarea = self.textarea2.insert(END,"\n"+ Error)
                break

                

root = Tk()
Meaning(root)
