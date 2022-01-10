def maximo(x,y):
    if (x>y):
        valorMaximo =  x
        return valorMaximo
    elif (x<y):
        valorMaximo = y
        return valorMaximo
    
    else:
        valorMaximo = x
        return valorMaximo

def test_maximo5():
    assert maximo(0,5) == 5


 
def test_maximo9():
    assert maximo(9,5) == 9


     
def test_maximo33():
    assert maximo(33,-9) == 33


     
def test_maximo_menos9():
    assert maximo(-9,-388) == -9

     
def test_maximo0():
    assert maximo(0,5) == 5

def teste_maximo_iguais():
    assert maximo(9,9) == 9
    
va = maximo(8,9)
print(va)