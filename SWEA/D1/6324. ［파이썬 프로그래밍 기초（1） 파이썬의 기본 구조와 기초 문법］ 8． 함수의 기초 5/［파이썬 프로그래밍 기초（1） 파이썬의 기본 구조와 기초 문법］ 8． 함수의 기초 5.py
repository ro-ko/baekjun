arr = [1, 2, 3, 4, 3, 2, 1]
uni = sorted(set(arr))
print(f"[{', '.join(map(str, arr))}]")
print(f"[{', '.join(map(str, uni))}]")

