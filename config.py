from pathlib import Path
 
# ── PROJECT ROOT ──────────────────────────────────────────────────────────────
# This file lives in the project root, so BASE_DIR = project root folder
BASE_DIR = Path(__file__).resolve().parent
 
# ── DATA ──────────────────────────────────────────────────────────────────────
DATA_DIR   = BASE_DIR / "DATA"
DB_PATH    = DATA_DIR / "university.db"
 
# ── MODELS ────────────────────────────────────────────────────────────────────
MODELS_DIR  = BASE_DIR / "MODELS"
MODEL_PATH  = MODELS_DIR / "student_performance_model.pkl"
 
# ── FEATURE ENGINEERING WEIGHTS ──────────────────────────────────────────────
# Defined here once — used in preprocessing, predict, retrain, and app
ACADEMIC_WEIGHTS = {
    "assignment_avg":  0.25,
    "quiz_avg":        0.25,
    "midterm_marks":   0.40,
    "study_bonus":     0.10,   # study_hours * 5 * 0.10
}
 
ENGAGEMENT_WEIGHTS = {
    "attendance_percent":    0.6,
    "study_hours_per_week":  5.0,   # multiplied, then used as-is
}
 
# ── THRESHOLDS ────────────────────────────────────────────────────────────────
PASS_THRESHOLD          = 50    # academic score >= this → pass
ATTENDANCE_GATE         = 50    # attendance below this → auto fail
HIGH_RISK_SCORE         = 50    # academic score below this → High risk
MEDIUM_RISK_SCORE       = 68    # between HIGH and this → Medium risk
 
# ── MODEL SETTINGS ────────────────────────────────────────────────────────────
RANDOM_STATE  = 42
TEST_SIZE     = 0.2
N_ESTIMATORS  = 100
 
# ── ENSURE DIRECTORIES EXIST ─────────────────────────────────────────────────
DATA_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)
