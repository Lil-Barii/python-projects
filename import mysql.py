import mysql.connector


db = {
    "user":"root",
    "password":"1261Ba220862",
    "host":"localhost"
}

database = mysql.connector.connect(**db)
mycursor=database.cursor()
mycursor.execute("create database lib")
mycursor.commit()
mycursor.execute("create table library(book_ID  INT NOT NULL AUTO_INCREMENT PRIMARY KEY, book_name  VARCHAR(45) NOT NULL , author  VARCHAR(45) , publisher  VARCHAR(45) ,  price  INT)")
mycursor.commit()
mycursor.execute("insert into library(book_name , publisher , price) values('oliver twist' , 'charles dickens', 'jsda' , '15') ")
mycursor.commit()
mycursor.execute("select * from library")
lib = mycursor.fetchall()
print(lib)