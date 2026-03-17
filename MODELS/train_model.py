


# import sys
# import os

# # Add parent directory to path if preprocessing is in a different location
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from preprocessing_p import clean_data, create_features, select_features


# import sqlite3
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib




# # Connect to database
# conn = sqlite3.connect("C:\\Users\\anwar\\OneDrive\\Desktop\\HACKATHON_3\\DATA\\university.db")

# # Load data
# query = "SELECT attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result FROM course_performance"
# df = pd.read_sql(query, conn)
# conn.close()

# df = clean_data(df)
# df = create_features(df)
# X, y = select_features(df)


# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train model
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)

# print(f"Random Forest Accuracy: {accuracy * 100:.2f}%")

# # Train Logistic Regression
# log_model = LogisticRegression(max_iter=1000)
# log_model.fit(X_train, y_train)

# log_predictions = log_model.predict(X_test)
# log_accuracy = accuracy_score(y_test, log_predictions)

# print(f"Logistic Regression Accuracy: {log_accuracy * 100:.2f}%")


# # Test model
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)

# print(f"Model Accuracy: {accuracy * 100:.2f}%")

# # Save model
# joblib.dump(model, "student_performance_model.pkl")
# print("Model saved successfully!")














import sqlite3
import pandas as pd
import joblib
import sys
import os
 
from sklearn.ensemble         import RandomForestClassifier
from sklearn.linear_model     import LogisticRegression
from sklearn.tree             import DecisionTreeClassifier
from sklearn.model_selection  import train_test_split
from sklearn.metrics          import (accuracy_score, recall_score,
                                       precision_score, f1_score)
 
# ── PATHS ─────────────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_PATH, MODEL_PATH, RANDOM_STATE, TEST_SIZE, N_ESTIMATORS
from preprocessing_p import clean_data, create_features, select_features
 
# ── LOAD DATA ─────────────────────────────────────────────────────────────────
print("📂  Loading data from database...")
conn = sqlite3.connect(DB_PATH)
df   = pd.read_sql(
    "SELECT attendance_percent, assignment_avg, quiz_avg, "
    "midterm_marks, study_hours_per_week, final_result "
    "FROM course_performance",
    conn
)
conn.close()
print(f"    Loaded {len(df)} records.")
 
# ── PREPROCESS ────────────────────────────────────────────────────────────────
df   = clean_data(df)
df   = create_features(df)
X, y = select_features(df)
 
print(f"    Features : academic_score, engagement_score")
print(f"    Class balance: Pass={y.sum()} | Fail={len(y)-y.sum()}")
 
# ── SPLIT ─────────────────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
print(f"    Train: {len(X_train)} | Test: {len(X_test)}\n")
 
# ── HELPER: EVALUATE ──────────────────────────────────────────────────────────
def evaluate(name, model, X_tr, y_tr, X_te, y_te):
    model.fit(X_tr, y_tr)
    preds = model.predict(X_te)
 
    acc  = accuracy_score(y_te, preds)
    rec  = recall_score(y_te, preds, pos_label=0)   # recall for FAIL class
    prec = precision_score(y_te, preds, pos_label=0, zero_division=0)
    f1   = f1_score(y_te, preds, pos_label=0, zero_division=0)
 
    print(f"── {name} ──")
    print(f"   Accuracy  : {acc*100:.2f}%")
    print(f"   Recall    : {rec*100:.2f}%  ← (failing students caught)")
    print(f"   Precision : {prec*100:.2f}%")
    print(f"   F1 Score  : {f1*100:.2f}%")
    print()
 
    return model, rec   # return model + recall for comparison
 
# ── TRAIN ALL THREE MODELS ────────────────────────────────────────────────────
rf_model, rf_recall = evaluate(
    "Random Forest",
    RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=RANDOM_STATE),
    X_train, y_train, X_test, y_test
)
 
lr_model, lr_recall = evaluate(
    "Logistic Regression",
    LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
    X_train, y_train, X_test, y_test
)
 
dt_model, dt_recall = evaluate(
    "Decision Tree",
    DecisionTreeClassifier(max_depth=5, random_state=RANDOM_STATE),
    X_train, y_train, X_test, y_test
)
 
# ── SAVE BEST MODEL ───────────────────────────────────────────────────────────
# Compare all three by recall (we care most about catching failing students)
all_models = [
    ("Random Forest",      rf_model, rf_recall),
    ("Logistic Regression", lr_model, lr_recall),
    ("Decision Tree",       dt_model, dt_recall),
]
best_name, best_model, best_recall = max(all_models, key=lambda x: x[2])
 
# Also save Decision Tree separately so it can be loaded independently
dt_path = MODEL_PATH.parent / "decision_tree_model.pkl"
joblib.dump(dt_model, dt_path)
print(f"💾  Decision Tree saved : {dt_path}")
 
joblib.dump(best_model, MODEL_PATH)
print(f"✅  Best model: {best_name} (Recall={best_recall*100:.2f}%)")
print(f"    Saved to  : {MODEL_PATH}")
 