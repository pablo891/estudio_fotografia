from estudioFotografia import SessaoFotografia

cadastro = SessaoFotografia()
consulta = SessaoFotografia()
delete = SessaoFotografia()
update = SessaoFotografia()
individual = SessaoFotografia()

print('Seja Bem-vindo(a) ao estúdio de fotografia eternizando momentos')
while True:
    print('.' * 50 )
    option = int(input('Opções:\n1. Marcar Sessão\n2. Consultar todas as sessões\n3. Consultar sessão individual\n4. Deletar sessão\n5. Atualizar sessão\n6.Sair\n'))

    if option == 1:
        print('Informações de Cadastro', '-' * 30)
        
        cliente = input('Nome: ')
        data = input('Data da sessão: ')
        tipo = input('Tipo de serviço: ')
        preco = float(input('Preço: R$'))

        cadastro.cadastrarSessao(cliente, data, tipo, preco)

    elif option == 2:
        print('------------------- SESSÕES --------------------')
        consulta.consultarSessoes()

    elif option == 3:
        id = int(input('Informe a sessão: '))
        print('-' * 20)
        print('DADOS DA SESSÃO')
        individual.consultarSessaoIndividual(id)

    elif option == 4:
        id = int(input('Informe a sessão: '))
        print('-' * 20)
        delete.consultarSessaoIndividual(id)
        delete.deletarSessao(id)

    elif option == 5:
        id = int(input('Informe o ID da sessão: '))
        tipo = input('Informe o novo tipo de serviço: ')

        update.atualizarSessao(tipo, id)

    elif option == 6:
        print('Obrigado pela preferência')
        break

    else:
        print('Opção inválida, tente novamente')
    