while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break

    sides = sorted([a, b, c])
    
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")
