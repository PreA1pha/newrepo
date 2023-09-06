import sqlite3 as sqll
class Process():
    def __init__(self,name,page,author,rate):
        self.name=name
        self.author=author
        self.rate=rate
        self.page=page
        self.sql=sqll.connect("backend/Library.sqlite")
        self.sql.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS Lib (Id INTEGER PRIMARY KEY AUTOINCREMENT , name , author,page,rate)")
    def add(self):
        self.sql.execute("INSERT INTO Lib VALUES('{}','{}','{}','{}')".format(self.name, self.author,self.page,self.rate))
        return self.sql.commit()
    def erase(self):
        self.silozellik=input("lütfen ne sileceğiniz özellikleri seçiniz")
        self.silsecim=input("lütfen hangi objeyi sileceğinizi seçiniz")
        self.sql.execute("DELETE FROM Lib WHERE {}={}".format(self.silozellik,self.silsecim))
        self.sql.commit()
        self.sql.close()
        return print("başarılı")
    def cl(self):
        self.sql.close()

book1=Process("white","1459","walter","10/10")
print(book1)
print(book1.add())
print(book1.cl())