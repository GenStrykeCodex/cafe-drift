import json
import os
import hashlib

BASE_DATA_DIR = "runtime_data"


def ensure_data_dir(data_dir: str):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def generate_hash(data: dict) -> str:
    json_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(json_string.encode("utf-8")).hexdigest()


def save_with_integrity(filename: str, data: dict, integrity_file: str = "integrity.json"):
    save_json(filename, data)

    integrity_path = os.path.join(BASE_DATA_DIR, integrity_file)
    integrity_data = load_json(integrity_file, default={})

    integrity_data[filename] = generate_hash(data)
    save_json(integrity_file, integrity_data)


def load_with_integrity(filename: str, default: dict, integrity_file: str = "integrity.json"):
    data = load_json(filename, default)
    integrity_data = load_json(integrity_file, default={})

    stored_hash = integrity_data.get(filename)
    current_hash = generate_hash(data)

    if stored_hash is None:
        return data, True  # First-time save

    return data, stored_hash == current_hash


def save_json(filename: str, data: dict, data_dir: str = BASE_DATA_DIR):
    ensure_data_dir(data_dir)
    filepath = os.path.join(data_dir, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filename: str, default: dict, data_dir: str = BASE_DATA_DIR):
    filepath = os.path.join(data_dir, filename)

    if not os.path.exists(filepath):
        return default

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return default
