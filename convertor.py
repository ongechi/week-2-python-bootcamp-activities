user= input('please enter your name\n')
print('Hello',user,'Welcome to Your personal Converter')
print('\nkindly choose your conversion\n')

print(' a-converting cm into inches')
print(' b-multiplying values')
print(' c-convert liters to m^3')
print(' d-convert percentage to letter grade')
print(' e-convert degrees celsius to fahreneit')

select= input('')
if select =='a':
    print("you have selected cm convertor")
    #converting cm to inches
    a = float(input("Enter the distance in cm : "))
    inc=a/2.54
    print("the distance in inches is : " ,inc)

elif select =="b":
    print("You have selected the ml converter")
    ml=int(input("enter capacity in ml : "))
    b=ml/1000
    print(ml,"ml is equvalent to",b,"litres")
elif select =="c":
    #converting liters to m^3
    print("You have selected the litres converter")
    c=int(input("enter capacity in litres : "))
    metres=c/1000
    print("the capacity in m^3 is : " ,metres)
elif select=="d":
    #converting percentage to letter Grade
    print("You have selected the grade coverter")
    d=int(input("enter you grade in percentage\n"))
    if  80<= d <=100:
        print("A")
    elif 70<= d <=79:
        print ("B")
    elif 60<= d <=69:
        print("C")
    elif 50<= d <=59:
        print("D")
    elif 20<= d <=49:
        print("E")
    elif 0<= d <=19:
        print("F")
    else:
        print("enter valid Grade") 
elif select =="e":
    #converting degrees to fahrenheit
    print("You have selected the temperature converter")
    e=float(input("enter temperature in Celsius : "))
    fahrenheit=(e*1.8)+ 32
    print(e,"celsius is equal to",fahrenheit,"degrees fahrenheit")           
else:
        print("select again")

print("Goodbye",user)      


