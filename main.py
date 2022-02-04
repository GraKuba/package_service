package_count = 0
package_weight = 0
kilograms_sent = 0

while package_count >= 0:
    print("Podaj wagę paczki")
    element = int(input())
    if element > 10 or element < 1:
        break
    else:
        if package_weight + element > 20:
            package_count += 1
            kilograms_sent += package_weight
            package_weight = 0
            package_weight += element
            print("Paczka została wysłana")
        else:
            package_weight += element

    print("Package count:", package_count)
    print("Current package weight:", package_weight)
    print("Kilograms sent:", kilograms_sent)

print("1. Packages sent:", package_count)
print("2. Kilograms sent:", kilograms_sent)
print("3. Wasted kilograms:", (package_count * 20) - kilograms_sent)





