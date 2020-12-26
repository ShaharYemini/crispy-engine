import pickle

with open("names.txt", "rb") as f:
    names = pickle.load(f)
    f.close()

for name in names:
    print(name)