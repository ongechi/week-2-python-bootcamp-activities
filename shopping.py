#request user for number of books
books=int(input("enter number books : \n"))
print("you have entered",books,"books")
#requesting user for the height of a single book
heightb=float(input("enter height of a book in inches : \n"))
print("you have entered",heightb,"inches per book")

#height of boxes
Bigbox=float(input("enter height of big box in inches eg 7.5 : \n"))
print("you have entered",Bigbox,"inches as height for the big box")

smallbox=float(input("enter height of small box in inches eg 7.5 : \n"))
print("you have entered",smallbox,"inches as height for the small box")

totalh=books*heightb
print ("the total height is ",totalh,"inches")


#if we are using the big boxes
if totalh >= Bigbox:
    
    if totalh%Bigbox == 0:
        x=totalh/Bigbox
        rndx=round(x)
        print(rndx,"Big boxes")
#where a big and a small box are needed

    elif totalh%Bigbox !=0:
        #calculate big boxes needed
        x=totalh/Bigbox
        rndx=round(x)
        print(rndx,"Big boxes")
        #to calculate small boxes 
        m=totalh%Bigbox
    
        rem=m/smallbox
        rndrem=round(rem)
        print(rndrem,"small boxes")
        
#if using the small boxes
elif totalh < Bigbox:
    a=totalh/smallbox
    rnda=round(a)
    print(rnda,"small boxes")
else:
    print("seek help")