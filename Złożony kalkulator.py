print("Witaj, w kalkulatorze nowej generacji SPOX!")

print("Zacznijmy liczenie")

wybor = input(''' Wybierz odpowiednią operację:
+ - dodawanie,
- - odejmowanie,
* -  mnożenie,
/ - dzielenie,
** - potęgowanie,
Wybrana operacja: ''')


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if(wybor == "+"):
    print("wynik to:", a + b)
    print("Gratulujemy")
elif(wybor == "-"):
    print("wynik to:", a - b)
    print("Gratulujemy")
elif(wybor == "*"):
    print("wynik to:", a * b)
    print("Gratulujemy")
elif(wybor == "/"):
    if(b == 0):
        print("Czy ja tu widzę zero? Nie dziel cholero przez zero!")
    else:
        print(a / b)
elif(wybor == "**"):
    print(a ** b)
    print("Gratulujemy")
else:
    print("Dokonałeś niewłaściwego wyboru znaku")
    

        
    
