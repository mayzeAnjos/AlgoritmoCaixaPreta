# MAYZE DOS ANJOS NUNES

#-------------------------------- Cifra de Vigenere --------------------------------

def CifraVigenere(palavra, chave, modo='criptografar'):

    palavra_gerada = []     # Lista vazia que guardara cada letra gerada pela criptografia, no final, formara uma palavra completa
    chave = chave.upper()   # Transforma cada letra da senha em maiuscula para facilitar o calculo
    indice_chave = 0        # Controle das letras que estao sendo inseridas

    for caractere in palavra:
        if caractere.isalpha():   # Verifica se o caractere da vez eh realmente uma letra

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

        else:   # Para o caso de o caractere ser um numero, espaco ou pontuacao
            # Nao eh feita nenhuma matematica, so adiciona-o na palavra gerada do jeito que esta, mas nao roda o indice da chave
            palavra_gerada.append(caractere)

    return "".join(palavra_gerada)   # Pega todos os elementos da lista e junta tudo em uma unica string para mostrar o resultado


#-------------------------------- Executando o programa --------------------------------

# Chave
chave = 'artyom'

# Palavra que sera a resposta final
palavra_final = []

# Lendo a palavra do usuario
usuario = input("Digite uma palavra: ")
tamanho = len(usuario)   # Descobrindo o tamanho da palavra

# Formando a palavra criptografada
palavra_vigenere = CifraVigenere(usuario, chave, modo='criptografar')   # Chamando a funcao
palavra_final.append(palavra_vigenere)     # Adicionando a palavra criptografada na palavra final

# --- Formando a palavra misturada ---

palavra_final.append(usuario[0])   # Adicionando a primeira letra

# Removendo letras
palavra_misturada = usuario[1:]             # a primeira
palavra_misturada = palavra_misturada[:-1]   # a ultima

inverter_mistura = palavra_misturada[::-1]   # Invertendo o restante da palavra

palavra_final.append(inverter_mistura)     # Adicionando a palavra invertida
palavra_final.append(usuario[tamanho-1])   # Adicionando a ultima letra da palavra original

# --- --- --- --- --- --- --- --- --- ---

# Formando a saida
saida = "".join(palavra_final)   # Juntando todos os elementos da lista em uma unica string
print(f"Saída: {saida}")         # Imprimindo a string resultante