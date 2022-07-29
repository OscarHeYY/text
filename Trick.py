def popovers():
    import tkinter as tk
    import random
    import threading
    import time
    def dow():
        window = tk.Tk()
        window.title('you are a fool!!')
        window.geometry("300x75" + "+" + str(random.randrange(0, window.winfo_screenwidth())) + "+" + str(random.randrange(0, window.winfo_screenheight())))
        tk.Label(window,
                text='you are a fool!!!!!',
                bg='Blue',
                font=('幼圆', 17),
                width=20, height=2
                ).pack()
        window.mainloop()


    threads = []
    for i in range(100000000):
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.1)
        threads[i].start()
def uninstall():
    from tkinter import messagebox
    print("Are you sure you want to delete me?")
    print("Damn! Your computer should be infected with a virus!")
    messagebox.showinfo("uninstall...","uninstall...")
    import random
    print("\033[32;40m")
    while True:
        a = random.randint(1,5 )
        if a == 1:
            print("0",end="")
        if a == 2:
            print("1",end="")
        if a == 3:
            print("0110",end="")
        if a == 4:
            print("011",end="  ")
        if a == 5:
            print("——",end="  ")
            print("haha,your computer is infected with a virus!")
def github():
    import webbrowser
    import time
    while True:
        time.sleep(1)
        webbrowser.open('github.com')

