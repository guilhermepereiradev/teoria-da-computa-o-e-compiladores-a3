import re
from typing import List

class Token:
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}')"

class AnaliseLexica:
    KEYWORDS = r'\b(se|senao|enquanto|para|retornar|numero|frase|inicio|fim)\b'
    IDENTIFIER = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    NUMBER = r'\b\d+(\.\d+)?\b'
    OPERATOR = r'[+\-*/=<>!]+'
    SYMBOL = r'[{}();,]'
    STRING = r'"[^"\n]*"'

    pattern = re.compile(
        f'(?P<KEYWORDS>{KEYWORDS})|'
        f'(?P<IDENTIFIER>{IDENTIFIER})|'
        f'(?P<NUMBER>{NUMBER})|'
        f'(?P<OPERATOR>{OPERATOR})|'
        f'(?P<SYMBOL>{SYMBOL})|'
        f'(?P<STRING>{STRING})'
    )

    @staticmethod
    def de_token(code: str) -> List[Token]:
        tokens = []
        for match in AnaliseLexica.pattern.finditer(code):
            for tipo in [ 'SYMBOL', 'STRING', 'KEYWORDS', 'IDENTIFIER', 'NUMBER', 'OPERATOR']:
                if match.group(tipo):
                    tokens.append(Token(tipo, match.group(tipo)))
                    break
        return tokens
