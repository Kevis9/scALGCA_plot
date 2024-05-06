import numpy as np
import matplotlib.pyplot as plt
import umap
import seaborn as sns
import pandas as pd
import anndata as ad
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os

def run_umap(data):
    reducer = umap.UMAP()
    embedding = reducer.fit_transform(data)
    return embedding

def plot_umap(data, label, save_path):
    data_df = pd.DataFrame(data, columns=['x', 'y'])
    data_df['label'] = label
    sns.scatterplot(data=data_df, x='x', y='y', hue='label', s=8, linewidth=0)    
    plt.legend(bbox_to_anchor=(1, 0.5), ncol=1)
    plt.savefig(save_path, dpi=300, transparent=True, bbox_inches="tight")    
    plt.clf()
    

methods = [
    'ours',
    'seurat'
]

for i in range(len(methods)):
    if methods[i] == 'ours':
        ref_e = np.load('pcp1_mp1/ref_embeddings_ours.npy')
        query_e = np.load('pcp1_mp1/query_embeddings_ours.npy')
        ref_l = pd.read_csv('pcp1_mp1/ref_true_ours.csv').iloc[:, 0].tolist()
        query_l = pd.read_csv('pcp1_mp1/query_pred_ours.csv').iloc[:, 0].tolist()        
        data = np.concatenate((ref_e, query_e), axis = 0)
        data = MinMaxScaler().fit_transform(data)
        embeddings = run_umap(data)        
        label = ref_l + query_l
    elif methods[i] == 'seurat':
        embeddings = pd.read_csv('pcp1_mp1/embeddings_2d_seurat.csv').to_numpy()
        label = pd.read_csv('pcp1_mp1/all_preds_seurat.csv').iloc[:, 0].tolist()
    plot_umap(embeddings, label = label, save_path = methods[i] + "_umap.png")    
