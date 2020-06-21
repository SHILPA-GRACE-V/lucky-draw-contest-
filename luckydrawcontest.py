import random
while True:
    number=int(input("enter a number:"))
    num=0
    n=0
    while(number!=0):
        num+=number%10
        number=number//10
    if(num>=10):
        while(num!=0):
            n+=num%10
            num=num//10
    number=n
    #print(number)
    randomList=[]
    for i in range(0,5):
        randomList.append(random.randint(0,9))
    #print(randomList)
    gift_items=['spiderman','barbie doll','suzuki acces scooty','royal enfield bullet','dhothi','t-shirt','saree','churidhar','cosmetics','dinner set','parker pin','tata tiger car','amazon gift card']
    if(number in randomList):
        Giftitem=random.choice(gift_items)
        if(Giftitem=='suzuki acces scooty'):
            gift_items.remove('suzuki acces scooty')
            print("Hurry you got special price")
        elif(Giftitem=='royal enfield bullet'):
            gift_items.remove('royal enfield bullet')
            print("Hurry you got special price")
        elif(Giftitem=='tata tiger car'):
             gift_items.remove('tata tiger car')
             print("Hurry you got special price")
        print("Congartulations")
        print("Gift for you is:",Giftitem)
    else:
        print("Better luck next time")
    

    
    

