def cadastro_atendimento(matricula, nome_aluno, duvida, data):
    novo_atendimento = {
        'matricula': matricula,
        'nome_aluno': nome_aluno,
        'duvida': duvida,
        'data': data
    }
    adicionar_arquivo(novo_atendimento)
    print('Registro salvo com sucesso!')

def adicionar_arquivo(atendimento):
    with open('cadastro.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write('Matrícula do aluno: '+atendimento['matricula']+'\n')
        arquivo.write('Nome do aluno: '+atendimento['nome_aluno']+'\n')
        arquivo.write('Dúvida do aluno: '+atendimento['duvida']+'\n')
        arquivo.write('Data do atendimento: '+atendimento['data']+'\n\n')

def lista_atendimentos():
    print('\nLista de atendimentos\n')
    listar_arquivo()

def listar_arquivo():
    with open('cadastro.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            print(linha, end='')

def busca_atendimento(matricula):
    with open('./cadastro.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        encontrado = False
        for i in range(len(linhas)):
            if f'Matrícula do aluno: {matricula}' in linhas[i]:
                encontrado = True
                print(f'\n--- Atendimentos do Aluno ({matricula}) ---')                    
                print(linhas[i].strip())
                print(linhas[i+1].strip())
                print(linhas[i+2].strip())
                print(linhas[i+3].strip())
                print('-' * 30)
        if not encontrado:
            print('\nNenhum atendimento encontrado para esta matrícula.')
               
def atualizacao_assunto(matricula, data, duvida):
    linhas = []
    with open('cadastro.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    atualizado = False
    for i in range(0, len(linhas), 5):
        if f'Matrícula do aluno: {matricula}' in linhas[i] and f'Data do atendimento: {data}' in linhas[i+3]:
            linhas[i+2] = f'Dúvida do aluno: {duvida}\n'
            atualizado = True
            break
    if atualizado:
        with open('./cadastro.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        print('Dúvida atualizada com sucesso')
    else:
        print('\nRegistro não encontrado. Verifique a matrícula e a data.')

def remocao_atendimento(matricula, data):
    with open('cadastro.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    lista_atendimentos = []
    removido = False
    i = 0
    while i < len(linhas):
        if i+3 < len(linhas):
            if not (f'Matrícula do aluno: {matricula}' in linhas[i] and f'Data do atendimento: {data}' in linhas[i+3]):
                lista_atendimentos.extend(linhas[i:i+5])
            else:
                removido = True
            i += 5
        else:
            lista_atendimentos.append(linhas[i])
            i += 1
    if removido:
        with open('cadastro.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(lista_atendimentos)
        print('\nAtendimento deletado com sucesso!')
    else:
        print('\nRegistro não encontrado para exclusão.')
