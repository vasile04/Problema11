n=(int(input('Introdu nr de elemente ale tabloului:')))
lista1=[]
print('introduceti', n, 'elemente al tabloului')
if n>=10:
    print('eroare')
else:
    for i in range(0, n):
        a=int(input('introdu a:'))
        lista1.extend([a])
    print('lista initiala: ', lista1)
    a1=lista1[0:6]
    print('a) afisarea tabloului la un interval de 5 pozitii ', a1)
    b=list(reversed(lista1))
    print("b) afisarea elementelor in ordine inversa a introducerii de la calculator: ", b)
    c=sorted(lista1, reverse=True)
    print('c) Sortarea elementelor tabloului in ordine descrescatoare:', c)
    d=[]
    for i in range(0, len(lista1)):
        if lista1[i]%2==0:
            k=lista1[i]
            d.extend([k])
    print('d) si m) afisarea elementelor pare din lista initiala', d)
    print('e) afisarea mediei aritmetice a elementelor pare: ', sum(d)/len(d))
    f=[]
    for q in range(0, len(lista1)):
        if lista1[q]%2!=0:
            v=lista1[q]
            f.extend([v])
    print('f) afisarea componentelor impare: ', f)
    x=int(input('Introdu valoarea lui x: '))
    y=int(input('introdu valoarea lui y: '))
    g=[]
    for i in range(0, len(lista1)):
        if (lista1[i]>x) and (lista1[i]%y!=0):
            s=lista1[i]
            g.extend([s])
    print('g) afisarea elementelor mai mari ca x si nu sunt divizibile cu y: ', g)
    h=[]
    for i in range(0, len(lista1)):
        if lista1[i]>x and lista1[i]<y:
            l=lista1[i]
            h.extend([l])
    print("h) lista cu elemente mai mari ca x si mai mici ca y: ", h)
    m=[]
    for i in lista1:
        if i<0 and i%2!=0:
            m.extend([lista1.index(i)])
    
    print('i) afisarea pozitiilor elementelor impare negative: ', m)
    p=[]
# 2 cifre semnificative => numarul e mai mare ca 0
    for klk in lista1:
        if (klk>9 and klk <100):
            p.extend([lista1.index(klk)])
    print('j) afisarea pozitiilor numerelor formate din 2 cifre semnificative: ', p)
    k1=lista1.copy()
    k1[0]=min(k1)
    print('k) inlocuirea primului element al listei1 cu elementul minim al acestei liste: ', k1)
    r=lista1.copy()
    r[r.index(min(r))]=r[0]
    print('l) inlocuirea elementului minim al listei cu primul element: ', r)
    mgk1=[]
    for rt4 in range(0, len(lista1)):
        if lista1[rt4]%3==0:
            pb1=lista1[rt4]
            mgk1.extend([pb1])
    print('n) tabloul format din componentele divizibile cu 3: ', mgk1)