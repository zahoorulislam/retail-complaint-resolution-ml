"""
Feature engineering functions for structured and narrative complaint data.
"""

def add_text_length(df, text_column="consumer_complaint_narrative"):
    """Add a simple text length feature."""
    df = df.copy()
    df["narrative_length"] = df[text_column].fillna("").str.len()
    return df
