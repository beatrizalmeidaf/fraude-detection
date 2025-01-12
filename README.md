# Detecção de Fraudes em Cartões de Crédito

Este projeto tem como objetivo a criação de um pipeline para detectar fraudes em transações de cartão de crédito, utilizando técnicas de aprendizado de máquina, análise de dados e tratamento de dados desbalanceados.


## **Visão Geral**

### **Base de Dados**
Este projeto utiliza a base de dados disponível no Kaggle:
[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data).

Esta base contém transações realizadas com cartões de crédito em setembro de 2013, em um conjunto altamente desbalanceado (99,8% de transações normais contra 0,2% de fraudulentas).

### **Referências e Guias**
- Notebook de referência: [Credit Fraud - Dealing with Imbalanced Datasets](https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets).
- Conteúdo do curso de Ciência de Dados da [Hashtag Programação](https://www.hashtagprogramacao.com).

### **Conceitos Abordados**
O projeto foca nos seguintes tópicos principais:
- Extração, Transformação e Carga (ETL);
- Análise Exploratória de Dados (EDA);
- Técnicas de aprendizado de máquina;
- Tratamento de dados desbalanceados (Oversampling, Undersampling, SMOTE);
- Métricas de avaliação de modelos.


## **Estrutura do Projeto**

### **1. Compreensão dos Dados**
- Investigação inicial para entender as características e a distribuição do conjunto de dados.

### **2. Pré-Processamento**
- Normalização e ajuste dos dados para maior eficácia dos modelos;
- Divisão dos dados em conjuntos de treino, validação e teste.

### **3. Tratamento de Dados Desbalanceados**
- Análise da distribuição das classes e correlação entre variáveis;
- Identificação de padrões fraudulentos;
- Redução de dimensionalidade (t-SNE) e clusterização para melhor visualização;
- Avaliação de diferentes classificadores;
- Aplicação de técnicas de oversampling com SMOTE.

### **4. Testes e Avaliação**
- Teste e análise detalhada de modelos, como regressão logística e redes neurais;
- Comparação do desempenho com diferentes estratégias de balanceamento dos dados.

