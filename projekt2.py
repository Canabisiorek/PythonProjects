password = input("Podaj hasło: ")
digit = False
upper = False
lower = False
special = False
space = False
for char in password:
    if char.isdigit():
        digit = True
    elif char.islower():
        lower = True
    elif char.isupper():
        upper = True
    elif not char.isalnum():
        special = True
    elif  char.isspace():
        space = True
        
if not digit:
    print("Brakuje Cyfry")
if not lower :
    print("Brak małego znaku")
if not upper :
    print("Brak wielkiego znaku")
if len(password)<8:
    print("Hasło powinno mieć przynajmniej 8 znaków")
else:
    pass_length = True
if not special :
    print("Brakuje znaku specjalnego")
if space:
    print("Hasło nie powinno zawierać spacji")

is_correct =  digit and lower and upper and not space and pass_length and special
if is_correct:
    print("Hasło poprawne")




