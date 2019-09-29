from tkinter import *

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()






def root ():

    window_width = 1080
    window_height = 900
    root = Tk()
    window = Canvas(root, width=window_width, height=window_height, bg="black")
    window.create_rectangle(0,0, 1850, 55, fill="light blue", command=menu_window())




    window.pack()
    center(root)
    root.mainloop()



root()