import mysql.connector

# config = mysql.connector.connect(**database)
# mycursor = config.cursor()
# mycursor.execute("update participants set BOD = '1995' where region = 'virginia'")
# config.commit()
# mycursor.execute("select * from participants")
# result = mycursor.fetchall()
# print(result)

# class Model:
#     def __init__(self):
#         self.database = {"user": "root", "password": "midnight", "host": "localhost", "database": "library"}
#         self.config = mysql.connector.connect(**self.database)
#         self.cursor = self.config.cursor()
#
#     def create_table(self):
#         self.cursor.execute("create table books(id INT primary key, title varchar(100), author varchar(100), publisher varchar(120), price INT)")
#         self.config.commit()
#
#     def get_rows(self):
#         self.cursor.execute("select * from books")
#         data = self.cursor.fetchall()
#         print(data)
#
#     def insert(self):
#         self.cursor.execute("insert into books(id, title, author, publisher, price) values(2, 'jang va solh', 'leo', 'cheshmeh', 120)")
#         self.config.commit()
#
#     def update(self):
#         self.cursor.execute("update books set title = 'little prince', author = 'exupery' where id = 1")
#         self.config.commit()
#
#     def delete(self):
#         self.cursor.execute("delete from books where id = 2")
#         self.config.commit()

# m = Model()
# m.create_table()
# m.insert()
# m.update()
# m.delete()
# m.get_rows()