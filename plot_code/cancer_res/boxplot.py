import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

colors = [
    '#2878b5',
    '#9ac9db',
    '#f8ac8c',
    '#c82423',
    '#ff8884',
    '#f8ac8c'
]


def draw_boxplot(data, save_path):        
    hue_order = ['scGCA', 'scGCN', 'SingleR', 'seurat', 'scmap']
    sns.boxplot(data=data,showfliers=False, width=.5, palette=sns.color_palette(colors), order=hue_order)    
    # plt.legend(bbox_to_anchor=(1, 0.7))    
    plt.xlabel('')
    plt.ylabel('')
    plt.savefig(save_path, dpi=300, transparent=True,bbox_inches="tight")    
    plt.clf()

def to_long_format(data):    
    # data的exp是bcp1_6000-bcp2_6000的格式, 变成BCP1-BCP2_6000，并且转大写
    data['exp'] = data['exp'].apply(lambda x: x.upper())
    data['exp'] = data['exp'].apply(lambda x: x.replace('_6000', ''))    
    data = data.melt(id_vars=['exp'], var_name='method', value_name='val')    
    return data        


acc_data = pd.read_csv('cancer_acc.csv')
f1_data = pd.read_csv('cancer_f1.csv')

draw_boxplot(acc_data, save_path='cancer_res_acc_box')
draw_boxplot(f1_data, save_path='cancer_res_f1_box')
