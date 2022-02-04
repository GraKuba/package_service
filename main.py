package_count = 0
package_weight = 0
kilograms_sent = 0
highest_waste = 0

while package_count >= 0:
    print("Podaj wagę paczki")
    element = int(input())
    if element > 10 or element < 1:
        break
    else:
        if package_weight + element > 20:
            package_count += 1
            kilograms_sent += package_weight
            highest_waste = 20 - kilograms_sent
            package_weight = 0
            package_weight += element
            print("Paczka została wysłana")
        else:
            package_weight += element

    print("Package count:", package_count)
    print("Current package weight:", package_weight)
    print("Kilograms sent:", kilograms_sent)

print("Packages sent: {}, Kilograms sent: {}, Wasted kilograms: {}, Package with the highest waste: {}".format(
    package_count, kilograms_sent, (package_count * 20) - kilograms_sent, highest_waste))






