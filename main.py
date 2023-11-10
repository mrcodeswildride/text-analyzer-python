print()

text = input("Enter some text:\n")

characters = {}
num_chars = 0

for character in text:
  if character != " ":
    if character not in characters:
      characters[character] = 0

    characters[character] += 1
    num_chars += 1

print()

for character, count in characters.items():
  decimal = count / num_chars
  percent = decimal * 100
  print(f"{character}: {percent:.2f}%")
