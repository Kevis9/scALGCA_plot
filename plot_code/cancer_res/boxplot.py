import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


colors = [
    '8ECFC9',
    'FFBE7A',
    'FA7F6F',
    '82B0D2',
    'BEB8DC',
    'E7DAD2'    
]


def draw_boxplot(data, save_path, x, y, hue, width):        
    sns.boxplot(data=data,x='method', y='val', hue='metric', showfliers=False, width=.5, palette=sns.color_palette(colors)) 
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))    
    plt.xlabel('')
    plt.ylabel('')
    plt.savefig('same_cancer_box_plot', dpi=300, transparent=True,bbox_inches="tight")    
    plt.clf()

def to_long_format(data):    
    # data的exp是bcp1_6000-bcp2_6000的格式, 变成BCP1-BCP2_6000，并且转大写
    data['exp'] = data['exp'].apply(lambda x: x.upper())
    data['exp'] = data['exp'].apply(lambda x: x.replace('_6000', ''))    
    data = data.melt(id_vars=['exp'], var_name='method', value_name='val')    
    return data        


# acc_data = to_long_format(pd.read_csv('cancer_acc.csv'))
f1_data = to_long_format(pd.read_csv('cancer_f1.csv'))

draw_boxplot(f1_data, 'cancer_res_f1_bar.png', save_path='exp', x='method', y='val', hue='metric', width=.5)
