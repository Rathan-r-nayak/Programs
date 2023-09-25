for i in range(1,21):
    with open(f"tables/mulof{i}","w") as a:
        for j in range(1,11):
            a.write(f"{i}X{j}={i*j}\n")