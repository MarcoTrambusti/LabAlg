import numpy as np
from RandomGraph import adjacency_matrix
# generazione di grafi pesati casuali
def random_weighted_graph(w, n, p):
    a = adjacency_matrix(n, p)
    weight = np.random.randint(1, w, (n, n))
    a *= weight
    return a