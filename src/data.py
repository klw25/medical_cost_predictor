import pandas as pd
from pathlib import Path

def load_data():
    current_file_path = Path(__file__).resolve()
    project_root = current_file_path.parent.parent
    medical_cost_path = project_root / "data" / "medical_cost_prediction_dataset.csv"

    medical_cost_data = pd.read_csv(medical_cost_path)
    return medical_cost_data