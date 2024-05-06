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

def draw_barplot(data, save_path):          
    plt.figure(figsize=(15, 6))      
    # 设置hue的顺序    
    hue_order = ['scGCA', 'scGCN', 'SingleR', 'seurat', 'scmap']
    ax = sns.barplot(x="exp", y="val", hue="method", data=data, palette=sns.color_palette(colors), hue_order=hue_order, width=.8)            
    plt.xticks(rotation=90)
    ax.set_ylabel('')                    
    plt.savefig(save_path, dpi=300, transparent=True, bbox_inches="tight")
    plt.clf()

def to_long_format(data):            
    # data的exp是bcp1_6000-bcp2_6000的格式, 变成BCP1-BCP2_6000，并且转大写    
    data['exp'] = data['exp'].apply(lambda x: x.upper())
    data['exp'] = data['exp'].apply(lambda x: x.replace('_6000', ''))    
    data = data.melt(id_vars=['exp'], var_name='method', value_name='val')    
    return data        


acc_data = to_long_format(pd.read_csv('cancer_acc.csv'))
f1_data = to_long_format(pd.read_csv('cancer_f1.csv'))

draw_barplot(acc_data, 'cancer_res_acc_bar.png')
draw_barplot(f1_data, 'cancer_res_f1_bar.png')


