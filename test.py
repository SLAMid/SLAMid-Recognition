with open("test/images/dog.jpg", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print(b)