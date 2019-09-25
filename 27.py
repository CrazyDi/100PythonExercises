def acceleration(v1, v2, t1, t2):
    return (v2 - v1) / (t2 - t1)


if __name__ == "__main__":
    print(acceleration(0, 10, 0, 20))
