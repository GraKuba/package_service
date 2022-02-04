package_count = 0
package_weight = 0

while package_count >= 0:
    print("Podaj wagę paczki")
    element = int(input())
    if element > 10 or element < 1:
        break
    else:
        if package_weight >= 20:
            package_count += 1
            package_weight = 0
            package_weight += element
            print("Paczka została wysłana")
        else:
            package_weight += element

    print("Package count=", package_count)
    print("Current package weight", package_weight)





