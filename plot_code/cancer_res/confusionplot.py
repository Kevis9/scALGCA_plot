import seaborn as sns
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

def draw_color_bar(colors, save_path):
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.5)
    cmap = sns.color_palette(colors)
    cb = sns.color_palette(colors)
    cb = sns.color_palette(colors)
    cb.set_array([])
    cbar = plt.colorbar(cb, orientation='horizontal')
    cbar.set_ticks([])
    cbar.set_ticklabels([])
    plt.savefig(save_path, dpi=300, transparent=True,bbox_inches="tight")
    plt.clf()

def confusion_matrix(true_labels, pred_labels):
    # Create a mapping from class labels to integers
    classes = sorted(set(true_labels + pred_labels))
    
    
    label_to_int = {label: i for i, label in enumerate(classes)}

    # Convert labels to integers
    true_labels_int = [label_to_int[label] for label in true_labels]
    pred_labels_int = [label_to_int[label] for label in pred_labels]

    # Initialize the confusion matrix
    num_classes = len(classes)
    
    matrix = [[0] * num_classes for _ in range(num_classes)]

    # Fill the confusion matrix
    for true, pred in zip(true_labels_int, pred_labels_int):
        matrix[true][pred] += 1

    # Normalize the confusion matrix
    for i in range(num_classes):
        row_sum = sum(matrix[i])
        if row_sum != 0:
            matrix[i] = [count / row_sum for count in matrix[i]]


    classes = [label for label, _ in sorted(label_to_int.items(), key=lambda x: x[1])]
    conf_matrix_df = pd.DataFrame(matrix, index=classes, columns=classes)
    
    # 我们不看Unassigned
    true_classes = []
    for label in classes:
        if label in true_labels and label != 'Unassigned':
            true_classes.append(label)
    conf_matrix_df = conf_matrix_df.loc[true_classes][:]
    
    return conf_matrix_df

def read_pred_true_label(res_path):
    preds = pd.read_csv(os.path.join(res_path, 'query_pred.csv')).iloc[:, 0].tolist()
    trues = pd.read_csv(os.path.join(res_path, 'query_true.csv')).iloc[:, 0].tolist()    
    return preds, trues


res_path = 'pcp1_mp1'

methods = [
    'ours',
    'singler',
    'scgcn',
    'seurat'    
]

query_true = pd.read_csv(os.path.join(res_path, 'query_true.csv')).iloc[:, 0].tolist()


for i in range(len(methods)):
    query_pred = pd.read_csv(os.path.join(res_path, 'query_pred_' + methods[i] + '.csv')).iloc[:, 0].tolist()
    print('acc is {:.3f}'.format(accuracy_score(query_true, query_pred)))
    conf_matrix = confusion_matrix(query_true, query_pred)
    # print("{:}, {:.3f}".format(methods[i], conf_matrix.iloc[2][2]))
    sns.heatmap(conf_matrix,linewidths=0, cmap='Blues')
    plt.savefig(methods[i]+'_'+'confmatrix', dpi=300, transparent=True,bbox_inches="tight")
    plt.clf()

# 绘制color bar, color bar的颜色和cmap一致
# draw_color_bar(['#f7fbff', '#08306b'], 'colorbar')