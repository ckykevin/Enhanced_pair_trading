import itertools
from statsmodels.tsa.stattools import coint

def ticker_combinations(full_info, pivoted_return, country_list, industry_list):
    """
    find pairs that pass the co-integration test at 90%* significance level.
    
    Parameters
    ---------------
    full_info: dataframe with country and industry information for each equity
    pivoted_return: return dataframe with date as index and ticker as column
    country_list: all the countries we are going to use
    industry_list: all the industries we are going to use
    """
    useful_pairs = []
    for country in country_list:
        for industry in industry_list:
            ticker_list = full_info[(full_info['COUNTRY_CODE']==country) & (full_info['Industry Title']==industry)]['TICKER'].unique()
            pairs = list(itertools.combinations(ticker_list, 2))
            for pair in pairs:
                # filter 1: use co-integration
                pair_return = pivoted_return.loc[:,pair].dropna(axis = 0)
                p_value = coint(pair_return.iloc[:,0], pair_return.iloc[:,1])[1]
                if p_value <= 0.1:
                    useful_pairs.append(pair)
    return useful_pairs   
