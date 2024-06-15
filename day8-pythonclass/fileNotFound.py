try:
  file = open("nonexistent.txt","r")
  c = file.read()
  file.close()
except FileNotFoundError:
  print("file not found!")