frase = "Cabeça de urubu nava haver com vento"

dividir = frase.split()
inverter = dividir[::-1]
espacos = " ".join(inverter)

print(f"Frase: {frase}\nQuantidade de letra {len(frase) - frase.count(' ')}\n{espacos}")