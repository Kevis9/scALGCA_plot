import seaborn as sns
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('mp1_bcp1/cell_states_score.csv')
# 用sklearn做0-1归一化
scaler = MinMaxScaler()
data_norm = scaler.fit_transform(data.to_numpy())
sns.heatmap(data_norm,linewidths=0)
plt.savefig('cell_state_heatmap.png', dpi=300, transparent=True,bbox_inches="tight")