cols = 5
rows = 5

for x in range(cols * rows):
    print(f"({x % cols}, {x // cols})")
