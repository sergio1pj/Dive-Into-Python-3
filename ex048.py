from pathlib import Path

path = Path()
#print(path.mkdir())
#print(path.rmdir())
#print(path.exists())
for file in path.glob('*.py'):
    print(file) 