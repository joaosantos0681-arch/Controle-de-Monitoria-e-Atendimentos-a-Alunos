import operacoes

def menu_principal():
    print('\n-----------')
    print('\nBem-vindo à monitoria. Selecione a opção:')
    print('[1]: Cadastrar um atendimento')
    print('[2]: Listar todos os atendimentos do mês')
    print('[3]: Listar atendimentos de um aluno')
    print('[4]: Atualizar assunto de um atendimento')
    print('[5]: Deletar um registro')
    print('[6]: Sair')

def main():
    while True:
        menu_principal()
        opcao = input('\nSelecione a opção de 1 a 6: ')
        if opcao == '1':
            matricula = input('Informe a matrícula de um aluno: ')
            nome_aluno = input('Informe o nome do aluno: ')
            duvida = input('Informe a dúvida do aluno: ')
            data = input('Informe a data do atendimento (DD/MM/AAAA): ')
            operacoes.cadastro_atendimento(matricula, nome_aluno, duvida, data)
        elif opcao == '2':
            print('Atendimentos do mês: ')
            operacoes.lista_atendimentos()
        elif opcao == '3':
            matricula = input('Informe a matrícula de um aluno para a busca: ')
            operacoes.busca_atendimento(matricula)
        elif opcao == '4':
            matricula = input('Informe a matrícula de um aluno para a atualização: ')
            data = input('Informe a data que aconteceu o atendimento (DD/MM/AAAA): ')
            duvida = input('Informe a dúvida nova: ')
            operacoes.atualizacao_assunto(matricula, data, duvida)
        elif opcao == '5':
            matricula = input('Informe a matrícula de um aluno para a remoção: ')
            data = input('Informe a data que aconteceu o atendimento (DD/MM/AAAA): ')
            operacoes.remocao_atendimento(matricula, data)
        elif opcao == '6':
            print('\nEncerrando')
            break
        else:
            print('\nOpção inválida')


if __name__ == '__main__':
    main()
