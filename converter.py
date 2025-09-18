def php_yen(php):
    return print(php * 2.58)

def yen_php(php):
    return print(php / 2.58)

print("1. PHP to Yen")
print("2. Yen to PHP")

while True:
    choice = int(input("Select what currency: "))

    if choice == 1:
        convert = int(input("Enter PHP: "))
        php_yen(convert)

    else: 
        convert1 = float(input("Enter Yen: "))
        yen_php(convert1)
    
    pick = input("Want to convert again? (Y/N): ").upper()
    if (pick == "Y"):
        print()
        continue
    else:
        break
