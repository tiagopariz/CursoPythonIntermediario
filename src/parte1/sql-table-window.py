from tkinter import ttk
from tkinter import *
import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window 
        self.wind.title('Products Application')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text = 'Register a new product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus() # Foco inicial
        self.name.grid(row = 1, column = 1)

        # Prince Input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Button Add Product
        ttk.Button(frame, text = 'Save Product').grid(row = 3, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)
        
        # get data
        self.get_products()

    # Run query
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    def get_products(self):
        # cleaning table
        records = self.tree.get_children() # Table elements
        for element in records:
            self.tree.delete(element)
        # quering data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()