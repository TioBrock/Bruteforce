# Quebra de Senha com Bruteforce (Python)

Este programa tenta descobrir uma senha fornecida pelo usuário usando um ataque de bruteforce, testando **todas as combinações possíveis** dos caracteres escolhidos para a mesma quantidade de caracteres da senha.

---

## Como usar

1. Executar o programa Python.
2. Digite uma senha que você quer testar.
3. O programa vai tentar todas as combinações e encontrar a senha.
4. No final, ele mostra quantas tentativas foram feitas e quanto tempo levou.

---

## Avisos importantes

* **O programa é didático e funciona bem APENAS para senhas curtas** (4, 5 caracteres, no máximo). Senhas maiores podem levar um
  andamento **muito** longo (horas, dias, semanas, até mais).
* Não use este programa para **tentar invadir contas ou sistemas alheios**.
* É só para aprendizado e testes.
* O bruteforce cresce exponencialmente com o tamanho da senha, então **não espere milagres** com senhas grandes (funciona melhor com senhas curtas).
* O programa roda só no terminal e precisa do Python instalado.

---

## Como melhorar

* Usar uma biblioteca de multiprocessamento para rodar em paralelo e aproveitar melhor seu computador.
* Tentar senhas de tamanhos diferentes (atualmente ele só tenta do tamanho da senha).
* Melhorar a lista de caracteres para cobrir mais casos ou diminuir para acelerar.
* Usar outras técnicas de ataque (dicionários, padrões, pegar senhas vazadas de uma API, etc).
* Colocar uma interface gráfica para melhor interação.

---

O objetivo deste programa é puramente educativo e demonstra uma vulnerabilidade de alguns tipos de senha na prática.
Deixei algumas ideias de como ele pode ser melhorado para se tornar mais eficiente.
Sinta-se à vontade para usar meu código de base para melhorias e para seu aprendizado.
