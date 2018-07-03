#question1
import sqlite3
a=sqlite3.connect('test.db')
a.execute(''' CREATE TABLE BOOKS
 (  BOOK_ID  INT  PRIMARY KEY  NOT NULL,
    TITLE_ID INT               NOT NULL,
    LOCATION CHAR(50)             NOT NULL,
    GENRE    CHAR(50)             NOT NULL)''')
a.execute('''CREATE TABLE Titles
 (   Titles_ID      CHAR      NOT NULL,
    Title         CHAR                  NOT NULL,
    ISBN          CHAR(50)              NOT NULL,
    Publisher_ID  INT        NOT NULL,
    Publication_Year     CHAR(50))''')
a.execute('''CREATE TABLE Publishers
   ( Publishers_ID      CHAR       NOT NULL,
    Name              CHAR(50)             NOT NULL,
    Street_Address    CHAR(50)             NOT NULL,
    Zip_Code_ID       INT      NOT NULL)''')
a.execute('''CREATE TABLE Zip_Codes
  (  Zip_Codes_ID      CHAR       NOT NULL,
    City             CHAR(50)             NOT NULL,
    State            CHAR(50)             NOT NULL,
    Zip_Code         CHAR(50)             NOT NULL)''')
a.execute('''CREATE TABLE Authors_Titles
  (  Author_Title_ID      INT       NOT NULL,
    Author_ID            INT       NOT NULL,
    Title_ID             INT              NOT NULL)''')
a.execute('''CREATE TABLE Authors
 (   Authors_ID      CHAR      NOT NULL,
    First_Name     CHAR(50)             NOT NULL,
    Middle_Name     CHAR(50),
    Last_Name        CHAR(50)             NOT NULL)''')
print("tables created")

a.execute("INSERT INTO Books(Book_ID,Title_ID,Location,Genre) VALUES(1,20,'Chandigarh','Kavya')")
a.execute("INSERT INTO Books(Book_ID,Title_ID,Location,Genre) VALUES(2,25,'Delhi','Kashish')")
a.execute("INSERT INTO Titles(Titles_ID,Title,ISBN,Publisher_ID,Publication_Year) VALUES('1','acadview python','432-5452-344',1453,'2018')")
a.execute("INSERT INTO Titles(Titles_ID,Title,ISBN,Publisher_ID,Publication_Year) VALUES('1','acadview machine learning','342-5343-346',1233,'2018')")
a.execute("INSERT INTO Publishers(Publishers_ID, Name,Street_Address,Zip_Code_ID) VALUES('432-5452-344','Kavya Kapoor','Chandigarh',403106)")
a.execute("INSERT INTO Publishers(Publishers_ID, Name,Street_Address,Zip_Code_ID) VALUES('342-5343-346','Kashish','Delhi',110012)")
a.execute("INSERT INTO Zip_Codes(Zip_Codes_ID,City,State,Zip_Code) VALUES('403106','Chandigarh','Delhi','123')")
a.execute("INSERT INTO Zip_Codes(Zip_Codes_ID,City,State,Zip_Code) VALUES('110012','Chandigarh','Delhi','123')")
a.execute("INSERT INTO Authors_Titles(Author_Title_ID ,Author_ID ,Title_ID) VALUES(1,2345,344-433-3435)")
a.execute("INSERT INTO Authors_Titles(Author_Title_ID ,Author_ID ,Title_ID) VALUES(2,3242,354-435-4535)")
a.execute("INSERT INTO Authors(Authors_ID,First_Name,Middle_Name,Last_Name) VALUES('1','Miss','Kavya','Kapoor')")
a.execute("INSERT INTO Authors(Authors_ID,First_Name,Middle_Name,Last_Name) VALUES('2','Miss','Kashish','Gupta')")
a.commit()