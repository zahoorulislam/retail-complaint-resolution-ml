"""
Model training functions.
"""

from sklearn.linear_model import LogisticRegression

def build_baseline_logistic_regression():
    """Create a baseline class-weighted logistic regression model."""
    return LogisticRegression(max_iter=1000, class_weight="balanced")
