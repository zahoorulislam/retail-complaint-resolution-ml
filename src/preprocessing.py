"""
Preprocessing functions for CFPB complaint data.
"""

def clean_column_names(df):
    """Standardize column names."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df
