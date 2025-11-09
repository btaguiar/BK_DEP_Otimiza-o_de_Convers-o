# 🏦 BK-DEP — Otimização de Conversão em Campanha Bancária  

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](https://jupyter.org/)
[![SQL](https://img.shields.io/badge/Database-MySQL-blue)](https://www.mysql.com/)
[![Visualization](https://img.shields.io/badge/Visualization-Seaborn%20%7C%20Plotly-green)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Autor:** Bruno Aguiar  
> **Área de foco:** Marketing Analytics • Data Storytelling • Business Intelligence  
> 📊 **Objetivo:** Maximizar o ROI e otimizar a taxa de conversão de campanhas de depósito a prazo por meio de análise exploratória e segmentação baseada em dados.

---

## 📘 Sumário

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Objetivos e Perguntas de Negócio](#objetivos-e-perguntas-de-negócio)
3. [Arquitetura do Projeto](#arquitetura-do-projeto)
4. [Fases de Desenvolvimento](#fases-de-desenvolvimento)
5. [Principais Resultados](#principais-resultados)
6. [Ferramentas Utilizadas](#ferramentas-utilizadas)
7. [Como Reproduzir](#como-reproduzir)
8. [Autor e Contato](#autor-e-contato)
9. [Licença](#licença)

---

## 🧠 Sobre o Projeto

O projeto **BK-DEP – Otimização de Conversão em Campanha Bancária** analisa os resultados de campanhas de **depósito a prazo** conduzidas por um banco fictício, com o objetivo de **maximizar o Retorno sobre o Investimento (ROI)** e **reduzir o Custo por Aquisição (CPA)**.

O estudo combina **análise exploratória (EDA)** e **modelagem preditiva** para identificar os perfis de clientes mais propensos à conversão e construir estratégias de alocação de recursos *data-driven*.

---

## 🎯 Objetivos e Perguntas de Negócio

**Objetivo central:**  
> Maximizar o ROI e a taxa de conversão por meio da análise de segmentos de clientes e do desempenho das campanhas.

**Perguntas respondidas:**
- Quais perfis (profissão, estado civil, educação) têm maior propensão à conversão?  
- Existe uma relação entre o investimento (CPA) e o retorno (ROI)?  
- Como redistribuir o orçamento de forma mais eficiente?  
- Quais segmentos entregam o melhor equilíbrio entre custo e retorno?

---

## 🏗️ Arquitetura do Projeto
BKDEP/
│
├── data/
│ ├── raw/ # Dados originais (ex: bank_marketing.csv)
│ ├── processed/ # Dados tratados e limpos (dados_banco_clean.csv, ROI)
│ └── outputs/ # Dados finais integrados (dados_banco_merged.csv)
│
├── notebooks/
│ ├── 01_diagnostico_inicial.ipynb # Diagnóstico e limpeza de dados
│ ├── 02_analise_exploratoria.ipynb # Análises de ROI, CPA e taxa de conversão
│ └── 03_modelagem.ipynb # Futuras modelagens (clusterização, predição)
│
├── scripts/
│ ├── utils.py # Funções auxiliares
│ ├── pre_processamento.py # Funções de ETL
│ └── analise_roi.py # Cálculos de ROI, CPA e taxa de conversão
│
├── assets/ # Gráficos, prints e visuais do projeto
├── docs/ # Roadmap e documentação
├── README.md # Documentação principal do projeto
├── requirements.txt # Dependências Python
└── .gitignore # Arquivos ignorados pelo Git

---

## 🧮 Fontes e Bases de Dados

| Base | Descrição | Origem |
|------|------------|--------|
| `bank_marketing` | Dados de campanhas de marketing de depósito a prazo | UCI Repository / Kaggle |
| `tabela_roi_final_otimizada.csv` | Resultado consolidado de ROI e CPA por segmento | SQL Aggregation |
| `dados_banco_clean.csv` | Dados tratados, sem valores faltantes | MySQL → Pandas |
| `dados_banco_merged.csv` | Base integrada final (ROI + perfil de cliente) | Python Merge |

---

## 🔍 Principais Etapas e Entregas

### **Fase 1 — Planejamento e Definição de Métricas**
- ROI = (Receita - Custo) / Custo  
- CPA = Custo / Conversões  
- Taxa de Conversão = Conversões / Total de Contatos

✅ Concluída: Objetivos, métricas e KPIs definidos.

---

### **Fase 2 — Limpeza e Diagnóstico Inicial**
- Tratamento de valores `unknown`
- Normalização de categorias (`nao_informado`)
- Exportação `dados_banco_clean.csv`

✅ Concluída: Base limpa e exportada via MySQL/Pandas.

---

### **Fase 3 — Análise Exploratória (EDA)**
- Correlação entre variáveis: idade, saldo, duração, contatos.  
- Boxplots: distribuição de ROI por profissão e educação.  
- Heatmap: relação entre ROI, CPA e taxa de conversão.  
- Identificação de **segmentos de alto valor (Top 10)**.

✅ Concluída: Tendências de conversão e ROI identificadas.

---

### **Fase 4 — Integração e Segmentação de ROI**
- Junção SQL + Python (`tabela_roi_final_otimizada.csv` + `dados_banco_clean.csv`)
- Verificação de integridade e ausência de duplicatas.
- Exportação final: `dados_banco_merged.csv`

✅ Concluída: Base única pronta para análise e modelagem.

---

### **Fase 5 — Modelagem e Insights Prescritivos (futuro)**
- K-Means: clusterização de perfis de cliente.
- Regressão logística: probabilidade de conversão.
- Simulações de ROI com diferentes alocações de verba.

🚧 Em desenvolvimento.

---

## 📈 Principais Insights (versão atual)

- **Melhores segmentos de conversão:**  
  - `student + secondary` (30.13%)  
  - `retired + tertiary` (29.29%)  
  - `management + unknown` (21.46%)  

- **Taxa média global:** ~11.27%  
- **Relação entre duração da chamada e conversão:**  
  - Campanhas mais longas têm ROI decrescente após ~250 segundos.  
- **Clientes aposentados e estudantes** são os perfis mais propensos a aderir.  

---

## 🧰 Stack Tecnológica

| Ferramenta | Aplicação |
|-------------|------------|
| **Python (Pandas, Numpy, Seaborn, Plotly)** | Limpeza e análise exploratória |
| **SQL (MySQL)** | Extração e agregação de dados |
| **Power BI / Looker Studio** | Dashboards de performance |
| **Google Colab** | Desenvolvimento e execução |
| **Git + GitHub (SSH)** | Versionamento e publicação |

---

## 📊 Visualizações

- Boxplot ROI × Profissão × Educação  
- Gráfico de dispersão ROI × CPA × Volume  
- Heatmap de Correlação  
- Top 10 segmentos de ROI  

📷 Gráficos disponíveis em [`assets/`](assets/)

---

## 🚀 Próximos Passos

- Implementar `02_analise_exploratoria.ipynb` (com Plotly e correlação ROI × CPA).  
- Adicionar clusterização de segmentos (K-Means).  
- Criar dashboard interativo Power BI / Looker Studio.  
- Publicar artigo com resultados e storytelling no LinkedIn.

---

## 🧑‍💻 Como Reproduzir

1️⃣ Clone o repositório:
```bash
git clone git@github.com:btaguiar/BK_DEP_Otimiza-o_de_Convers-o.git
cd BK_DEP_Otimiza-o_de_Convers-o
pip install -r requirements.txt
jupyter notebook notebooks/01_diagnostico_inicial.ipynb





