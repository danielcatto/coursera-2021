'''
converter segundos para minutos horas e dias
e vice-versa
HORAS [MULTIPLICA POR 60] MINUTOS [MULTIPLICA POR 60] SEGUNDOS
SEGUNDOS [DIVIDE POR 60] MINUTOS [DIVIDE POR 60] HORAS
'''

segundos = 500000

minutos = segundos / 60
horas = minutos // 60

print("minutos ",minutos)
print("horas", horas)