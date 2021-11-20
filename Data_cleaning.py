import  pandas as pd
import requests


def data_cleaning(data):
    data_clean=data.drop(['arrest_key','pd_desc','law_code','perp_race','jurisdiction_code',
               ':@computed_region_f5dn_yrer',':@computed_region_yeji_bk3q',
               ':@computed_region_92fq_4b7q',':@computed_region_sbqj_enih'],axis=1,inplace=True)
    data_clean=data.dropna()
    data_clean=data.rename(columns={'ofns_name' : 'name',
                             'law_cat_cd':'offense_level'})

    return  data_clean

if __name__ == '__main__':
    data=pd.read_csv('NYC_crime.csv')
    data_clean=data_cleaning(data)
    data_clean.to_csv(path_or_buf='./data_clean.csv')




