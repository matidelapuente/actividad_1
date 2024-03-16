import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_attempts = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adiviananzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

fails = 0
while fails < max_attempts:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya ha sido adivinada
    # Si ingresa por segunda vez una letra incorrecta, se cuenta como un solo error
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter == "":
        print("Debes ingresar una letra")
    elif letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails += 1

    # Mostrar la palabra parcialmente adivinadaz
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
          letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    #print("Errores cometidos: ", fails)
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} errores permitidos.")
    print(f"La palabra secreta era: {secret_word}")