def is_right_angled_triangle(a, b, c):
    # Check if a^2 + b^2 = c^2 or b^2 + c^2 = a^2 or a^2 + c^2 = b^2
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return True
    else:
        return False


a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if is_right_angled_triangle(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
