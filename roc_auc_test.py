import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
average_precision_score(y_true, y_scores)
y_true = np.array([0, 0, 1, 1, 2, 2])
y_scores = np.array([
    [0.7, 0.2, 0.05,0.05],
    [0.4, 0.3, 0.15,0.15],
    [0.1, 0.8, 0.05,0.05],
    [0.2, 0.3, 0.25,0.25],
    [0.4, 0.4, 0.1,0.1],
    [0.1, 0.2, 0.35,0.35],
])
print(average_precision_score(y_true, y_scores))

print(roc_auc_score(y_true, y_scores,average=None,multi_class="ovr"))

