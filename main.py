from PIL import Image
import numpy as np
import imageio

file = open("entire.bin", "wb")

ne = np.loadtxt('CSVs/SX57NE.csv', delimiter=',')
print("NE Loaded!")
nw = np.loadtxt('CSVs/SX67NW.csv', delimiter=',')
print("NW Loaded!")
se = np.loadtxt('CSVs/SX57SE.csv', delimiter=',')
print("SE Loaded!")
sw = np.loadtxt('CSVs/SX67SW.csv', delimiter=',')
print("SW Loaded!")

print("All loaded!")

true_east = np.concatenate((nw, sw))
print("East built!")
true_west = np.concatenate((ne, se))
print("West built!")

whole_map = np.concatenate((true_east, true_west), axis=1)
print("Whole built!")

np.save(file, whole_map, allow_pickle=False)
print("File Saved!")
file.close()

file = open("entire.bin", "rb")

a = np.load(file)
print("Reloaded!")
imageio.imwrite("pictures/entire_frombin.png", a)

file.close()