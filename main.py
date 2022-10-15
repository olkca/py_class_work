try:
    a = int(input("Ведіть висоту: "))
    b = int(input("Ведіть ширину: "))
    for i in range(a):
        for j in range(b):
            if i == 0 or i == a - 1:
                print("* ", end="")
            else:
                d = b - a - 1
                if j == 0 or j == a + d:
                    print("* ", end="")
                else:
                    print("  ", end="")
        print()
except Exception as e:
    print(f"Error {e}")