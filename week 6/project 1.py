print("Delivery Addresses\n1. Ibeju-Lekki\n2.Epe")
location = input("Delivery ddress: ")

if location == "Ibeju-Lekki": 
  weight = int (input("What does your package weigh?: "))
  if weight >= 10: 
    print("Your package is N5500")