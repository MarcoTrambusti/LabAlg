import numpy as np
# generazione di grafi casuali con un numero di nodi a scelta ed una determinata probabilità di presenza di archi tra vertici
def adjacency_matrix(n, p):
    adjacency_matrix = np.random.binomial(1, p, (n, n))  # binomial(n,p,dimensione) mettendo n=1 ho una distribuzione di bernoulli ovvero 1*p
    return adjacency_matrix
