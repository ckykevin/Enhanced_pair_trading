import itertools
from statsmodels.tsa.stattools import coint

def ticker_combinations(full_info, pivoted_return, country_list, industry_list):
    useful_pairs = []
    for country in country_list:
        for industry in industry_list:
            ticker_list = full_info[(full_info['COUNTRY_CODE']==country) & (full_info['Industry Title']==industry)]['TICKER'].unique()
            pairs = list(itertools.combinations(ticker_list, 2))
            for pair in pairs:
                # filter 1: use co-integration - Passed the co-integration test at 90%* significance level.
                pair_return = pivoted_return.loc[:,pair].dropna(axis = 0)
                p_value = coint(pair_return.iloc[:,0], pair_return.iloc[:,1])[1]
                if p_value <= 0.1:
                    useful_pairs.append(pair)
            
