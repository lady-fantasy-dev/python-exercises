'''
WENN Wasser im Tank ist DANN
    WENN Bohnen im Behälter sind DANN
        Stelle eine Tasse unter den Ausguss
        Drücke Start
    SONST
        Fülle Bohnen in den Behälter
    ENDE WENN
SONST
    Fülle Wasser in den Tank
ENDE WENN   
'''

water = False
beans = False

if not water:
    user_input = input("Do you want to fill the water tank? y/n: ")

    if user_input == "y":
        water = True
    
if not beans:
    user_input = input("Do you want to fill the coffee container? y/n: ")

    if user_input == "y":
        beans = True

if water and beans:
    print("Put a cup under the spout")
    print("Press start")
else:
    print("Can't brew coffee")


# water = False
# beans = False
# 
# if water == False:
#     print("Fülle Wasser in den Tank")
#     user_input = input("Refill water? y/n: ")
#     if user_input == "y":
#         if user_input == "y":
#             print("Water refilled!")
#         else:
#             print("Aborting")
# else:
#     match beans:
#         case True:
#             print("Stelle eine Tasse unter den Ausguss & Drücke Start")
#         case False:
#             print("Fülle Bohnen in den Behälter")
#             user_input = input("Refill water? y/n: ")
#             if user_input == "y":
#                 print("Refilling beans!")
#                 print("Stelle eine Tasse unter den Ausguss & Drücke Start")
#             else:
#                 print("Aborting")
        

# water = False
# beans = False
# 
# if water == True:
#     match beans:
#         case True:
#             print("Stelle eine Tasse unter den Ausguss & Drücke Start")
#         case False:
#             print("Fülle Bohnen in den Behälter")
#             user_input = input("Refill water? y/n: ")
#             if user_input == "y":
#                 print("Refilling beans!")
#             else:
#                 print("Aborting")
# else:
#     print("Fülle Wasser in den Tank")
#     user_input = input("Refill water? y/n: ")
#     if user_input == "y":
#         print("A cup of coffee coming right up!")
#     else:
#         print("Aborting")
#         
        
        
        
        

# 
# water = False
# beans = False
# 
# if water == True:
#     match beans:
#         case True:
#             print("Stelle eine Tasse unter den Ausguss & Drücke Start")
#         case False:
#             print("Fülle Bohnen in den Behälter")
#             user_input = input("Refill water? y/n: ")
#             if user_input == "y":
#                 print("Refilling beans!")
#             else:
#                 print("Aborting")
# else:
#     print("Fülle Wasser in den Tank")
#     user_input = input("Refill water? y/n: ")
#     if user_input == "y":
#         print("A cup of coffee coming right up!")
#     else:
#         print("Aborting")
# 

