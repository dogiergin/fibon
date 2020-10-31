import timeit
print('#'*67)
print("""        Fibonacci  programına hoşgeldiniz!
|    Aşağıda yapmak istediğiniz işlemin  numarasını giriniz.      |  
|    Yazdığınız sayıya kadar olan fibonacci sonuçları  = 1        |
|    Belirli bir adımdaki fibonacci sayısı = 2                    |
|    Yazdığınız sayıya kadar geçen işlemci süresi = 3             |
|    Belirli adımdaki fibonacci sayısında geçen işlemci süresi = 4| 
|    İteratif kod için "1" ,  Özyinelemeli kod için "2"           |
|    yanına ekleyiniz .        ( "11" ya da "22" gibi)            |
|    Fibonacci tarihçesi için yukarıdaki sayılar dışında  bir şey |""")
print('#'*67)
istemci = int(input('İşlem numarasını giriniz : '))
def fr(m):
    if ( m == 0 ):
        return 0
    elif( m == 1 ):
        return 1
    else:
        return fr(m-1) + fr(m-2)

def fi(n):
    a , b = 0, 1
    for i in range(0, n):
        a , b = b, a + b
    return a
if ( istemci == 11):
    k = int(input('Kaçıncı adıma kadar ? :'))
    a = []
    for i in range(0,k):
        a += [fi(i)]
    print(a)
elif( istemci == 12):
    k = int(input('Kaçıncı adıma kadar ? :'))
    a = []
    for i in range(0, k):
        a += [fr(i)]
    print(a)
elif (istemci == 21):
    p = int(input('Hangi adım ? :'))
    print(fi(p))
elif (istemci == 22):
    p = int(input('Hangi adım ? :'))
    print(fr(p))
elif (istemci == 31):
    k = int(input('Kaçıncı adıma kadar ? :'))
    a = []
    for i in range(0, k):
        a += [fi(i)]
    print(a)
    print('Geçen süre : {}'.format(timeit.timeit()))
elif (istemci == 32):
    k = int(input('Kaçıncı adıma kadar ? :'))
    a = []
    for i in range(0, k):
        a += [fr(i)]
    print(a)
    print('Geçen süre : {}'.format(timeit.timeit()))
elif (istemci == 41):
    p = int(input('Hangi adım ? :'))
    fi(p)
    print('İşlem süresi : {} '.format(timeit.timeit()))
elif (istemci == 42):
    p = int(input('Hangi adım ? :'))
    fr(p)
    print('İşlem süresi : {} '.format(timeit.timeit()))
else:
    print("""Fibonacci (diğer bilinen adlarıyla Leonardo Bonacci, Pisalı Leonardo, Leonardo Bigollo Pisano d. 1170, ö. 1250), orta çağın en yetenekli Batılı matematikçisi olarak kabul edilen İtalyan matematikçi. 
     Leonardo 1170 yılında İtalya'nın Pisa şehrinde doğdu.Fibonacci Hint-Arap sayıları ile aritmetik işlemler yapmanın Roma rakamları ile hesap yapmaktan çok daha basit ve verimli olduğunu gördü. Leonardo bütün Akdeniz bölgesini gezdi ve dönemin önde gelen Arap matematikçiler ile çalışma olanağı buldu. Leonardo yaklaşık olarak 1200 yıllarında bu seyahatinden döndü. 1202 yılına gelindiğinde 32 yaşında, öğrendiklerini "abaküs kitabı" veya "hesaplama kitabı" anlamına gelen Liber Abaci isimli eserinde topladı. 
     Yayınladığı bu eserinde Hint-Arap Sayı Sistemi'ni Avrupa'ya duyurdu. 
     Kaynak:https://tr.wikipedia.org/wiki/Leonardo_Fibonacci """)



