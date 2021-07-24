'''from pathlib import Path

path = Path("")
print(path.exists())'''

'''from pathlib import Path

path = Path("emails")
print(path.rmdir())'''

from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)