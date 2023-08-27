adres = input("Tanpri antre adrès IP a: ")
ip = adres.split('.')



som = sum(int(digit) for digit in ''.join(ip))

#print(som)

port = som * int(ip[0][0])

print(f"Pòt ki ouvri a se: {port}")
