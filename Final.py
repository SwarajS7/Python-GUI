#import necessary libraries needed for the code

import mysql.connector as m
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import webbrowser


def search_club():
    a = entry.get()
    query = "SELECT champions, COUNT(champions) from uclwinners where champions like %s group by champions;"
    para = ('%' + a + '%',)
    cursor.execute(query, para)

    result = cursor.fetchall()
    result_text.delete(1.0, tk.END)

    if result:
        for record in result:
            champion = record[0]
            count = record[1]
            query_years = "select years from uclwinners where champions = %s"
            cursor.execute(query_years, (champion,))
            years_result = cursor.fetchall()
            years_won = ','.join(str(year[0]) for year in years_result)
            result_text.insert(tk.END, f"Club Name : {champion}\nNumber of times UCl Won: {count}\nYears won: {years_won}\n")
    else:
        result_text.insert(tk.END, "No result found.")


def year_winners():
    b = entry.get()
    query = "select champions,Runnerup from uclwinners where years=%s;"
    para = (b,)
    cursor.execute(query, para)
    result2 = cursor.fetchall()
    result_text.delete(1.0, tk.END)

    if result2:
        for record in result2:
            champion = record[0]
            runner_up = record[1]
            result_text.insert(tk.END, f"champion club:{champion}\nRunner up team: {runner_up}\n")

    else:
        result_text.insert(tk.END, "No result found")


def runners_club():
    c = entry.get()
    query = "SELECT Runnerup, COUNT(Runnerup) from uclwinners where Runnerup like %s group by Runnerup;"
    para = ('%' + c + '%',)
    cursor.execute(query, para)

    result = cursor.fetchall()
    result_text.delete(1.0, tk.END)

    if result:
        for record in result:
            runnerup = record[0]
            count = record[1]
            query_years = "select years from uclwinners where Runnerup = %s"
            cursor.execute(query_years, (runnerup,))
            years_result = cursor.fetchall()
            years_won = ','.join(str(year[0]) for year in years_result)
            result_text.insert(tk.END, f"Club Name : {runnerup}\nNumber of times UCl Runner up: {count}\nYears team came Second: {years_won}\n")
    else:
        result_text.insert(tk.END, "No result found.")


def link():
    webbrowser.open_new(r"https://www.uefa.com/MultimediaFiles/Download/EuroExperience/competitions/Publications/02/28/56/89/2285689_DOWNLOAD.pdf")

def link2():
    webbrowser.open_new(r"https://www.uefa.com/uefachampionsleague/history/")

def newentry():
    #    mydatabase=m.connect(host="localhost",user="root",password="12345")
    #    cursor=mydatabase.cursor()
        years=int(new_years_entry.get())
        champions=new_champions_entry.get()
        runner_up=new_runnerup_entry.get()
            
        query="insert into uclwinners(years,champions,Runnerup) values(%s,%s,%s)"
        values=(years,champions,runner_up)
        cursor.execute(query,values)
        mydatabase.commit()
        result_text.delete(1.0,tk.END)
        result_text.insert(tk.END,"new entry added successfully")


def close():
    cursor.close()
    mydatabase.close()
    window.destroy()


mydatabase = m.connect(host="localhost", user="root", password="12345", database="UCL")
cursor = mydatabase.cursor()

window = tk.Tk()
window.title("UCL Search App")
window.geometry("900x700")
window.configure(bg="lightgrey")

input_frame = Frame(window, bg="red")
input_frame.pack(pady=10)

label = tk.Label(input_frame, text="Enter club name, years, or runner-up:", bg="purple", fg="white",font=("Arial", 14, "bold"))
label.pack(side=LEFT, padx=10)

entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
entry.pack(side=LEFT)

search_button = tk.Button(input_frame, text="Search", command=search_club, font=("Arial", 12, "bold"), bg="green",fg="white")
search_button.pack(side=LEFT, padx=10)

result_frame = Frame(window)
result_frame.pack(pady=10)

logo_image = ImageTk.PhotoImage(Image.open("gun__1381310671_uefa_champions_league.jpg").resize((600, 150)))
logo_label = Label(result_frame, image=logo_image)
logo_label.pack()

result_text = tk.Text(result_frame, width=80, height=10, font=("Helvetica", 12), bg="white", fg="black")
result_text.pack()

button_frame = Frame(window, bg="red")
button_frame.pack(pady=10)

# display_button=tk.Button(window,text="Display",command=search_club)
# display_button.pack()

year_search = tk.Button(button_frame, text="Years", command=year_winners, font=("Arial", 12, "bold"), bg="green",fg="white")
year_search.pack(side=LEFT, padx=10)

runner_search = tk.Button(button_frame, text="Runner-ups", command=runners_club, font=("Arial", 12, "bold"), bg="green",fg="white")
runner_search.pack(side=LEFT, padx=10)

Mainsite = tk.Button(window, text="UEFA Stats", command=link, font=("Arial", 12, "bold"), bg="blue", fg="white")
Mainsite.pack(pady=10)

Mainsite2 = tk.Button(window, text="History", command=link2, font=("Arial", 12, "bold"), bg="blue", fg="white")
Mainsite2.pack(pady=10)

new_years_label = tk.Label(window, text="Years:", bg="lightgray", font=("Arial", 12))
new_years_label.pack()
new_years_entry = tk.Entry(window, width=45, font=("Arial", 12))
new_years_entry.pack()

new_champions_label = tk.Label(window, text="Champions:", bg="lightgray", font=("Arial", 12))
new_champions_label.pack()
new_champions_entry = tk.Entry(window, width=45, font=("Arial", 12))
new_champions_entry.pack()

new_runnerup_label = tk.Label(window, text="Runner-up:", bg="lightgray", font=("Arial", 12))
new_runnerup_label.pack()
new_runnerup_entry = tk.Entry(window, width=45, font=("Arial", 12))
new_runnerup_entry.pack()

new_entry_button = tk.Button(window, text="Add New Entry", command=newentry, font=("Arial", 12, "bold"), bg="green", fg="white")
new_entry_button.pack(pady=10)

close_button = tk.Button(window, text="Close", command=close, font=("Arial", 12, "bold"), bg="red", fg="white")
close_button.pack()

window.mainloop()
