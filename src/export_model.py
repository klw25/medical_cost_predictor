import joblib
import os
from train_model import run_pipeline

def export_model():
    # This calls the function and gets the returned model
    rf_medical_cost_model = run_pipeline()

    base_dir = os.path.dirname(__file__)
    save_path = os.path.join(base_dir, 'medical_model.pkl')

    joblib.dump(rf_medical_cost_model, save_path)
    print(f"Model saved to: {save_path}")

if __name__ == "__main__":
    export_model()