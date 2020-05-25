def Multi(*faktoren):
    h = 1
    for g in faktoren:
        h = h * g
    print(h)


print("Gib Werte ein:")
d = int(input())
e = int(input())
f = int(input())
Multi(d,e,f)
