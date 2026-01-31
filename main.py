import json

def salvar_tarefas(lista_de_tarefas):
    with open('tarefas.json', 'w', encoding = 'utf-8') as arquivo:
        json.dump(lista_de_tarefas, arquivo, indent=4, ensure_ascii=False)
    print('Dados salvos com sucesso!')


def carregar_tarefas():
    try:
        with open('tarefas.json', 'r', encoding = 'utf-8')as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    except Exception as e:
        print(f'Erro ao carregar: {e}')
        return []
    
minhas_tarefas = carregar_tarefas()

if not minhas_tarefas:
    minhas_tarefas.append({'nome': 'Meu primeiro registro', 'concluida': False})
    salvar_tarefas(minhas_tarefas)

def listar_tarefas(tarefas):
    if not tarefas:
        print('\nSua lista está vazia.')
        return
    
    print('\n---MINHAS TAREFAS---')
    for i, tarefa in enumerate(tarefas):
        status = '✔' if tarefa['concluida'] else ''
        print(f'{i+1}.[{status}] {tarefa['nome']}')
    print('-'*10)

def adicionar_tarefa(tarefas):
    nome = input('\nDigite o nome da tarefa: ').strip()
    if nome:
        nova_tarefa = {'nome': nome, 'concluida': False}
        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    else:
        print('Erro: o nome da tarefa não pode estar vazio.')

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input('\nDigite o numero da tarefa para concluir: ')) -1
        if 0 <= indice < len(tarefas):
            tarefas[indice]['concluida'] = True
            salvar_tarefas(tarefas)
            print('Tarefa marcada como concluida!')
        else:
            print('Esse número de tarefa não existe.')
    except ValueError:
        print('Por favor, digite um número válido.')

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input('\nDigite o número da tarefa que deseja remover: '))-1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida['nome']}' removida!")
        else:
            print('Esse número de tarefa não existe.')
    except ValueError:
        print('Entrada inválida. Digite apenas números.')


def menu():
    tarefas = carregar_tarefas()

    while True:
        print('\n======GERENCIADOR DE TAREFAS ======')
        print('1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Concluir tarefa')
        print('4. Remover tarefa')
        print('5. Sair')

        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            print('Saindo... Até logo!')
            break
        else:
            print('Opção inválida! Tente novamente.')


if __name__ == '__main__':
    menu()