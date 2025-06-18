# Desafio Digital Innovation One
Trilha Python. 

## Objetivos:
Modificar um algoritmo de conta bancária simples. A proposta é da plataforma Digital Innovation One como primeiro desafio da trilha Python. Url do projeto original: [Conta bancário: DIO](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)

## Propostas da trilha Python:
* Para a primeira versão do sistema devemos implementar apenas 3operações: depósito, saque e extrato.
* Deve ser possível depositar valores positivos para a conta bancária.
* O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
* Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o
saldo atual da conta.
* Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
* Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45.

## Modificações:
* Função ```Limpa_tela()``` através do módulo os.
* Entrada de dados com ```input()``` que somente aceitará números inteiros e de ponto flutuante, com ponto e vírgula, assim com o devido tratamento com ```try except```.
* Saída de dados formatados na moeda brasileira.
* Adição de Comentários.
* Adição de ícones.

## Ferramentas utilizadas:
* Linguagem de programação Python 3.9.13
* Ambiente virtual VENV
* Git/GitHub
* Visual studio code
* Windows 10

## Modo de utilizar: 
* Clonar repositório.
* Acessar o diretório ```'cd desafio-python-dio```.
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar a dependência, caso o projeto as tenha.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## Contribuição:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## Licença:
Este projeto é licenciado sob a Licença MIT.

## Comandos importantes
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.