#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk#used to style tkinter widgets 
from googletrans import Translator, LANGUAGES


# In[2]:


root = Tk()
root.geometry('1100x500')
root['bg']='skyblue'

root.title("Language Translator")
Label(root,text = "Language Translator", font = "arial 25 bold",bg="purple").pack()


# In[3]:


Label(root,text = "Enter Text", font = "arial 15 bold",bg="pink").place(x=165,y=90)


# In[4]:


input_text = Entry(root,width=60)
input_text.place(x=30,y=150)
input_text.get()


# In[5]:


Label(root,text="Translated",font = "arial 15 bold", bg="pink").place(x=865,y=90)
output_text=Text(root,font="arial 15 bold",height=5,wrap=WORD, padx=5, pady=5, width=25)
output_text.place(x=830,y=150)

language = list(LANGUAGES.values())
dest_lang=ttk.Combobox(root, values=language, width=25)
dest_lang.place(x=90,y=170)
dest_lang.set('Choose Language')


# In[6]:


def Translate():
    input_text_val = input_text.get()
    dest_language = dest_lang.get()
    if not input_text_val.strip():
        output_text.delete(1.0, END)
        output_text.insert(END, "Please enter text to translate.")
    elif dest_language == 'Choose Language':
        output_text.delete(1.0, END)
        output_text.insert(END, "Please choose a destination language.")
    else:
        translator = Translator()
        translated = translator.translate(text=input_text_val, dest=dest_language)
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)

translate_button = Button(root, text="Translate", font="arial 15 bold", pady=5, command=Translate, bg="yellow", activebackground="violet")
translate_button.place(x=525, y=100)

root.mainloop()

