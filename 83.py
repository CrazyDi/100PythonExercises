import ctypes

user32 = ctypes.windll.user32

screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(f"Width {screensize[0]}, Height: {screensize[1]}")
