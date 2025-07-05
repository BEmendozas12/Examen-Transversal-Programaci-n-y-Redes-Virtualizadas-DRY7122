# verificar_as.py
as_numero = int(input("Ingrese el número de AS: "))
if (64512 <= as_numero <= 65534) or (4200000000 <= as_numero <= 4294967294):
    print("AS Privado")
else:
    print("AS Público")
