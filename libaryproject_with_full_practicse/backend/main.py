from cpu import Process
book2 = Process()
print("kütüphaneye hoş geldiniz işlemleriniz (A)dd,(E)rase,(R)ead,(U)pdate,(E)xit")
while True:
    print(50*"-")
    secim = input("lütfen ne yapmak istediğinizi giriniz:")
    if secim == 'add':
        name = input("isim girin:")
        page = input("safya sayısı girin:")
        author = input("yazar girin:")
        rate = input("yorum girin:")
        book1 = Process(name, page, author, rate)
        book1.add()
        book1.cl

    if secim == 'erase':
        book2.erase()
    if secim == 'read':
        book2.read()
    if secim == 'update':
        book2.updt()
    if secim == 'exit':
        exit()