# MAYZE DOS ANJOS NUNES

#-------------------------------- Cifra de Vigenere --------------------------------

def CifraVigenere(palavra, chave, modo='criptografar'):

    palavra_gerada = []     # Lista vazia que guardara cada letra gerada pela criptografia, no final, formara uma palavra completa
    chave = chave.upper()   # Transforma cada letra da senha em maiuscula para facilitar o calculo
    indice_chave = 0        # Controle das letras que estao sendo inseridas

    for caractere in palavra:

        # Verifica se o caractere da vez eh realmente uma letra
        if caractere.isalpha():   

            maiusculo = caractere.isupper()   # Verifica se a letra eh maiuscula
            base = 65 if maiusculo else 97    # Se 'maiusculo' for TRUE, a 'base' vale 65, senao vale 97

            letra_num = ord(caractere) - base                        # Transforma a letra em numero
            chave_num = ord(chave[indice_chave % len(chave)]) - 65   # Faz o sistema ser ciclico para com o tamanho da chave

            if modo == 'criptografar':
                numero_novo = (letra_num + chave_num) % 26
            else:
                numero_novo = (letra_num - chave_num + 26) % 26

            palavra_gerada.append(chr(numero_novo + base))   # Adiciona a letra resultante na lista 'palavra_gerada'
            indice_chave += 1

        # Para o caso de o caractere ser um numero, espaco ou pontuacao
        else:   
            # Nao eh feita nenhuma matematica, so adiciona-o na palavra gerada do jeito que esta, mas nao roda o indice da chave
            palavra_gerada.append(caractere)

    return "".join(palavra_gerada)   # Pega todos os elementos da lista e junta tudo em uma unica string para mostrar o resultado


#-------------------------------- Executando o programa --------------------------------

# Chave
chave = 'artyom'

# Palavra que sera a resposta final
palavra_final = []

# Lendo a palavra do usuario
usuario = input("\nDigite uma palavra: ").lower()   # Depois da leitura, transforma todas as suas letras para minusculo
tamanho = len(usuario)                              # Descobrindo o tamanho da palavra

# ------ Formando a palavra criptografada ------

palavra_vigenere = CifraVigenere(usuario, chave, modo='criptografar')   # Chamando a funcao
palavra_final.append(palavra_vigenere)            # Adicionando a palavra criptografada na palavra final

# ------ Formando a palavra misturada ------

palavra_final.append(usuario[0])   # Adicionando a primeira letra

if tamanho > 2:   # Se tiver mais de 2 letras faz sentido fazer a parte de inverter o meio

    # Removendo letras
    palavra_misturada = usuario[1:]              # a primeira
    palavra_misturada = palavra_misturada[:-1]   # a ultima

    inverter_mistura = palavra_misturada[::-1]   # Invertendo o restante da palavra
    palavra_final.append(inverter_mistura)       # Adicionando a palavra invertida

if tamanho >= 2:   # So faz sentido pegar a ultima letra se existir 2 ou mais letras
    
    palavra_final.append(usuario[tamanho-1])   # Adicionando a ultima letra da palavra original

# ------ Formando a ultima parte da palavra ------

if tamanho > 2:
    # Se tiver mais de 2 letras:
        #se a quantidade de letras for par => pega todas as vogais
        #se a quantidade for impar => pega as consoantes

    if tamanho % 2 == 0:
        for letra in usuario:
            if letra in "aeiou":
                palavra_final.append(letra)
    else:
        for letra in usuario:
            if letra not in "aeiou":
                palavra_final.append(letra)
else:
    if tamanho == 2:
        # Se tiver exatamente 2 letras:
            #verifica se a primeira letra eh consoante, se for => eh selecionada

        if usuario[0] not in 'aeiou':
            palavra_final.append(usuario[0])
            
    else:
        # Se tiver somente 1 letra:
            #verifica se a primeira letra eh vogal, se for => eh selecionada
        
        if usuario[0] in 'aeiou':
            palavra_final.append(usuario[0])

# ------ Formando a saida ------

saida = "".join(palavra_final)   # Juntando todos os elementos da lista em uma unica string
print(f"Saída: {saida}\n")       # Imprimindo a string resultante
