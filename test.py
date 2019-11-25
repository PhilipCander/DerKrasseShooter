import ctypes

user32 = ctypes.windll.user32
screensizex, screensizey = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


print(screensizex, screensizey)