from operacoesbd import *

'''Equipe:
1 - Maria Gabriela Pereira da Silva
2 - Inácio Herculano da Silva Neto
3 - João Henrique Leite da Silva
4 - João Paulo Sigieski Bonetti
5 - Rayanne Vanessa Figueiredo da Silva
6 - Waleska Vitor Almeida
'''

#tratativa para verificar se os caracteres digitados possuem apenas letras.
def verificarNome(nome):
    for i in nome:
        if i in numeros:
            return True

conexao = abrirBancoDados('localhost','root','1234','ouvidoria')

opcao = 0
separadores = '•' * 60

# Utilizamos separadores para identificar a saudação e menu
print(separadores)
print('Olá, seja bem-vindo(a) à Ouvidoria Unifacisa!')
print("Para acessar nossos serviços, utilize as opções abaixo:")
print(separadores)

while opcao != 5:
    print()
    print('• MENU •')
    print()
    print('1) Listar as ocorrências')
    print('2) Adicionar nova ocorrência')
    print('3) Remover uma ocorrência')
    print('4) Pesquisar uma ocorrência pelo código')
    print('5) Sair')
    print()
    print(separadores)

    # Se o dado recebido for um número entre 1 e 5, a ação será executada, caso contrário, será solicitada nova entrada.

    try:
        opcao = int(input('Por favor, informe o número da opção desejada: '))
        print()
    except:
        print('Operação inválida. Por favor, digite um número de 1 à 5, correspondente a opção desejada.')
        print()

    naoHaOcorrencia = 'Nenhuma ocorrência cadastrada no sistema.'
    codigoInvalido = 'Não há ocorrência com este código. Por favor, digite um código válido.'
    operacaoInvalida = 'Operação inválida.'

    if opcao == 1:
        exibeOcorrencia = 'select * from ocorrencia'
        listaOcorrencia = listarBancoDados(conexao,exibeOcorrencia)

        if len(listaOcorrencia) == 0:
            print(naoHaOcorrencia)

        else:
            print('Listagem de ocorrências: ')
            print()
            for reclamacao in listaOcorrencia:
                print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])

    elif opcao == 2:
        #lista de verificação a ser utilizada no método verificarNome().
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nome = input('Digite seu nome: ')
        if verificarNome(nome):
            print()
            print('Por favor, digite seu nome apenas utilizando letras')

        else:
            print()
            ocorrencia = input('Digite sua reclamação: ')

            adicionaNovoFilme = 'insert into ocorrencia (nome_pessoa,reclamacao) values (%s,%s)'
            dados = (nome, ocorrencia)
            insertNoBancoDados(conexao, adicionaNovoFilme, dados)

            consultaCodigo = 'select codigo_ocorrencia from ocorrencia'
            listaCodigo = listarBancoDados(conexao,consultaCodigo)
            print()
            print('Ocorrência  adicionada com sucesso.')

    elif opcao == 3:
        exibeOcorrencia = 'select * from ocorrencia'
        listaOcorrencia = listarBancoDados(conexao,exibeOcorrencia)
        listaOcorrenciaTamanhoInicial = len(listaOcorrencia)

        if len(listaOcorrencia) == 0:
            print(naoHaOcorrencia)

        else:

            for reclamacao in listaOcorrencia:
                print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])

            #Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
            try:
                print()
                codigo = input('Digite o código da ocorrência a ser removida: ')
                consultaRemoverOcorrenciaCodigo = 'delete from ocorrencia where codigo_ocorrencia = %s '
                dados = (codigo,)
                excluirBancoDados(conexao, consultaRemoverOcorrenciaCodigo, dados)
                print()
                exibeOcorrenciaFinal = 'select * from ocorrencia'
                listaOcorrenciaFinal = listarBancoDados(conexao, exibeOcorrenciaFinal)
                listaOcorrenciaTamanhoFinal = len(listaOcorrenciaFinal)
                if listaOcorrenciaTamanhoInicial == listaOcorrenciaTamanhoFinal:
                    print('Não há ocorrência cadastrada com o código pesquisado.')
                else:
                    print('Ocorrência removida com sucesso.')
                print()

            except:
                print(operacaoInvalida)


    elif opcao == 4:
        exibeOcorrencia = 'select * from ocorrencia'
        listarOcorrencia = listarBancoDados(conexao,exibeOcorrencia)

        for reclamacao in listarOcorrencia:
            print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])

        print()

        #Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
        try:
            codigo = input('Digite o código da ocorrência a ser pesquisada: ')
            consultaListagem = 'select * from ocorrencia where codigo_ocorrencia = ' + codigo
            listaOcorrencia = listarBancoDados(conexao, consultaListagem)

            if len(listaOcorrencia) == 0:
                print('Não existem ocorrências disponíveis com este código!')
            else:
                print()
                print('Listagem de Filmes')
                for ocorrencia in listaOcorrencia:
                    print('Código', ocorrencia[0], 'nome: ', ocorrencia[1], 'ocorrencia:', ocorrencia[2],)

        except:
            print(operacaoInvalida)

    elif opcao < 0 or opcao > 5:
        print(operacaoInvalida)

print('Obrigado por usar nosso canal. A sua opinião é muito importante para nós!')

encerrarBancoDados(conexao)
