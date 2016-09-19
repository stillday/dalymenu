# -*- coding: utf-8 -*-

print "Willkommen bei der Eingabe des Tagesmenüs."

menu = {}

while True:
    dish = raw_input("Bitte gib die Hauptspeise ein: ")
    price = raw_input("Gib bitte den Preis in Euro ein: ")

    print "Das  Tagesgericht " + dish + " Kostet " + price + "€"

    new = raw_input("Möchtest du eine weitere Speise erfassen? Ja/Nein: ")

    menu[dish] = price

    if new == "nein":
       break

print "Das Tagesmenü lautet heute %s" % menu

with open("menu.txt", "w+") as restaurant_file:
    print "Unsere heutigen Tagesmenüs:"
    restaurant_file.write("Unsere heutigen Tagesmenüs:\n")
    for item in menu:
        print item + " - " + price + "€"
        restaurant_file.write("- " + item + " - " + price + "€" + "\n")
    restaurant_file.write("\n")


