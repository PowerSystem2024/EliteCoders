seleccionArgentina = {
    10:{"Nombre":"Lionel Messi", "Edad":35,"Altura":1.70,"Precio":"50 Millones", "Posicion":"Extremo Derecho"},
    11:{"Nombre":"Angel Di Maria", "Edad":34,"Altura":1.80,"Precio":"12 Millones", "Posicion":"Extremo Derecho"},
    24:{"Nombre":"Paulo Dybala", "Edad":28,"Altura":1.77,"Precio":"35 Millones", "Posicion":"Media Punta"},
    19:{"Nombre":"Nicolas Otamendi", "Edad":34,"Altura":1.83,"Precio":"3.5 Millones", "Posicion":"Defensa Central"},
    1:{"Nombre":"Franco Armani", "Edad":35,"Altura":1.89,"Precio":"3.5 Millones", "Posicion":"Portero"}
}

print(seleccionArgentina[10])
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(f'\n')
seleccionArgentina[23] = {"Nombre":"Emiliano Martinez", "Edad":32,"Altura":1.95,"Precio":"28 Millones", "Posicion":"Portero"}
seleccionArgentina[9] = {"Nombre":"Julian Alvarez","Edad":24,"Altura":1.70,"Precio":"104 Millones","Posicion":"Media Punta"}
seleccionArgentina[7] = {"Nombre":"Rodrigo de Paul", "Edad":30,"Altura":1.78,"Precio":"37 Millones", "Posicion":"Centrocampista"}
seleccionArgentina[14] = {"Nombre":"Enzo Fernandez", "Edad":23,"Altura":1.78,"Precio":"121 Millones", "Posicion":"Mediocampista"}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(f'\n')
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')