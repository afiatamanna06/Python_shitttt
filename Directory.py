from pathlib import Path

path = Path("ecommerce")
print(path.exists())
for file in path.glob('*.*'):
    print(file)
path1 = Path("emails")
#path1.mkdir()
#print(path1.exists())
#path1.rmdir()
#print(path1.exists())
