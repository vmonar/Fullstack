lenguajes = ["python", "C++", "go", "java", "javascript"]
# print(type(lenguajes))

print(lenguajes[1])
# lenguajes[1] = "ruby"
print(lenguajes[1])
print(lenguajes)

print(lenguajes[1:4])
print(lenguajes[:3])

lenguajes.insert(3, "dart")
print(lenguajes)

lenguajes.remove("dart")
print(lenguajes)

print("php" in lenguajes)