# Força Bruta Quebra de Senha (Python)

Este programa tenta descobrir uma senhora fornecida pelo usuário usando uma força bruta ataque, testando **todas as combinações possíveis** dos caracteres escolhidos para uma mesma quantidade de caracteres da senha.

---

## Como usar

1. Executar o programa Python.
2. Digite uma senhora que você quer testar.
3. O programa vai tentar todas as combinações é contrar um senador.
4. Sem final, ele mostra quantas tentativas foram feitas e quanto tempo levou.

---

## Avisos importantes

* **O programa é didático e funciona bem como APENAS para senhas curvas** (4, 5 caracteres, sem máximo). Senhas maiores poder levar um 
andamento **muito** longo (horas, dias, semanas, até mais).
* Não use este programa para **tentar invadir contas ou sistemas alheios**
* É só para aprendido e testículos.
* O força bruta cresce exponencialmente com o tamanho da senha, então **não espere milagres** com senhas grandes (função melhor com senhas curvas).
* O programa roda só no terminal e precisa do Python instalado.

---

## Como melhorar

* Usar uma biblioteca multiprocessamento para rodar em paralelo e aproveitar melhor seu computador.
* Tentar senhas de tamanhos diferentes (atualmente ele só tenta do tamanho da senha).
* Melhor uma lista de caracteres para cobrir mais casos ou diminuir para acelerar.
* Usar outras técnicas de ataque (dicionários, padrões, pegar senhas vazadas de uma API, etc).
* Interface colocar alguma gráfica para melhor interação.

---

O objetivo destina programa é puramento aprendido e demonstra uma vulnerabilidade de alguns tipos de senha na prática.
Deixei algumas ideias de como ele pode ser melhado para se tornar mais eficiente.
Sinta-se a voz para usar meu código de base para melodias e para seu aprendido.
