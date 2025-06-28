import numpy as np

# Max Element & Location (1D & 2D)
print("Max Element & Location (1D & 2D)")
data = np.random.randint(35,45, (5,10))
max_val = np.max(data)
flat_idx = np.argmax(data)
idx= np.unravel_index(flat_idx, np.shape(data))
idx_pos = tuple(int(i) for i in idx)
print(f"Data: \n{data} \nMax = {max_val}\nPosition = {idx_pos}")


# Find All Positions of a Target Value
print("\n\nFind All Positions of a Target Value")
target_val = input("Enter Target Value: ")
positions_target = np.argwhere(data == int(target_val))
print(f"Data: \n{data}\nIndex: \n{positions_target}")


# Boolean Mask to Coordinates
print("\n\nBoolean Mask to Coordinates")
data = np.random.choice([True, False], size=(3, 3))
mask = data == True
print(f"Data: \n{data}\nIndex of True: \n{np.argwhere(mask)}")