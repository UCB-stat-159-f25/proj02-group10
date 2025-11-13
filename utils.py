import pandas as pd

def edit_year(df):
    """ Modifies year value from float to datetime."""
    
    df_output = df.copy()  # Create a copy
    df_output['Year'] = df['Year'].astype(int)
    
    return df_output