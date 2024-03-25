import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_attempts = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adiviananzas!")
difficulty = input("Elige el nivel de dificultad: facil (F), medio (M) o dificil (D): ")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

if difficulty.lower() == "d":
    word_displayed = "_" * len(secret_word)
elif difficulty.lower() == "m":
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
else:
    vocales = ["a", "e", "i", "o", "u"]
    letters = []
    for letter in secret_word:
        if letter in vocales:
          letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(word_displayed)

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
    word_displayed_list = list(word_displayed)

    for pos in range(len(secret_word)):
        if secret_word[pos] in guessed_letters:
            word_displayed_list[pos] = secret_word[pos]

    word_displayed = "".join(word_displayed_list)
    print(f"Palabra: {word_displayed}")
    #print("Errores cometidos: ", fails)
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} errores permitidos.")
    print(f"La palabra secreta era: {secret_word}")