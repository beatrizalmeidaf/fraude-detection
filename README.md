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

---

## **Estrutura do Projeto**

### **I. Compreensão dos Dados**
- **Gather Sense of our data:** Investigação inicial para entender as características principais e a distribuição dos dados.

### **II. Pré-Processamento**
- **Scaling and Distributing:** Normalização e distribuição dos dados para garantir maior eficácia nos modelos.
- **Splitting the Data:** Divisão em conjuntos de treino, validação e teste.

### **III. Tratamento de Dados Desbalanceados**
- **Distributing and Correlating:** Investigação da correlação entre variáveis e a distribuição das classes.
- **Anomaly Detection:** Identificação de padrões fraudulentos.
- **Dimensionality Reduction and Clustering:** Redução de dimensionalidade (t-SNE) para melhor visualização e clusterização.
- **Classifiers:** Teste de diferentes classificadores para maximizar a performance.
- **A Deeper Look into Logistic Regression:** Análise detalhada do modelo de regressão logística.
- **Oversampling with SMOTE:** Aumentação de dados minoritários utilizando SMOTE.

### **IV. Testes e Avaliação**
- **Testing with Logistic Regression:** Avaliação do modelo de regressão logística.
- **Neural Networks Testing:** Comparativo entre redes neurais aplicadas a dados com undersampling e oversampling.




