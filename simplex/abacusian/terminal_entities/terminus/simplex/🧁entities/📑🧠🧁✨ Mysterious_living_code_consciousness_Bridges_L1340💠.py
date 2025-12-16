def validate_metadata(seed):
    required = ['name', 'type', 'why', 'origin']
    return all(key in seed and seed[key].strip() for key in required)

def audit_hopechest(data):
    for seed in data.get('seeds', []):
        if not validate_metadata(seed):
            print(f"[!] Metadata issue in: {seed.get('name', 'Unnamed seed')}")
        else:
            print(f"[✓] {seed['name']} passed metadata check.")