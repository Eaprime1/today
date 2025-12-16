def export_seeds_to_markdown(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 🌱 Hopechest Seed Report\n\n")
        for seed in data.get('seeds', []):
            f.write(f"## {seed['name']}\n")
            f.write(f"**Type:** {seed['type']}\n\n")
            f.write(f"**Why it matters:** {seed['why']}\n\n")
            f.write(f"_Origin: {seed['origin']}_\n\n---\n")