"""Simulação de duas contas bancárias pelo terminal."""

import re


def converter_para_centavos(valor):
    """Aceita ponto ou vírgula decimal e preserva o valor exato em centavos."""
    texto = str(valor).strip().replace(",", ".")
    if not re.fullmatch(r"[+-]?[0-9]+(?:\.[0-9]{1,2})?", texto):
        return None

    reais, _, centavos = texto.partition(".")
    try:
        return int(reais + centavos.ljust(2, "0"))
    except ValueError:
        return None


def formatar_reais(saldo_em_centavos):
    reais, centavos = divmod(saldo_em_centavos, 100)
    reais_formatados = f"{reais:,}".replace(",", ".")
    return f"R$ {reais_formatados},{centavos:02d}"


class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo_inicial):
        saldo = converter_para_centavos(saldo_inicial)
        if saldo is None or saldo < 0:
            raise ValueError("O saldo inicial deve ser um valor monetário não negativo.")

        self.__titular = titular
        self.__numero_conta = numero_conta
        self.__saldo = saldo

    def consultar_saldo(self):
        print(f"Conta {self.__numero_conta} — {self.__titular}")
        print(f"Saldo disponível: {formatar_reais(self.__saldo)}")

    def depositar(self, valor):
        centavos = converter_para_centavos(valor)
        if centavos is None or centavos <= 0:
            return False

        self.__saldo += centavos
        return True

    def sacar(self, valor):
        centavos = converter_para_centavos(valor)
        if centavos is None or centavos <= 0 or centavos > self.__saldo:
            return False

        self.__saldo -= centavos
        return True

    def transferir(self, conta_destino, valor):
        if not isinstance(conta_destino, ContaBancaria) or conta_destino is self:
            return False

        centavos = converter_para_centavos(valor)
        if centavos is None or centavos <= 0 or centavos > self.__saldo:
            return False

        self.__saldo -= centavos
        conta_destino.__saldo += centavos
        return True


MENU = """
========== SISTEMA BANCÁRIO ==========
1 - Consultar saldo da Conta 1
2 - Consultar saldo da Conta 2
3 - Depositar na Conta 1
4 - Depositar na Conta 2
5 - Sacar da Conta 1
6 - Sacar da Conta 2
7 - Transferir da Conta 1 para Conta 2
8 - Transferir da Conta 2 para Conta 1
9 - Encerrar programa
"""


def executar_menu():
    conta_joao = ContaBancaria("João", 101, 1000)
    conta_maria = ContaBancaria("Maria", 102, 500)

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "9":
            print("Programa encerrado.")
            return

        if opcao not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("Opção inválida. Escolha um número de 1 a 9.")
            continue

        conta = conta_joao if opcao in ("1", "3", "5", "7") else conta_maria
        if opcao in ("1", "2"):
            conta.consultar_saldo()
            continue

        valor = input("Informe o valor em reais (ex.: 50,00): ")
        centavos = converter_para_centavos(valor)
        if centavos is None or centavos <= 0:
            print("Valor inválido. Informe um valor positivo com até duas casas decimais.")
            continue

        if opcao in ("3", "4"):
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
                conta.consultar_saldo()
        elif opcao in ("5", "6"):
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
                conta.consultar_saldo()
            else:
                print("Saldo insuficiente para o saque.")
        else:
            destino = conta_maria if opcao == "7" else conta_joao
            if conta.transferir(destino, valor):
                print("Transferência realizada com sucesso!")
                conta.consultar_saldo()
                destino.consultar_saldo()
            else:
                print("Saldo insuficiente para a transferência.")


if __name__ == "__main__":
    executar_menu()
