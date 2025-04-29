# utils/data_loader.py
import json
import os

def load_test_data(filename="test_data.json"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'data', filename)
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise
    except json.JSONDecodeError:
        raise