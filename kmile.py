print("KM to Mile Converter")

unit = input("km or Mile: ")

amount = float(input("Amount: "))

if unit == "km":
    print(amount / 1.609)
elif unit == "mile":
    print(amount * 1.609)

else:
    print("error")
