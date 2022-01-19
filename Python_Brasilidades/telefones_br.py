import re
class TelefonesBr:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número Incorreto!!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(3)}"
        return numero_formatado

#Testes no main para encontrar padrões
"""" encontrando padrões em texto
import re
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())
"""
""" encontrando email dentro de um texto
import re
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "Olá meu email é euristenedesantos@gmail.com.br entre em contato"
resposta = re.search(padrao, texto)
print(resposta.group())
"""
"""" Encontrando número de telefone em um texto
import re
padrao_molde = "(xx) x aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do número 2126451234 e também do 2136431234"
resposta = re.findall(padrao, texto)
print(resposta)
"""