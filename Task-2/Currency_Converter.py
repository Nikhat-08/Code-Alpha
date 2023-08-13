#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from currency_converter import CurrencyConverter
from tkinter import ttk
from forex_python.converter import CurrencyRates


# In[2]:


root = Tk()
root.geometry('500x500')
root['bg']='green'


# In[3]:


l1 = Label(root, text = "My Currency Converter", font = "Times 25 bold", bg = "purple", fg="skyblue").place(x = 550, y = 50)
l2 = Label(root, text="Enter Amount:", font = "Times 12 italic", bg = "orange", fg="white").place(x = 400, y = 180)

e1 = Entry(root,width=50)
e1.place(x = 520, y = 183)
e1.get()


# In[4]:


l3 = Label(root, text="Choose from Currency:", font = "Times 12 italic", bg = "orange", fg="white").place(x = 400, y = 208)
Currency_list= ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
Currency_list.sort()
convert=ttk.Combobox(root, value=Currency_list, width=25)
convert.place(x=580, y=208)
convert.set("Choose Currency")


# In[5]:


l4 = Label(root, text="Choose to Currency:", font = "Times 12 italic", bg = "orange", fg="white").place(x = 400, y = 238)
Currency_list1= ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
Currency_list1.sort()
convert1=ttk.Combobox(root, value=Currency_list1, width=25)
convert1.place(x=580, y=238)
convert1.set("Choose Currency")


# In[6]:


l5 = Label(root, text="The Amount is:", font = "Times 12 italic", bg = "orange", fg="white").place(x = 400, y = 268)

e2 = Entry(root,width=50)
e2.place(x = 520, y = 273)


# In[7]:


def Converter():
    c = CurrencyRates()
    from_currency = convert.get()
    to_currency = convert1.get()
    if not e1.get().strip():
        e2.delete(0, END)
        e2.insert(0, "Please enter some number to convert")
    elif from_currency == 'Choose Currency' or to_currency == 'Choose Currency':
        e2.delete(0, END)
        e2.insert(0, "Please choose currencies to convert")
    else:
        new_amt = c.convert(from_currency, to_currency, float(e1.get()))
        new_amount = round(new_amt, 4)
        e2.delete(0, END)
        e2.insert(0, str(new_amount))
convert_btn = Button(root, text='Convert', font='Times 18 bold', command=Converter, bg='yellow', fg='white')
convert_btn.place(x=520, y=313)
root.mainloop()

