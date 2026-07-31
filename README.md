# 📊 Dashboard de gastos
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Uso](https://img.shields.io/badge/uso-educacional-blue)

## 📃Descrição
O projeto consiste em uma leitura de despesas de um arquivo csv do excel pelo pandas. Para que apartir dele possa ler, organizar e analisar de forma rápida e eficaz.

## 📌 Índice
- Sobre o projeto;
- Funcionalidades;
- Tecnologias usadas;
- Estrutura de pastas;
- Como rodar;
- Rodando os testes;
- Autor.

## 🖋 Sobre o projeto
Este projeto nasceu como treinamento de conhecimentos adiqueridos ao estudar as ferramentas usadas no mesmo. Objetivo de organizar despesas pessoais de forma simples, sem depender de planilhas complexas. Ele lê um arquivo CSV com lançamentos financeiros e gera relatórios agrupados por categoria e por mês, com testes automatizados garantindo a confiabilidade dos cálculos.

## Funcionalidades:
- Ler dados de despesas a partir de um arquivo CSV;
- Tratar e limpar os dados (remover colunas vazias, converter datas);
- Calcular o total de gastos por categoria;
- Calcular o total de gastos por mês;
- Validar os cálculos com testes automatizados (unittest).

## Tecnologias Usadas
python, pandas, unnittest, venv e openpyxl.

## Estrutura
```
dashboard-gastos/
│
├── source/
    ├── _pycache_
    ├──venv.
│   ├── dashboard.py
│   ├── data/
│   │   └── gastos.csv
│   └── tests/
│       └── test_dashboard.py
│
├── _init_.py
├─ pyprojejct.toml
├── README.md
└── requirements.txt
```

## Como rodar o código
1. Ativamento do ambiente virtual:
  - **Windows powershell**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
  - **Windows (Prompt de Comando / cmd)**
    ```cmd
    .venv\Scripts\activate.bat
    ```
  - **Linux / Mac (bash ou zsh)**
    ```bash
    source .venv/bin/activate
    ```
2. Instalação de dependências:
  ```
  pip install -r requirements.txt
  ```
3. Rodar o script principal
  - Abre o terminal e entre na pasta certa:
     ```
     cd .\source
      ```
  - Depois rode esse comando para fazer o código funcionar:
  ```
  python dashboard.py
  ```

## Rodando os testes
1. Abre o terminal e entre na pasta correta:
  ```
  cd .\source\tests
  ```
2. Depois, apenas rode este comando:
  ```
  python test_dashboard.py
  ```
resultado esperado:
<img width="973" height="132" alt="Captura de tela 2026-07-31 181256" src="https://github.com/user-attachments/assets/abfa3110-ab86-44da-8f84-07eecef326e5" />



  ## Autor
  Nicolle Rocha - Estudante de Ciência da computação
