# Curso de Python Intermediário

# Parte 1 : Formulário window

Crie um formulário que funciona em Windows e Linux.

## Requisitos

- Visual Studio Code
- Extensão do Python para o VS Code
- Python 3.8.1
- Tkinter
- SQL Lite
- DB Browser for SQL Lite

## Crie uma janela

Crie um arquivo chamado basic-window.py

```python
from tkinter import ttk
from tkinter import *

class Product:
    def __init__(self, window):
        self.wind = window 
        self.wind.title('Products Application')

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python basic-window.py`

## Adicionando controles

Crie um arquivo chamado controls-window.py

Este arquivo usa o conceito de grid, como se fosse uma coluna

     0    1    2    3
  ---------------------
0 |    |    |    |    |
  ---------------------
1 |    |    |    |    |
  ---------------------
2 |    |    |    |    |
  ---------------------
3 |    |    |    |    |
  ---------------------

```python
from tkinter import ttk
from tkinter import *

class Product:
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

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python controls-window.py`

## Adicione um tabela

Crie um arquivo chamado table-window.py

```python
from tkinter import ttk
from tkinter import *

class Product:
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

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python table-window.py`

## Crie um banco de dados

Crie um arquivo chamado database.db e crie a tabela product

1. Abra o DB Browser
2. Clique em File e em seguida em New Database...
3. Navege até a raiz do projeto
4. Defina o nome como database.db
5. Clique em Create Table
6. Crie a tabela product 

```sql
CREATE TABLE "product" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"price"	REAL NOT NULL
);
```

Adicione alguns dados

1 Laptop 3000.00
2 Mouse 300.00

## Conecte com o SQLLite

Crie um arquivo chamado sqllite-window.py

```python
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
        self.get_products()

    # Run
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    def get_products(self):
        # quering data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            print(row)

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python sqllite-window.py`

## Exiba os dados no formulário

Crie um arquivo chamado sql-table-window.py

```python
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
```

Execute no terminal:

`python sql-table-window.py`

## Valide os dados

Crie um arquivo chamado validation-window.py

```python
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
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

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
            
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=  0
    
    def add_product(self):
        if self.validation():
            print(self.name.get())
            print(self.price.get())
        else:
            print('Name and price is required')

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python validation-window.py`

## Adicione dados

Crie um arquivo chamado add-window.py

```python
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
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

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

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=  0
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            print('Data saved')
        else:
            print('Name and price is required')
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python add-window.py`

## Exibindo mensagens

Crie um arquivo chamado messages-window.py

```python
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
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

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

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=  0
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Succesfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and price is required'
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python messages-window.py`

## Exclua dados

Crie um arquivo chamado delete-window.py

```python
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
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT').grid(row = 5, column = 1, sticky = W + E)

        # Filing the row
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

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=  0
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Succesfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and price is required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return        
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'Record {} deleted Succesfully'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python delete-window.py`

## Edite dados

Crie um arquivo chamado edit-window.py

```python
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
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # filing the row
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

        # Filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=  0
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Succesfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and price is required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return        
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'Record {} deleted Succesfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_win = Toplevel()
        self.edit_win.title = 'Edit Product'

        # Old Name
        Label(self.edit_win, text = 'Old Name: ').grid(row = 0, column = 1)
        Entry(self.edit_win, textvariable = StringVar(self.edit_win, value = name), state = 'readonly').grid(row = 0, column = 2)

        # New Name
        Label(self.edit_win, text = 'New Name: ').grid(row = 1, column = 1)
        new_name = Entry(self.edit_win)
        new_name.grid(row = 1, column = 2)

        # Old Price
        Label(self.edit_win, text = 'Old Price: ').grid(row = 2, column = 1)
        Entry(self.edit_win, textvariable = StringVar(self.edit_win, value = old_price), state = 'readonly').grid(row = 2, column = 2)

        # New Price
        Label(self.edit_win, text = 'New Price: ').grid(row = 3, column = 1)
        new_price = Entry(self.edit_win)
        new_price.grid(row = 3, column = 2)

        # Save Button
        Button(self.edit_win, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_win.destroy()
        self.message['text'] = 'Record {} updated Successfully'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
```

Execute no terminal:

`python edit-window.py`

01:05:00