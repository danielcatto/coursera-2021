
def vogais(letra):
    letra_upper = letra.lower()

    if letra_upper == 'a' or letra_upper == 'e' or letra_upper == 'i' or letra_upper == 'o' or letra_upper == 'u':
        return True
    else:
        return False

print(vogais('e'))