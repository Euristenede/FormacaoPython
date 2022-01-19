url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Limeza da URL
url = url.strip()

#Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)