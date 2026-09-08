'''
User nach dem Alter und Geld fragen,
Wenn der Benutzer erwachsen ist (weil FSK 18),
und mind. 20 Euro Guthaben hat,
Artikel (Kinoticket) gekauft.
'''

def purchase_ticket():
    age = int(input("How old are you? Enter a number: "))
    balance = int(input("How much is your account balance? Enter a number: "))
  
    if age >= 18 and balance >= 20:
        print("You can purchase a ticket.")
    else:
        print("Sorry, you are too young or don't have sufficient credit")

purchase_ticket()
