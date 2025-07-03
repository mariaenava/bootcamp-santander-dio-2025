# BOOTCAMP Santander & DIO 2025 | Back-End Python

## Operadores e Manipulação de String com Python

### --> Desafio de Projeto | [Sistema Bancário com Python](00%20-%20Fundamentos/sistema_bancario.py)

**OBJETIVO**: Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

**DESAFIO**: Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

**OPERAÇÃO DE DEPÓSITO**: Deve ser possível depositar valores positivos para  aminha conta bancária. A V1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

**OPERAÇÃO DE SAQUE**: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**OPERAÇÃO DE EXTRATO**: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$1500.45


### --> Desafio de Código | [Cálculo de Desconto em Loja](00%20-%20Fundamentos/calculo_desconto.py)

**DESCRIÇÃO**: Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes. Regras de desconto: "DESCONTO10": 10% de desconto; "DESCONTO20": 20% de desconto; "SEM_DESCONTO": Sem desconto.

**ENTRADA**: Preço original do produto; Código do cupom digitado.

**SAÍDA**: Preço final após aplicar o desconto. Com duas casas decimais.

### --> Desafio de Código | [Validador de Formato de E-mails](00%20-%20Fundamentos/validador_email.py)

**DESCRIÇÃO**: Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras: Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com; Não pode começar ou terminar com "@"; Não pode conter espaços.

**ENTRADA**: Uma string contendo o e-mail a ser validado.

**SAÍDA**: "E-mail válido" se o e-mail estiver no formato correto; "E-mail inválido" caso contrário.
