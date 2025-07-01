# user_input = int(input("how big do you want the shape?"))
# for i in range (user_input):
#     for j in range (user_input):
#         print("*", end= " ")
#     print( )

# user_input = int(input("how big do you want the shape?"))
# for i in range (user_input):
#     for j in range (i+1):
#         print("*", end= " ")
#     print( )

user_input = int(input("how big do you want the shape?"))
for i in range (user_input):
    for j in range (user_input-i-1):
        print(" ", end= " " )
    for j in range (i+1):
        print(" * ",end= " ")
    print( )
