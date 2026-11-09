#Zadanie 1
# a = input("a = ")
# b = input("b = ")

# suma = int(a) + int(b)
# print(suma, type(suma).__name__)
# roznica = int(a) - int(b)
# print(roznica, type(roznica).__name__)
# iloczyn = int(a)*int(b)
# print(iloczyn, type(iloczyn).__name__)

# if int(b) > 0:

#     iloraz = int(a)/int(b)
#     print(iloraz, type(iloraz).__name__)

#Zadanie 1b
# a = input("a = ")
# b = input("b = ")

# suma = int(a) + float(b)
# print(suma, type(suma).__name__)
# roznica = int(a) - float(b)
# print(roznica, type(roznica).__name__)
# iloczyn = int(a)*float(b)
# print(iloczyn, type(iloczyn).__name__)

# if int(b) > 0:

#     iloraz = int(a)/float(b)
#     print(iloraz, type(iloraz).__name__)



#Zadanie 2
# a = input()
# b = input()

# print(a+b)
# print(a*3)
# print(int(b)*3)
# print(int(a)+int(b))



#Zadanie 3
# a = input()
# b = input()
# print(a == b)
# print(int(a) == float(b))
# print(int(a)>float(b))


#Zadanie 4
# liczba = int(input())
# print("Start")
# if liczba > 0:
#     print("Liczba dodatnia")
#     print("Koniec")


# liczba = int(input())
# print("Start")
# if liczba > 0:
#     print("Liczba dodatnia")
# print("Koniec")


#Zadanie 5
# a = int(input())

# if a > 0:
#     print("Dodatnia")

# if a%2 == 0:
#     print("Parzysta")

#Zadanie 6

a = float(input())
operator = input()
b = float(input())

if operator == "+":
    print(a+b)
if operator == "-":
    print(a-b)
if operator == "*":
    print(a*b)
if operator == "/":
    if b == 0:
        print("Nie można dzielić przez zero")
    print(a/b)
