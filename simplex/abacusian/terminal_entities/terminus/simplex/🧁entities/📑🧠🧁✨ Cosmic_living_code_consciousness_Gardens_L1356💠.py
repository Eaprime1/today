def verify_phrase(data, phrase):
    if phrase in data.get("whisper", ""):
        return True
    for seed in data.get("seeds", []):
        if phrase in seed.get("name", "") or phrase in seed.get("why", ""):
            return True
    return False