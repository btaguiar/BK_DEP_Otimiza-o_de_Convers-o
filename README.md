# 🏦 BK-DEP — Otimização de Conversão em Campanha Bancária

**Autor:** Bruno Aguiar  
**Área de foco:** Marketing Analytics • Data Storytelling • Business Intelligence  
**Última atualização:** Novembro de 2025

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Andamento-yellow" alt="Status do Projeto"/>
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="Licença"/>
</p>

## 📊 Objetivo do Projeto

Maximizar o **ROI** e otimizar a **taxa de conversão** de campanhas de depósito a prazo (Bank Marketing) por meio de análise exploratória avançada, segmentação de clientes e estratégias data-driven.

Baseado no famoso dataset [Bank Marketing UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing), este projeto simula um caso real de otimização de campanhas bancárias.

---

## 🎯 Perguntas de Negócio Respondidas

- Quais perfis de clientes (profissão, educação, estado civil) têm maior propensão à conversão?
- Existe relação entre investimento (CPA) e retorno (ROI)?
- Como redistribuir o orçamento de marketing de forma mais eficiente?
- Quais segmentos entregam o melhor equilíbrio entre custo e conversão?

---

## 🏗️ Estrutura do Projeto

BK-DEP/
├── data/
│   ├── raw/               # Dados originais (bank_marketing.csv)
│   ├── processed/         # Dados limpos e tratados
│   └── outputs/           # Datasets finais (ex: dados_banco_merged.csv)
├── notebooks/
│   ├── 01_diagnostico_inicial.ipynb      # Limpeza + EDA inicial ✅
│   ├── 02_analise_exploratoria.ipynb     # Segmentação + ROI/CPA ✅
│   └── 03_modelagem.ipynb                # Modelos preditivos (em construção)
├── scripts/
│   ├── utils.py
│   ├── pre_processamento.py
│   └── analise_roi.py
├── assets/
│   └── etapa02_exploratoria/   # Todos os gráficos exportados
├── docs/
│   └── roadmap.md
├── requirements.txt
├── LICENSE
└── README.md
---

## Fases do Projeto

| Fase                        | Status            | Descrição                                           |
|-----------------------------|-------------------|-----------------------------------------------------|
| 1. Diagnóstico e Limpeza    | Concluída      | Tratamento, feature engineering e KPIs iniciais     |
| 2. Análise Exploratória     | Concluída      | Segmentações detalhadas, cálculo de ROI/CPA         |
| 3. Modelagem Preditiva      | Em construção  | Regressão logística, árvores e clusterização       |
| 4. Dashboard & Storytelling | Planejado      | Power BI / Looker Studio + recomendações finais     |

---

## Principais Insights (Atualizados — Nov/2025)

- **Perfis com maior conversão**: aposentados, estudantes, técnicos e administrativos  
- **Melhor canal de contato**: `cellular` supera significativamente o `telephone`  
- **Menos é mais**: campanhas com ≤ 3 contatos apresentam CPA muito menor  
- **Sweet spot de ROI**: renda média + nível superior de educação  
- **Top 3 profissões por ROI**: `retired` → `student` → `management`

> **Recomendação prática**: concentrar 70-80% do orçamento nos segmentos de aposentados e estudantes com abordagem via celular e no máximo 3 contatos.

---

## Assets da Análise Exploratória

Pasta completa → [`assets/etapa02_exploratoria/`](assets/etapa02_exploratoria/)

| # | Descrição                                   | Visualização                                                                                   |
|---|---------------------------------------------|------------------------------------------------------------------------------------------------|
| 1 | Scatterplot — ROI vs CPA (interativo)       | ![Scatter ROI vs CPA](assets/etapa02_exploratoria/scatter_roi_cpa.png)                         |
| 2 | Boxplot — ROI por Profissão                 | ![Boxplot ROI por Profissão](assets/etapa02_exploratoria/boxplot_roi_profissao.png)            |
| 3 | Top 10 Segmentos com Maior ROI              | ![Top 10 ROI](assets/etapa02_exploratoria/top10_segmentos_roi.png)                             |
| 4 | Heatmap — Correlação Entre Variáveis        | ![Heatmap](assets/etapa02_exploratoria/heatmap_correlacao.png)                                 |
| 5 | Distribuição Geral — ROI e CPA              | ![Distribuição ROI/CPA](assets/etapa02_exploratoria/distribuicao_geral_roi_cpa.png)            |
| 6 | Resumo Visual de Insights                   | ![Resumo Insights](assets/etapa02_exploratoria/insights_resumo.png)                            |

### Scatterplot ROI vs CPA (zoom recomendado)
![Scatter ROI vs CPA — detalhe](assets/etapa02_exploratoria/scatter_roi_cpa.png)

---

## Tecnologias Utilizadas

| Categoria       | Ferramentas                              |
|-----------------|------------------------------------------|
| Linguagem       | Python 3.10                              |
| Manipulação     | Pandas, NumPy                            |
| Visualização    | Matplotlib, Seaborn, Plotly              |
| Modelagem       | Scikit-learn (em desenvolvimento)        |
| Ambiente        | Jupyter Notebook                         |
| Documentação    | Markdown                                 |

## Autor e Contato
Bruno Aguiar
Marketing Analytics & Data Intelligence
LinkedIn •
GitHub •

