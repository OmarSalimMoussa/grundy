def run():
    hits = []
    for i in range(10):
        for j in range(10):
            if i > j:
                hits.append(str(i * j))
    print(",".join(hits))
    return
