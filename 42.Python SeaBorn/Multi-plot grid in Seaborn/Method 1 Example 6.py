g = sns.PairGrid(exercise)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
