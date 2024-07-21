# number = [10, 16, 30, 21]
# print(max(number)) #menampilkan nilai yang paling besar
# print(min(number)) #menampilkan nilai yang paling kecil
# print("hello".upper()) #Mengubah teks menjadi huruf Kapital
# print("WELCOME".lower()) #Mengubah teks menjadi huruf kecil

# def order_pizza(): #Membuat function diawali dengan def lalu nama function
#     quantity = 7
#     price = 10
#     total_order = quantity * price
#     print(f"Total order  $:  {total_order}" )

# order_pizza() #Menjalankan function.

# def order_pizza(quantity): #Parameter (variable menampung quantity)
#     price = 10
#     total_order = quantity * price
#     print(f"Total order  $:  {total_order}" )

# order_pizza(7) #Argument , berisi nilai dari quantity 

# def order_pizza(): #Parameter (variable menampung quantity)
#     price = input("harga:  ")
#     quantity = input("quanity:  ")
#     price_integer = int (price)
#     quantity_integer= int (quantity)
#     total_order = price_integer * quantity_integer
#     print("Total order: ", total_order )

# order_pizza()

# total = 50 #Global variable : variable di deklarasikan diluar function. 
# def sum():
#     first = 10
#     second = 20
#     total = first+second #Local variable: variable di deklarasikan didalam function. 
#     print(total)
# print(total)
# sum()