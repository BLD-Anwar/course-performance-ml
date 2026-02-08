import pandas as pd

def clean_data(df):
    """
    Basic data cleaning:
    - Remove duplicates
    - Drop rows with missing values (if any)
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def select_features(df):
    """
    Select relevant features for the model
    """
    features = [
        "attendance_percent",
        "assignment_avg",
        "quiz_avg",
        "midterm_marks",
        "study_hours_per_week"
    ]
    target = "final_result"

    X = df[features]
    y = df[target]
    return X, y
