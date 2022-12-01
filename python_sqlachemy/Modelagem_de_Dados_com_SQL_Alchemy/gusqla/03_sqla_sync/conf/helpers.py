import random
import string
from datetime import datetime


def gerar_string(frase: bool = False) -> str:
    """
    The gerar_string function generates a random string of characters.

    :param frase:bool=False: Determine if the string will be a name or description
    :return: A string of random letters and digits with a length of 10 or 30, depending on the value passed to it
    :doc-author: Trelent
    """
    # Para nomes, o tamanho é 10, para descrição ou algo do tipo, 30
    tamanho: int = 10
    if frase:
        tamanho = 30
    texto: str = ''.join(random.choices(string.ascii_lowercase + string.digits, k = tamanho))

    texto = ''.join([c if c.isalpha() else ' ' for c in texto])

    return texto


def gerar_int() -> int:
    """
    The gerar_int function generates a random integer between 1 and 100.

    :return: A random integer between 1 and 100
    :doc-author: Trelent
    """
    valor = random.randint(1, 100)

    return valor


def gerar_float(digitos: int = 1) -> float:
    """
    The gerar_float function generates a random float value.

    :param digitos:int=1: Set the number of digits that the float will have
    :return: A random float number with the specified digits
    :doc-author: Trelent
    """
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
    """
    The gerar_cor function generates a random hexadecimal color code.

    :return: A random hexadecimal color code
    :doc-author: Trelent
    """
    cor = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    return cor


def formata_data(data: datetime) -> str:
    """
    The formata_data function accepts a datetime object and returns a string
    representation of the datetime formatted according to ISO-8601.

    :param data:datetime: Receive a datetime object and return a string with the format dd/mm/yyyy às hh:mm:ss
    :return: A string in the format &quot;dd/mm/yyyy às hh:mm:ss&quot;
    :doc-author: Trelent
    """
    return data.strftime("%d/%m/%Y às %H:%M:%S")
