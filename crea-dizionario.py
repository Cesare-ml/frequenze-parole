# lettere da escludere
excluded_letters = {'x', 'y', 'w', 'k', 'j'}

# lettere valide con valori da 1 a 21
valid_letters = [chr(i) for i in range(97, 123) if chr(i) not in excluded_letters]
letter_values = {letter: idx + 1 for idx, letter in enumerate(valid_letters)}

def calcola_frequenza(parola):
    parola = parola.lower()
    return sum(letter_values.get(c, 0) for c in parola if c in letter_values)

# input/output file
input_file = "it_50k.txt"
output_file = "frequenze.js"

data = []

with open(input_file, "r", encoding="utf-8") as infile:
    for linea in infile:
        parola = linea.split()[0].lower()

        # ignora parole con lettere escluse o non alfabetiche
        if any(c in excluded_letters for c in parola) or not parola.isalpha():
            continue

        frequenza = calcola_frequenza(parola)
        data.append([parola, frequenza])

# scrivi file .js con array
with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("const frequenzeParole = [\n")
    for parola, frequenza in data:
        f_out.write(f'  ["{parola}", {frequenza}],\n')
    f_out.write("];\n")
