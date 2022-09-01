import tkinter as tk
import time as t
import datetime as dt

ct = dt.datetime.now()

print("To Do List Python [RUNNING]", ct)

# Main Window Configuration
main_window = tk.Tk()
main_window.geometry("250x120")
main_window.title("ToDo Python")
main_window.resizable(False, False)

# Insert Event
def insert():
    mLabel1.forget()
    mEntry1.forget()
    mButton1.forget()
    mButton2.forget()

    def retryTdL():
        mLabel1.pack()
        mEntry1.pack()
        mButton1.pack(pady=10)
        mButton2.pack(pady=1)
        iLabel1.forget()
        iButton1.forget()
        main_window.geometry("250x120")

    with open("ToDo List.dat","a") as f:
        f.write(mEntry1.get())
        f.write("\n")

    main_window.geometry("250x80")
    iLabel1 = tk.Label(main_window, text="List has been Inserted!", font=("Arial", 17))
    iButton1 = tk.Button(main_window, text="Retry", width=10, command=retryTdL, font=("Arial", 12), )
    iLabel1.pack()
    iButton1.pack()

# Close Event
def close():
    print("To Do List Python [STOPPED]", ct)
    quit()

# Widget
mLabel1 = tk.Label(main_window, text="Insert List:")
mEntry1 = tk.Entry(main_window, width=25)
mButton1 = tk.Button(main_window, width=10, text="Insert", command=insert)
mButton2 = tk.Button(main_window, width=10, text="Close", command=close)

# Packing
mLabel1.pack()
mEntry1.pack()
mButton1.pack(pady=10)
mButton2.pack(pady=1)
main_window.mainloop()
