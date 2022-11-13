import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


    def create_table_categories(self):
        sql = """CREATE TABLE Categories(
            text STRING NOT NULL UNIQUE,
            callback_data STRING NOT NULL UNIQUE
        );
        """
        self.execute(sql=sql, commit=True)

    def add_categories(self, text: str = None, callback_data: str = None):
        sql = """INSERT INTO Categories(text, callback_data) 
        VALUES(?, ?)
        """
        self.execute(sql=sql, parameters=(text, callback_data), commit=True)

    def select_categories(self):
        sql = """
        SELECT * FROM Categories
        """
        return self.execute(sql=sql, fetchall=True)

    def select_categories_callback_data(self):
        sql = """
        SELECT callback_data FROM Categories
        """
        return self.execute(sql=sql, fetchall=True)


    def create_table_inner_categories(self):
        sql = """CREATE TABLE Inner_categories(
            img varchar(255),
            main_callback_data STRING,
            text STRING UNIQUE,
            own_callback_data STRING UNIQUE
            );
            """
        self.execute(sql=sql, commit=True)

    def add_inner_categories(self, img: str = None, main_callback_data: str =  None, text: str = None, own_callback_data: str = None):
        sql = """
        INSERT INTO Inner_categories(img, main_callback_data, text, own_callback_data)
        VALUES(?, ?, ?, ?)
        """
        self.execute(sql=sql, parameters=(img, main_callback_data, text, own_callback_data), commit=True)


    def select_inner_categories(self, main_callback_data):
        sql = """
        SELECT * FROM Inner_categories WHERE main_callback_data=?
        """
        return self.execute(sql=sql, parameters=(main_callback_data, ), fetchall=True)

    def select_all_inner_categories(self):
        sql = """
        SELECT * FROM Inner_categories
        """
        return self.execute(sql=sql, fetchall=True)

    def create_table_step(self):
        sql = """
        CREATE TABLE Step(
            id INTEGER NOT NULL UNIQUE,
            cnt INTEGER
        );
        """
        self.execute(sql=sql, commit=True)

    def add_step(self, id: int, cnt: int = 0):
        sql = """
        INSERT INTO Step(id, cnt)
        VALUES(?, ?)
        """
        self.execute(sql=sql, parameters=(id, cnt), commit=True)

    def select_step(self, id):
        sql = """
        SELECT * FROM Step WHERE id=?
        """
        return self.execute(sql=sql, parameters=(id, ), fetchone=True)

    def update_step(self, id, step):
        sql = """
        UPDATE Step SET cnt=? WHERE id=?
        """
        return self.execute(sql=sql, parameters=(step, id), commit=True)

    def create_table_cart(self):
        sql = """
        CREATE TABLE Cart(
            id INTEGER NOT NULL,
            caption STRING,
            price STRING,
            amount INTEGER
        );
        """
        self.execute(sql=sql, commit=True)

    def add_cart(self, id: int, caption: str = None, price: str = None, amount: int = None):
        sql = """
        INSERT INTO Cart(id, caption, price, amount)
        VALUES(?, ?, ?, ?)
        """
        self.execute(sql=sql, parameters=(id, caption, price, amount), commit=True)

    def update_cart(self, id, amount):
        sql = """
        UPDATE Cart SET amount=? WHERE id=?
        """
        return self.execute(sql=sql, parameters=(amount, id), commit=True)

    def select_cart(self, id):
        sql = """
        SELECT * FROM Cart WHERE id=?
        """
        return self.execute(sql=sql, parameters=(id, ), fetchall=True)

    def select_one_cart(self, id, caption, price):
        sql = """
        SELECT * FROM Cart WHERE id=? AND caption=? AND price=?
        """
        return self.execute(sql=sql, parameters=(id, caption, price), fetchall=True)

    def delete_cart(self, id, caption, price):
        sql = """
        DELETE FROM Cart WHERE id=? AND caption=? AND price=?
        """
        self.execute(sql=sql, parameters=(id, caption, price), commit=True)

    def create_table_about_product(self):
        sql = """CREATE TABLE About_product(
            img varchar(255),
            main_callback_data STRING,
            text STRING UNIQUE,
            own_callback_data STRING UNIQUE,
            size varchar(255), 
            colour varchar(255)
            );
            """
        self.execute(sql=sql, commit=True)

    def add_about_product(self, img: str = None, main_callback_data: str = None, text: str = None, own_callback_data: str = None, size: list = None, colour: list = None):
        sql = """
        INSERT INTO About_product(img, main_callback_data, text, own_callback_data, size, colour)
        VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql=sql, parameters=(img, main_callback_data, text, own_callback_data, size, colour), commit=True)

    def select_about_product(self, main_callback_data, own_callback_data):
        sql = """
        SELECT * FROM About_product WHERE main_callback_data=? AND own_callback_data=?
        """
        self.execute(sql=sql, parameters=(main_callback_data, own_callback_data), fetchall=True)

    def select_all_about_product(self):
        sql = """
        SELECT * FROM About_product WHERE True
        """
        return self.execute(sql=sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
