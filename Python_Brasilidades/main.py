from telefones_br import TelefonesBr
from cpf_cnpj import Documento
from datas_br import DataBr
from acesso_cep import BuscaEndereco
#Valida cpf e cnpj
cpf = "98897820069"
documento = Documento.cria_documento(cpf)
print(documento)
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
print("_______________________________")
#Valida números de telefone
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
print("_______________________________")
#Valida data de cadastro
cadastro = DataBr()
print(cadastro)
print(cadastro.dia_da_semana())
print(cadastro.mes_cadastro())
print(cadastro.tempo_cadastro())
print("_______________________________")
#Acessando cep via api (viacep)
cep = 73920000
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
a = objeto_cep.acessa_via_cep()
print(a)