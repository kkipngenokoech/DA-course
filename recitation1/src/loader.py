import pandas as pd

def get_clean_city_data(filepath):
    """
    Loads the city air quality data 
    """
    # 1. Fix the separator (;) and decimal (,) format
    df = pd.read_csv(filepath, sep=';', decimal=',', na_values=-200)
    
    # 2. Drop the empty columns at the end
    df = df.dropna(how='all', axis=1)

    # 3. Create a proper timeline
    df['Timestamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H.%M.%S')
    df.set_index('Timestamp', inplace=True)
    
    # 4. Select only what we need for the decision
    # CO(GT) = The Truth (Reference Analyzer)
    # PT08.S1(CO) = The Cheap Sensor reading
    return df[['CO(GT)', 'PT08.S1(CO)']]