from math import pi, pow


def liquid_volume_in_sphere(h, r=10):
    return (4 * pi * pow(r, 3)) / 3 - (pi * pow(h, 2) * (3 * r - h)) / 3


if __name__ == "__main__":
    print(liquid_volume_in_sphere(2))
