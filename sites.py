import random
import webbrowser
import time
for i in range(10):
    sites=random.choice(['https://youtube.com','https://instagram.com'])
    webbrowser.open(sites)
    time.sleep(2.5)
