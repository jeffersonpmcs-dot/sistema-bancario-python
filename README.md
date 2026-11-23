# Sistema Bancário em Python

Atividade de programação orientada a objetos que simula operações bancárias pelo terminal. Cada conta é um objeto da classe `ContaBancaria`, com titular, número e saldo encapsulados.

| Conta | Titular | Número | Saldo inicial |
| --- | --- | --- | --- |
| 1 | João | 101 | R$ 1.000,00 |
| 2 | Maria | 102 | R$ 500,00 |

## Como executar

Com o Python 3, abra `main.py` no PyCharm e selecione **Run 'main'**, ou abra um terminal na pasta do projeto e execute o comando abaixo.

```bash
python main.py
```

O menu permite consultar saldos, depositar, sacar e transferir dinheiro nos dois sentidos. A opção **9** encerra o programa. Digite valores em reais com ponto ou vírgula decimal, como `50`, `50.25` ou `50,25`, sem separador de milhar. Internamente, os saldos são armazenados em centavos inteiros para que as operações sejam exatas. Os saldos são reiniciados a cada execução.

Para reproduzir o exemplo da atividade, escolha **7** e informe `200`. João ficará com **R\$ 800,00** e Maria com **R\$ 700,00**.

## Desafio conceitual

**a) Qual é a diferença entre uma classe e um objeto?**

A classe define a estrutura e os comportamentos comuns. Um objeto é uma instância dessa classe, com seus próprios dados. `ContaBancaria` é a classe, e as contas de João e Maria são dois objetos criados a partir dela.

**b) Qual é a finalidade dos atributos e dos métodos?**

Os atributos guardam os dados da conta, como titular, número e saldo. Os métodos definem o que ela pode fazer, como consultar o saldo ou realizar um depósito.

**c) Qual é a função de `__init__()`?**

O Python chama `__init__()` ao instanciar a classe para inicializar o novo objeto. Neste programa, ele recebe o titular, o número e o saldo inicial e atribui esses valores à conta.

**d) Por que os atributos usam o prefixo `__`?**

O Python modifica internamente os nomes dos atributos com esse prefixo. Isso dificulta o acesso direto acidental e indica que os atributos fazem parte da implementação da classe. Essa convenção orienta o uso da classe, e o Python ainda permite acesso intencional ao nome modificado.

**e) Por que depósito, saque e transferência são métodos da classe?**

Essas operações alteram o estado de uma conta e precisam obedecer às regras do saldo. Como métodos de `ContaBancaria`, ficam no mesmo lugar que os dados e podem aplicar as mesmas regras em qualquer instância.

**f) Como o encapsulamento ajuda a impedir alterações indevidas no saldo?**

O saldo é mantido em `__saldo`, e a interface do programa muda esse valor pelos métodos da conta. Esses métodos verificam se o valor é positivo e se há saldo suficiente quando a operação exige um débito. Um saque recusado, por exemplo, preserva o saldo anterior.

**g) Por que a transferência recebe outro objeto `ContaBancaria`?**

O objeto recebido representa a conta que deve ser creditada. Assim, o método consegue debitar a conta de origem (`self`) e atualizar o saldo da conta de destino na mesma operação.

**h) Qual é a diferença entre atributos de classe e de instância?**

Um atributo de classe é definido no corpo da classe e pode ser compartilhado pelas instâncias. Um atributo de instância pertence a um objeto específico. Nesta atividade, `__titular`, `__numero_conta` e `__saldo` são atributos de instância inicializados por `__init__()`.

**i) Quais são as vantagens da orientação a objetos neste sistema?**

Cada conta guarda seu próprio estado e reutiliza a mesma implementação das operações. Isso facilita criar novas contas, localizar as regras de movimentação e corrigir um comportamento em um único lugar, sem precisar manter variáveis e funções separadas para cada conta.
