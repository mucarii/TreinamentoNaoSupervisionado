# %%
# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# %%
# Gerando dados de exemplo
x, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.60, random_state=0)

# %%
# Visualizando os dados gerados
plt.scatter(x[:, 0], x[:, 1], s=50)

# %%
# Aplicando KMeans
kmeans = KMeans(n_clusters=4)
y_kmeans = kmeans.fit_predict(x)

# %%
# Visualizando os clusters
plt.scatter(x[:, 0], x[:, 1], s=50, c=y_kmeans)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="red", s=200, alpha=0.5)

plt.title("KMeans Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
