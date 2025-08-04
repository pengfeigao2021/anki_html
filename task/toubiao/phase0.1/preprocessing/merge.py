import os
import sys
import pandas as pd
import numpy as np
import tabulate

DATA_FOLDER = '/Users/AlexG/Documents/2025/toubiao/工程7.0'
FILE_123 = 'merge-123.tab'
FILE_4 = '4.特征码表.csv'
FILE_5 = '5.专家评分表.csv'

def load_123(): 
    df = pd.read_csv(os.path.join(DATA_FOLDER, FILE_123), sep='\t')
    print(df.head())
    return df

def load_4(col1='标段唯一标识', col2='投标人名称'): 
    df4 = pd.read_csv(os.path.join(DATA_FOLDER, FILE_4))

    # Compute group sizes
    group_sizes = df4.groupby(by=[col1, col2])['zaojiasuo1'].transform('size')

    # Build mask: drop if group size > 1 and col3 is null
    mask = ~((group_sizes > 1) & (df4['zaojiasuo1'].isnull()))

    # Apply mask
    df_filtered = df4[mask]
    df_dedup = df_filtered.drop_duplicates(subset=[col1, col2], keep=False)
    print(df4.shape[0], df_filtered.shape[0], df_dedup.shape[0])
    print(df_dedup.head())
    return df_dedup

def clean_by_biaoduan_toubiaoren(df, col1='标段唯一标识', col2='投标人代码'):
    # check for duplicates and remove them
    total = df.shape[0]
    uc = df[[col1, col2]].drop_duplicates().shape[0]
    # df_unique_strict = df[~df.duplicated(subset=['col1', 'col2'], keep=False)]
    df_unique_strict = df.drop_duplicates(subset=[col1, col2], keep=False)
    print('total {} rows with {} unique ({}, {}) pairs -> remove all duplicates remaining rows: {}'.format(total, uc, col1, col2, df_unique_strict.shape[0]))
    return df_unique_strict

if __name__ == '__main__':
    # 读取数据
    # data1 = pd.read_csv('data1.csv')
    # data2 = pd.read_csv('data2.csv')

    # # 合并数据
    # merged_data = pd.concat([data1, data2], axis=0)

    # # 保存合并后的数据
    # merged_data.to_csv('merged_data.csv', index=False)

    df123 = load_123()
    df123 = clean_by_biaoduan_toubiaoren(df123, col2='投标人名称')
    df4 = load_4()
    df4 = clean_by_biaoduan_toubiaoren(df4, col2='投标人名称')

    # merge 1234
    df = pd.merge(df123, df4, on=['标段唯一标识', '投标人名称'], how='inner', suffixes=('', '_detail'))
    print('total rows after merge: {}'.format(df.shape[0]))
    out = os.path.join(DATA_FOLDER, 'merged_data1234_v3.csv')
    df.to_csv(out, index=False)

    print("数据合并完成！")