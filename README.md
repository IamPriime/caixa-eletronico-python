# Caixa eletrônico em Python

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IamPriime/caixa-eletronico-python/blob/main/caixa_eletronico.ipynb)

Simulação didática de consulta de saldo, depósito e saque com funções Python.

Projeto de estudo de **Gabriel / [IamPriime](https://github.com/IamPriime)**, desenvolvido a partir de um notebook do Google Colab e organizado para portfólio. O foco é mostrar a lógica implementada e permitir que outra pessoa execute o projeto.

## O que o projeto faz

- Consulta o saldo informado.
- Simula depósito e saque.
- Recusa saldo negativo, valores não positivos e saque acima do saldo.

## Tecnologias e conceitos

Python 3.10+ · funções · controle de fluxo · validação de entradas.

## Como executar

```bash
git clone https://github.com/IamPriime/caixa-eletronico-python.git
cd caixa-eletronico-python
python -m venv .venv
```

Ative o ambiente: no Windows PowerShell, `.venv\Scripts\Activate.ps1`; no macOS/Linux, `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python caixa_eletronico.py
```

No Colab, use o botão no início deste README. Execute a célula e responda às entradas interativas.

## Exemplo e interpretação

Exemplo: saldo inicial `100`, opção `2` e depósito `50` produzem saldo de R$ 150,00. Um saque de `200` é recusado. Valores monetários usam `Decimal`. O saldo existe apenas durante a execução.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `caixa_eletronico.ipynb` | Notebook para Colab/Jupyter, sem saídas antigas |
| `caixa_eletronico.py` | Versão executável localmente |
| `requirements.txt` | Indicação de que não há dependências externas |


## Origem e melhorias

Origem no Colab: `Atividade-Caixa-Eletronico-simples.ipynb`. O arquivo no Drive foi preservado. Adicionados menu contínuo, atualização de saldo, cálculo com Decimal e validação de valores. As saídas de execução e os metadados pessoais do notebook foram removidos da versão publicada.

## Limitações

Projeto educacional executado no terminal. Não inclui banco de dados, interface web ou persistência. Não realiza operações bancárias reais.

## Próximos passos

- Adicionar persistência e ampliar a cobertura de cenários de entrada.
- Separar a interface de terminal da lógica para facilitar futuras interfaces.

## Autoria e uso

Organização de estudos de [IamPriime](https://github.com/IamPriime). Nenhuma licença de software foi escolhida para este repositório.
