import string
import random

from datetime import datetime


def gerar_string(frase: bool = False) -> str:
    # Para nomes, o tamanho é 10, para descrição ou algo do tipo, 30
    tamanho: int = 10
    if frase:
        tamanho = 30
    texto: str = ''.join(random.choices(string.ascii_lowercase + string.digits, k = tamanho))

    texto = ''.join([c if c.isalpha() else ' ' for c in texto])

    return texto


def gerar_int() -> int:
    valor = random.randint(1, 100)

    return valor


def gerar_float(digitos: int = 1) -> float:
    valor: float = 0
    if digitos == 1:
        valor = random.uniform(1, 9)
    elif digitos == 2:
        valor = random.uniform(10, 99)
    elif digitos == 3:
        valor = random.uniform(100, 999)
    else:
        valor = random.uniform(1000, 99999)
    
    return round(valor, 2)


def gerar_cor() -> str:
    cor = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    return cor


def formata_data(data: datetime) -> str:
    return data.strftime("%d/%m/%Y às %H:%M:%S")
