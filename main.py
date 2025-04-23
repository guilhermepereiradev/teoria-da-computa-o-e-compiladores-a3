from analise_lexica import AnaliseLexica

with open('code.txt', 'r', encoding='utf-8') as file:
    code = file.read()

print(code)

tokens = AnaliseLexica.de_token(code)

for token in tokens:
    print(token)