import pandas as pd
import numpy as np
from TestA.lib.convert_tools import ch2num


def merge_all_data():
    df_a = pd.read_csv("./lvr_landcsv/a_lvr_land_a.csv")
    df_b = pd.read_csv("./lvr_landcsv/b_lvr_land_a.csv")
    df_e = pd.read_csv("./lvr_landcsv/e_lvr_land_a.csv")
    df_f = pd.read_csv("./lvr_landcsv/f_lvr_land_a.csv")
    df_h = pd.read_csv("./lvr_landcsv/h_lvr_land_a.csv")

    # 去除英文Header
    df_a = df_a.iloc[1:, :]
    df_b = df_b.iloc[1:, :]
    df_e = df_e.iloc[1:, :]
    df_f = df_f.iloc[1:, :]
    df_h = df_h.iloc[1:, :]
    df_all = pd.concat([df_a, df_b, df_e, df_f, df_h], axis=0, ignore_index=True)

    df_all.to_csv('./lvr_landcsv/lvr_land_a.csv', index=False)

def clean_data_filter_a(data):

    # 清理建物型態
    data['建物型態'] = data['建物型態'].str.split('(').apply((lambda x: x[0].strip()))

    # 總樓層數 nan => 0
    data['總樓層數'] = data['總樓層數'].replace(np.nan, '零層')
    # 中文轉數字
    data['總樓層數'] = data['總樓層數'].str.split('層').apply((lambda x: x[0].strip()))
    # 非 數字類型 => 轉為 0
    data['總樓層數'] = data['總樓層數'].apply(lambda x: int(ch2num(x)))

    return data

# 功能A
def filter_a_save(data):

    filter_a = (data['主要用途'] == '住家用') & (data['建物型態'] == '住宅大樓') & (data['總樓層數'] >= 13)

    df_filter_a = data[filter_a]
    # print(df_filter_a.shape)
    df_filter_a.to_csv('./OutPut/filter_a.csv', index=False)


def clean_data_filter_b(clean_data: pd):

    clean_data['車位'] = clean_data['交易筆棟數'].str.split('車位').apply((lambda x: int(x[-1])))
    # print(clean_data['車位'])

    return clean_data

# 功能B
def filter_b_cal_statistics(statistics_data: pd):

    # - 計算【總件數】
    counts = statistics_data.shape[0]
    print('總件數:', counts)

    # - 計算【總車位數】(透過交易筆棟數)
    parking_space_count = statistics_data['車位'].sum()
    print('總車位數:', parking_space_count)

    # - 計算【平均總價元】
    avg_total_price = statistics_data['總價元'].mean()
    print('平均總價元:', avg_total_price)

    # - 計算【平均車位總價元】
    # 車位數 不為1 & 車位總價元不為 0
    filter_park = (statistics_data['車位'] != 0) & (statistics_data['車位總價元'] != 0)
    statistics_park_data = statistics_data[filter_park]
    statistics_park_data.reset_index(drop=True, inplace=True)

    # 車位總價元 / 車位數
    statistics_park_data['車位單價'] = statistics_park_data.apply(lambda x: x['車位總價元']/x['車位'], axis=1)
    avg_parking_space_price = statistics_park_data['車位單價'].mean()
    print('平均車位總價元:', avg_parking_space_price)

    df = pd.DataFrame({'總件數': [counts],
                  '總車位數': [parking_space_count],
                  '平均總價元': [avg_total_price],
                  '平均車位總價元': [avg_parking_space_price]})

    df.to_csv('./OutPut/filter_b.csv', index=False)

if __name__ == '__main__':
    #整理檔案
    merge_all_data()

    data = pd.read_csv("./lvr_landcsv/lvr_land_a.csv")
    #
    data_cleaning = clean_data_filter_a(data)
    filter_a_save(data_cleaning)
    #
    data_cleaning_b = clean_data_filter_b(data)
    filter_b_cal_statistics(data_cleaning_b)








