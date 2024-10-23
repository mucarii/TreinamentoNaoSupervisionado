# KMeans Clustering Example

Este repositório contém um exemplo simples de aplicação do algoritmo de KMeans para agrupamento de dados gerados artificialmente. O código utiliza bibliotecas populares de Python, como `matplotlib` e `sklearn`, para gerar, visualizar e agrupar os dados.

## Descrição do Código

O script realiza os seguintes passos:

1. **Importação de Bibliotecas**: As bibliotecas `matplotlib` (para visualização) e `sklearn` (para manipulação de dados e aplicação do KMeans) são importadas.

2. **Geração de Dados de Exemplo**: Utilizamos a função `make_blobs` do `sklearn` para gerar um conjunto de dados com 500 amostras, distribuídas em 4 centros (clusters) com um desvio padrão de 0.60.

3. **Visualização dos Dados Gerados**: Os dados gerados são visualizados em um gráfico de dispersão, onde cada ponto representa uma amostra.

4. **Aplicação do Algoritmo KMeans**: O algoritmo KMeans é aplicado aos dados, buscando dividir as amostras em 4 clusters.

5. **Visualização dos Clusters**: Os clusters resultantes são plotados com cores diferentes, e os centros dos clusters são destacados em vermelho.

## Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install matplotlib scikit-learn
   ```

2. Execute o script:
   ```bash
   python K_means.py
   ```

## Bibliotecas Utilizadas
 - matplotlib: Para visualização dos dados e dos clusters.
 - scikit-learn: Para gerar dados e aplicar o algoritmo KMeans.
  