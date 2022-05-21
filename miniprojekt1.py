input_file = input("Podaj plik do wejściowy: ")
output_file = input("Podaj plik wyjściowy: ")
with open(input_file, 'r') as stream:
    text = stream.read()
for char in text:
    if char.isdigit():
        text = text.replace(char, "X")
if output_file == "":
    print(text)
else:
    with open(output_file, 'x') as writer:
        writer.write(text)
    print("SUKCES")

