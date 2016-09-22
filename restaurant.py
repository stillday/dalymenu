# -*- coding: utf-8 -*-

print "Willkommen bei der Eingabe des Tagesmenüs."

menu = {}

while True:
    dish = raw_input("Bitte gib die Hauptspeise ein: ")
    price = raw_input("Gib bitte den Preis in Euro ein: ")
    menu[dish] = price

    print "Das  Tagesgericht " + dish + " Kostet " + price + "€"

    if raw_input("Möchtest du eine weitere Speise erfassen? Ja/Nein: ").lower() == "nein":
       break

print "Das Tagesmenü lautet heute %s" % menu

with open("menu.txt", "w+") as restaurant_file:
    print "Unsere heutigen Tagesmenüs:"
    restaurant_file.write("Unsere heutigen Tagesmenüs:\n")
    for key in menu:
        print "- " + key + " - " + menu[key] + "€"
        restaurant_file.write("- " + key + " - " + menu[key] + "€" + "\n")
    restaurant_file.write("\n")
