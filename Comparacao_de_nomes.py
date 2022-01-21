

def Comparacao(nome_original, nome_digitado):
    '''
    Essa classe receberá dois argumentos, o nome que foi digitado e o nome original. Tera tres "Estações" (fase que ira
    avaliar e descobrir se eles são parecidos e/ou identicos). A primeira Estação ira verificar se eles são identico.
    O segundo ira verificaar se eles são parecidos. O terceiro ira verificar se o nome digitado é o primeiro nome do
    nome original. Se em alguma dessas estações tiver uma determinada porcentagem de igualdade vai ser retornado
    "True", se não tiver essa porcentagem vai ser retornado "False"
    '''
    def Estacao_1_e_2(nome, nome_digitado):
        # Criando algumas variaveis que vamos usr nessa função...
        letras_ja_verificadas = []
        letras_iguais = 0
        qntd_letras_que_contem_no_nome = 0
        cont = 0

        # Vamos tirar todos os espaços para a pesquisa ficar mais inteligente
        nome_digitado = nome_digitado.replace(' ', '').lower()
        nome = nome.replace(' ', '').lower()

        if nome == nome_digitado:
            # Mostrar so um aluno
            return True

        # Vamos comparar letra por letra
        for letra in nome_digitado:
            # Esse try é para não dar erro se o nome digitado for maior que o nome do aluno, o cont estaria
            # fora do intervalo do nome.
            try:
                # Pegando a letra do nome do aluno na mesma posição da letra do "for"
                letra_aluno = nome[cont]

                if letra == letra_aluno:
                    letras_iguais += 1

                # Se a letra não for igual, então vamos perguntar se tem essa letra no nome. OBS: Essa opção esta
                # no elif porque a opção anterior é mais importante.
                elif letra in list(nome) and letra not in letras_ja_verificadas:
                    qntd_letras_que_contem_no_nome += 1
                    letras_ja_verificadas.append(letra)

            except:
                pass

            cont += 1

        '''
        Só vamos adicionar esse aluno na tabela se a quantidade de letras iguais for maior ou igual a metade da
        quantidade de letras do nome do aluno, ou seja, se for maior ou igual a 50% do nome. Ou vamos adicionar se 
        a quantidade de letras que tem no nome seja maior ou igual a 80% da quantidade de letras do nome do aluno 
        '''
        if letras_iguais >= len(nome) * 0.55 or qntd_letras_que_contem_no_nome >= len(nome) * 0.8:
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

