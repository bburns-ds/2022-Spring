def sols(base):
    print(base)
    for i in range (base):
        print(f"${i}^2 + 2({i}) + 2 &= {(i**2 + 2*i + 2) % base}$\\\\")
    print("")

sols(5)
sols(7)
sols(8)