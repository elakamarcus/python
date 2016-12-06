q = {}
q = set(q)
for a in range(50, 1000, 50):
    for i in range(2, 1+a, 1):
        for j in range(2, 1+a, 1):
            q.add(i**j)
print"(2 -> {})^(2 -> {}): {}".format(i, j, len(q))
#above indent and spacing follows pylint requests
