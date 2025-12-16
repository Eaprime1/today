import json

def load_hopechest(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def list_seeds(data):
    return [(seed['name'], seed['type']) for seed in data.get('seeds', [])]

if __name__ == "__main__":
    hope_data = load_hopechest("hopechest.json")
    for name, seed_type in list_seeds(hope_data):
        print(f"{name} [{seed_type}]")