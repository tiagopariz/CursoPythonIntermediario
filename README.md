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

## Adicionando controles

Crie um arquivo chamado controls-window.py

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

## Crie um banco de dados

Crie um arquivo chamado database.db e crie a tabela product

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
    # Run 
        self.get_products()

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

## Exiba os dados no formulário

Crie um arquivo chamado sql-table-window.py

```python
        # cleaning table
        records = self.tree.get_children() # Elementos da tabela
        for element in records:
            self.tree.delete(element)
```