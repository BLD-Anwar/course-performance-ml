import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def create_features(df):
    df["academic_score"] = (
        df["assignment_avg"] * 0.3 +
        df["quiz_avg"] * 0.3 +
        df["midterm_marks"] * 0.4
    )

    df["engagement_score"] = (
        df["attendance_percent"] * 0.6 +
        df["study_hours_per_week"] * 5
    )

    return df


def select_features(df):
    X = df[["academic_score", "engagement_score"]]
    y = df["final_result"]
    return X, y

