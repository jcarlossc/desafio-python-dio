import os

# Método para limpar tela.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Chama a função antes do menu.
limpar_tela()

# Variável do menu.
menu = """
================= PYTHON =================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================================
Escolha uma operação => """

# Variáveis do sistema.
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Estrutura que centraliza o sistema.
while True:
    # Entrada para escolha das operações.
    opcao = input(menu)

    # Estrutura que centraliza os depósitos.
    if opcao == "d":
        # Entrada dos depósitos que somente aceita int e float, com ponto ou vírgula.
        try:
            valor_deposito = float(input("Digite o valor do depósito: ").strip().replace(",", "."))

        except ValueError:
            limpar_tela()
            print("❌ Operação de depósito falhou! Valor inválido.")
            continue
        
        # Testa os valores dos depósitos.
        if valor_deposito <= 0:
            limpar_tela()
            print("❌ Operação de depósito falhou! O valor informado é inválido.")
        
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:,.2f}\n".replace(",", "X").replace(".", ",").replace("X", ".")
            limpar_tela()
            print(f"✅ Depósito realizado com sucesso: R$ {valor_deposito:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
             
    # Estrutura que centraliza os saques.         
    elif opcao == "s":
        # Entrada dos saques que somente aceita int e float, com ponto ou vírgula.
        try:
            valor_saque = float(input("Digite o valor do saque: ").strip().replace(",", "."))

        except ValueError:
            limpar_tela()
            print("❌ Operação de saque falhou! Valor inválido.")
            continue

        # Variáveis de teste.    
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Testa de valor de saque é menor ou igual a zero.
        if valor_saque <= 0:
            limpar_tela()
            print("❌ Operação de saque falhou! O valor informado é inválido.")
        
        #  Testa se existe saldo suficiente.
        elif excedeu_saldo:
            limpar_tela()
            print("❌ Operação de saque falhou! Você não tem saldo suficiente.")
        
        #  Testa se o valor do saque excede o limite de R$ 500,00.
        elif excedeu_limite:
            limpar_tela()
            print("❌ Operação de saque falhou! O valor do saque excede o limite.")
        
        # Testa se o número de saque foi excedido.
        elif excedeu_saques:
            limpar_tela()
            print("❌ Operação de saque falhou! Número máximo de saques excedido.")
        
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:,.2f}\n".replace(",", "X").replace(".", ",").replace("X", ".")
            limpar_tela()
            print(f"✅ Saque realizado com sucesso: R$ {valor_saque:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Estrutura que centraliza o extrato. 
    elif opcao == "e":
        limpar_tela()
        print("\n" + " EXTRATO ".center(42, "="))

        if not extrato:
            print("⚠️  Não foram realizadas movimentações.\n")

        else:
            print(extrato)

        print(f"Saldo: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("=" * 42)

    # Estrutura para sair do sistema. 
    elif opcao == "q":
        print("\nObrigado. Até a próxima!\n")
        break

    else:
        limpar_tela()
        print("❌ Operação inválida, selecione novamente a operação desejada.")