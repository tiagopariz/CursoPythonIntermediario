import os
from pathlib import Path
from tkinter import *

# OS Path
project_path = os.path.abspath(os.curdir)
images_path = project_path + '\\src\\parte2\\images'

menu_inicial = Tk()

menu_inicial.title('Menu')

# Dimension an position
window_width = 500
window_height = 300
screen_width = menu_inicial.winfo_screenwidth()
screen_height = menu_inicial.winfo_screenheight()
posx = screen_width / 2 - window_width / 2
posy = screen_height / 2 - window_height / 2
menu_inicial.geometry('%dx%d+%d+%d' % (window_width, window_height, posx, posy))
menu_inicial.resizable(True, True)
menu_inicial.minsize(width = window_width, height = window_height)
menu_inicial.maxsize(700, 300)
menu_inicial.state('iconic')

menu_inicial.iconbitmap(os.path.join(images_path, 'icon.ico'))
menu_inicial['bg'] = 'silver'

# label
label_1 = Label(menu_inicial,
                text = 'Nome: ',
                bg = '#C0C0C0',
                fg = 'black',
                font = 'Arial 14 bold italic')
label_1.pack()

# button
def cmd_Click(message):
    print(message)

cmd = Button(menu_inicial,
             text = 'Executar',
             command = lambda: cmd_Click('You clicked me!'))
cmd.pack()

menu_inicial.mainloop()