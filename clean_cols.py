def clean_cols(df):
    import re
    
    cols=list(df.columns.values)
    
    # Lowercase everything
    cols=list(map(lambda x: x.lower(), cols))
    
    # Remove special characters 
    cols = [re.sub(r'[^a-zA-Z0-9]','_',string) for string in cols]
    
    # Rename colums
    df.columns = cols

    return df