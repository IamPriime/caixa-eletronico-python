from decimal import Decimal, InvalidOperation


def ler_valor(mensagem, permitir_zero=False):
    while True:
        try:
            valor = Decimal(input(mensagem).replace(",", "."))
            if not valor.is_finite() or valor < 0 or (valor == 0 and not permitir_zero):
                raise ValueError
            if valor != valor.quantize(Decimal("0.01")):
                raise ValueError
            return valor
        except (InvalidOperation, ValueError):
            print("Informe um valor válido com até duas casas decimais.")


def depositar(saldo, valor):
    if valor <= 0:
        raise ValueError("O depósito deve ser positivo.")
    return saldo + valor


def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O saque deve ser positivo.")
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor


def main():
    print("Bem-vindo ao GEN-CAIXA")
    saldo = ler_valor("Saldo inicial: ", permitir_zero=True)
    while True:
        print("\n1 - Ver saldo\n2 - Depositar\n3 - Sacar\n0 - Sair")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        try:
            if escolha == "2":
                saldo = depositar(saldo, ler_valor("Valor do depósito: "))
            elif escolha == "3":
                saldo = sacar(saldo, ler_valor("Valor do saque: "))
            elif escolha != "1":
                print("Opção inválida.")
                continue
            print(f"Saldo: R$ {saldo:.2f}")
        except ValueError as erro:
            print(erro)


if __name__ == "__main__":
    main()
