

def Comparacao(nome_original, nome_digitado):
    '''
    Essa classe receberá dois argumentos, o nome original e o nome que foi digitado. Tera tres "Estações" (fase que ira
    avaliar e descobrir se eles são parecidos e/ou identicos). A primeira Estação ira verificar se eles são identico.
    O segundo ira verificaar se eles são parecidos. O terceiro ira verificar se o nome digitado é o primeiro nome do
    nome original. Se em alguma dessas estações tiver uma determinada porcentagem de igualdade vai ser retornado
    "True", se não tiver essa porcentagem vai ser retornado "False"
    '''
    def Estacao_1_e_2(nome, nome_digitado):
        # Criando algumas variaveis que vamos usr nessa função...
        letras_ja_verificadas = []
        letras_iguais = 0
        qntd_letras_no_nome = 0
        cont = 0

        # Vamos tirar todos os espaços para a pesquisa ficar mais inteligente
        nome_digitado = nome_digitado.replace(' ', '').lower()
        nome = nome.replace(' ', '').lower()

        if nome == nome_digitado:
            # Mostrar so um aluno
            return True

        # Vamos comparar letra por letra
        for letra in nome_digitado:
            # Esse try é para não dar erro se o nome digitado for maior que o nome original, o cont estaria
            # fora do intervalo do nome. Então deixamos a variael vazia para conrinuar se der erro no nome original.
            letra_original = ''
            try:
                # Pegando a letra do nome original na mesma posição da letra do "for"
                letra_original = nome[cont]
            except:
                pass

            if letra == letra_original:
                letras_iguais += 1

            # Se a letra não for igual, então vamos perguntar se tem essa letra no nome. OBS: Essa opção esta
            # no elif porque a opção anterior é mais importante.
            if letra not in letras_ja_verificadas and letra in nome:
                qntd_letras_no_nome += 1
                letras_ja_verificadas.append(letra)

            cont += 1

        '''
        Só vamos retornar True se a quantidade de letras iguais for maior que 55% do nome original, ou se a quantidade
        de letras iguais for maior ou igual a 80% do nome original, e se o nome digitado for menor ou igual a 175% do 
        nome original, ex: um nome com 4 letras sera aceito se o nome digitado tiver até 7 letras (4 * 1.75 = 7).
        '''
        if letras_iguais >= len(nome_digitado) * 0.7 or qntd_letras_no_nome >= len(nome) * 0.8 and len(nome_digitado) <= len(nome) * 1.75:
            # O nome tem uma semelhança com o nome original
            return True

        else:
            # O nome NÃO tem uma semelhança com o nome original
            return False

    def Estacao_3(nome, nome_digitado):
        # Vamos obter apenas o primeiro nome
        try:
            nome = nome.split(' ')
            nome_digitado = nome_digitado.split(' ')
            return Estacao_1_e_2(nome[0], nome_digitado[0])

        except:
            return False

    # Vamos verificar se os nomes tem uma semelhança entre eles
    if Estacao_1_e_2(nome_original, nome_digitado):
        return True

    # Se os nomes não forem semelhantes tem a possibilidade do usuario ter digitado apenas o primeiro nome,
    # então vamos verificar se é o primeiro nome e se esse nome esta digitado corretamente
    else:
        return Estacao_3(nome_original, nome_digitado)

def FormarGrupos(qntd_grupos: int, lista_nomes: list):
    from random import choice  # Para importar somente quando for usar essa função

    def Formando_os_grupos(qntd_loop, oq_fazer, lista):
        '''A "qntd_loop" é a quantidade de vezes que o loop vai rodar. O "oq_fazer" é para saber se é para criar uma
        matriz ou formar os grupos, onde True é para criar a matriz e False é para formar os grupos'''
        cont = 0
        for _ in range(qntd_loop):
            if oq_fazer:
                lista.append([f'Grupo {cont + 1}:'])  # Para não começar com 0

            else:
                nome = choice(lista_nomes)  # Escolher nome aleatoriamente
                lista_nomes.pop(lista_nomes.index(nome))  # Tirar o nome da lista

                lista[cont].append(nome)

                if cont == len(lista) - 1:
                    cont = -1  # Para zerar qunado passar pelo "cont += 1"

            cont += 1

        return lista

    # Para criar a matriz dos grupos
    grupos = Formando_os_grupos(qntd_grupos, True, [])

    # Retornar a matriz dos grupos com os nomes aleatorios
    return Formando_os_grupos(len(lista_nomes), False, grupos)


