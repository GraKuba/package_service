package_count = 0
package_weight = 0
kilograms_sent = 0
highest_waste = 0
waste = 0

while True:
    print("Input package weight")
    element = int(input())
    if element > 10 or element < 1:
        break
    else:
        if package_weight + element > 20:
            package_count += 1
            kilograms_sent += package_weight
            waste = 20 - package_weight
            if highest_waste < waste:
                highest_waste = 0
                highest_waste += waste
            package_weight = 0
            package_weight += element
            print("Package has been sent")
        elif (package_weight + element) == 20:
            package_count += 1
            kilograms_sent += 20
            package_weight = 0
            print("Package has been sent")
        else:
            package_weight += element


print("Packages sent: {}, Kilograms sent: {}, Wasted kilograms: {}, Package with the highest waste: {}".format(
    package_count, kilograms_sent, (package_count * 20) - kilograms_sent, highest_waste))
