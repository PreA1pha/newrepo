import sqlite3 as sqll
class Process():
    def __init__(self,name="NUll",page="NUll",author="NUll",rate="NUll"):
        self.name=name
        self.author=author
        self.rate=rate
        self.page=page
        self.sql=sqll.connect("backend/Library.sqlite")
        self.sql.cursor()
        self.a=self.sql.cursor()
        self.rd=self.a.fetchall()
        self.sql.execute("CREATE TABLE IF NOT EXISTS Lib (Id INTEGER PRIMARY KEY AUTOINCREMENT,name,author,page,rate)")
    def add(self):
        self.sql.execute("INSERT INTO Lib (name,author,page,rate) VALUES('{}','{}','{}','{}')".format( self.name,self.page, self.author,self.rate))#soecfy wwhat shoul u nuse  in it if u dont it takes all of them
        return self.sql.commit()

    def erase(self):
        self.silsecim=input("lütfen sileceğiniz objenin id'sini giriniz:")
        self.sql.execute("DELETE FROM Lib WHERE Id='{}'".format(self.silsecim))
        return self.sql.commit()
    def read(self):
        self.a.execute("SELECT * FROM Lib")
        rd = self.a.fetchall()
        for tup in rd:
            for word in tup:
                print(word)
    def updt(self):
        self.ratenew=input("değiştirmek istediğin puan")
        self.namenew=input("hangi ad ile")
        self.authornew=input("hangi Yazar")
        self.pagenew=input("hangi sayfalar")
        self.old=input("hangi id")#parametrelerdede tanımlayabilirdik ama bu yaptığımız işlem farklı objenin özelliğini kullanıcıdan istediğimiz veri ile tanımlıyoruz yoksa böyle bir imkanımız olmaz her zaman init devam
        self.sql.execute("UPDATE Lib SET name= '{}' author='{}' WHERE Id ='{}'".format(self.namenew,self.authornew,self.old))
        return self.sql.commit()
    def cl(self):
        self.sql.close()

#remember when u are using method thnk of litke a imported shit
#__init__ let us create a attribute for our object and attributes can also  have sub attirbutes
#super().__init__(self) lets us define our imports our upper clases atrributes from this