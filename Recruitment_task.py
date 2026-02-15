import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not re.fullmatch(r'[a-zA-Z_]+', new_column):
        return pd.DataFrame([])
    
    pattern = r'^\s*([a-zA-Z_]+)\s*([+\-*])\s*([a-zA-Z_]+)\s*$'
    match = re.fullmatch(pattern, role)

    if not match:
        return pd.DataFrame([])
    
    col1_name, operator, col2_name = match.groups()

    if col1_name not in df.columns or col2_name not in df.columns:
        return pd.DataFrame([])
    
    result_df = df.copy()

    try:
        if operator == '+':
            result_df[new_column] = result_df[col1_name] + result_df[col2_name]
        elif operator == '-':
            result_df[new_column] = result_df[col1_name] - result_df[col2_name]
        elif operator == '*':
            result_df[new_column] = result_df[col1_name] * result_df[col2_name]
        
        return result_df
    
    except Exception:
        return pd.DataFrame([])