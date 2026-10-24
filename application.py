m=list(map(float,input("inter the score 0-->100 : ").split()))
for i in m :
    if i > 100 :
     print("MAximume is 100")
    else:
        while len(m)>0 :
            n=int(input("choos one of these things : 1-add score , 2-show all of scores , 3-View class statistics (Total, Avg, Max, Min) , 4-remove a score , 5-Sort scores list , 6-exit  (choose numbers only) "))
            if n == 1:
             mn=list(map(float,input("inter the score 0-->100 : ").split()))
             for i in mn :
               if i > 100 :
                print("MAximume is 100")
                m.extend(mn)
                print("score you have : ", m)
            elif n == 2:
                print("all score you have",m)
            elif n==3:
             l=str(input("choose one of these things (total score ,avg,max,min)"))
             if l == "total" :
                    print(len(m))
             elif l == "avg" :
                print((sum(m)/ len(m)))
             elif l == "max":
                 print("max score you have", max(m))
             elif l == "min":
                print("min score you have : ", min(m))
            elif n == 4 :
             i=float(input("choos number you want remove"))
             if i in m:
                m.remove(i)
                print("list without number you remove ", m)
             else:
                print("number not found in list")
            elif n == 5:
                m.sort()
                print("your lis is sored", m)
            elif n == 6:
             print("Thank you to use this application :) ")
            break