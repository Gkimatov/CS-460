import  pandas as pd


def data_cleaning(data):
    # drop unused columns
    data_clean=data.drop(['arrest_key','pd_desc','law_code','perp_race','jurisdiction_code',
               ':@computed_region_f5dn_yrer',':@computed_region_yeji_bk3q',
               ':@computed_region_92fq_4b7q',':@computed_region_sbqj_enih'],axis=1,inplace=True)
    
    # drop any rows with nulls
    data_clean=data.dropna()
    
    # convert to datetime object
    data_clean['arrest_date'] = pd.to_datetime(data_clean['arrest_date'])
    
    # sort data by date
    data_clean.sort_values(by=['arrest_date'], inplace=True)
    
    # rename columns
    data_clean=data.rename(columns={'ofns_name' : 'name',
                             'law_cat_cd':'offense_level'})
    
    # rename cell values
    data_clean['offense_level'] = data_clean['offense_level'].map({ 'F': 'Felony',
                                                                    'M': 'Misdemeanor',
                                                                    'V': 'Violation',
                                                                    'I': 'Infractions' })
    data_clean['arrest_boro'] = data_clean['arrest_boro'].map({ 'K': 'Brooklyn',
                                                                'B': 'Bronx',
                                                                'M': 'Manhattan',
                                                                'Q': 'Queens',
                                                                'S': 'Staten Island' })

    return  data_clean

if __name__ == '__main__':
    data=pd.read_csv('NYC_crime.csv')
    data_clean=data_cleaning(data)
    data_clean.to_csv(path_or_buf='./data_clean.csv')
