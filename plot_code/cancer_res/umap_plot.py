import numpy as np
import matplotlib.pyplot as plt
import umap
import seaborn as sns
import pandas as pd
import anndata as ad

def run_umap(data):
    reducer = umap.UMAP()
    embedding = reducer.fit_transform(data)
    return embedding

def plot_umap(data, label, save_path):
    data_df = pd.DataFrame(data, columns=['x', 'y'])
    data_df['label'] = label
    sns.scatterplot(data=data_df, x='x', y='y', hue='label', s=8, linewidth=0)
    plt.savefig(save_path, dpi=300, transparent=True)    
    


def read_data(data_paths):
    datas = []
    for path in data_paths:
        data = np.load(path)
        datas.append(data)
    return datas

data_paths = [
    'mp1_bcp1/query_embeddings_ours.npy',
    'mp1_bcp1/query_embeddings_scgcn.npy'
]

save_paths = [
    'ours',
    'scgcn'
]

datas = read_data(data_paths)

# all_data = np.concatenate([data.X.toarray() for data in datas], axis=0)
# print(all_data.shape)
# bcp1_label = ['BC-P1' for i in range(datas[0].n_obs)]
# bcp2_label = ['BC-P2' for i in range(datas[1].n_obs)]
# bcp3_label = ['BC-P3' for i in range(datas[2].n_obs)]
# pcp1_label = ['PC-P1' for i in range(datas[3].n_obs)]
# all_label = bcp1_label + bcp2_label + bcp3_label + pcp1_label
# embeddings = run_umap(all_data)
for i, data in enumerate(datas):
    embeddings = run_umap(data)   
    np.save(save_paths[i] +'_embeddings.npy', embeddings) 
    label = pd.read_csv('query_true.csv').iloc[:, 0].tolist()
    plot_umap(embeddings, label = label, save_path = save_paths[i] + "_umap.png")    

