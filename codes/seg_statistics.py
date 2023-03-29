'''
\begin{table}[h]
\caption{\label{tab1}Summary of OCTA-500 dataset.}
\centering
\begin{tabular}{|p{1.2cm}|p{1.5cm}|p{1.6cm}|p{1.8cm}|}
\hline
Field of View & Resolution & Number of Samples & Disease Types \\
\hline
3M & 304 * 304 & 200 & AMD, CNV, DR \\
\hline
6M & 400 * 400 & 300 & AMD, CNV, CSC, DR, RVO \\
\hline
\end{tabular}
\end{table}
'''

import os
import pandas as pd
from collections import *

region = "faz" # vessel or faz
metrics = [' dice', ' jaccard', ' HD', ' precision', ' recall', ' specificity']

result_dir = "2023-03-22-02-21-43-6M-SRF"
matrics_dct = defaultdict(list)

for fold_dir in os.listdir("results/" + result_dir):
    last_dir = sorted(os.listdir("/".join(["results", result_dir, fold_dir])))[-1]
    metric_file = "/".join(["results", result_dir, fold_dir, last_dir, "metrics_val.xlsx"])
    mv_dct = pd.read_excel(metric_file)

    dice_lst = list(mv_dct["_".join([" dice", region])])
    max_idx = dice_lst.index(max(dice_lst))
    print("Dice : ", fold_dir, max(dice_lst))
    for metrix in metrics:
        matrics_dct[metrix.replace(" ", "")].append(list(mv_dct["_".join([metrix, region])])[max_idx])
print_lst = []
for k, v in matrics_dct.items():
    print(k, sum(v) / len(v))
    print_lst.append(str(sum(v) / len(v))[:5])
print(" & ".join(print_lst))


