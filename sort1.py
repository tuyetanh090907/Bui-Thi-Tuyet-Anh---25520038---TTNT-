import numpy as np
import os

N = 1_000_000

os.makedirs("data", exist_ok=True)

#Tăng dần
day_tang_dan = np.sort(np.random.rand(N))
np.save("data/daytangdan.npy", day_tang_dan)

#Giảm dần
day_giam_dan = day_tang_dan[::-1]
np.save("data/daygiamdan.npy", day_giam_dan)

#4 dãy số thực ngẫu nhiên
for i in range(1, 5):
    day_thuc = np.random.rand(N)
    np.save(f"data/daythuc{i}.npy", day_thuc)
    
#4 dãy số nguyên ngẫu nhiên
for i in range(1, 5):
    day_nguyen = np.random.randint(0, 10_000_000, size=N)
    np.save(f"data/daynguyen{i}.npy", day_nguyen)    