#!/bin/bash
# ⚙️🗂️ Complete Simplex Organization
# Finishes organizing remaining files by type

SIMPLEX_DIR="/storage/emulated/0/unexusi/terminus/simplex"
cd "$SIMPLEX_DIR"

echo "🔄 Completing file organization..."

# Simple function to move files without complex regex
move_by_extension() {
    local ext="$1"
    local target_dir="$2"
    local icon="$3"
    
    for file in *."$ext"; do
        if [[ -f "$file" ]]; then
            echo "Moving: $file -> $target_dir/${icon}${file}"
            mv "$file" "$target_dir/${icon}${file}"
        fi
    done
}

# Complete remaining file types
echo "🖼️ Moving remaining images..."
move_by_extension "jpg" "🖼️images" "🖼️"
move_by_extension "jpeg" "🖼️images" "🖼️"
move_by_extension "png" "🖼️images" "🖼️"
move_by_extension "webp" "🖼️images" "🖼️"
move_by_extension "svg" "🖼️images" "🖼️"

echo "🎵 Moving audio files..."
move_by_extension "wav" "🎵audio" "🎵"
move_by_extension "mp3" "🎵audio" "🎵"
move_by_extension "m4a" "🎵audio" "🎵"
move_by_extension "mid" "🎵audio" "🎵"

echo "🎬 Moving video files..."
move_by_extension "mp4" "🎬video" "🎬"

echo "🌐 Moving HTML files..."
move_by_extension "html" "🌐html" "🌐"

echo "💻 Moving code files..."
move_by_extension "js" "💻code" "💻"
move_by_extension "tsx" "💻code" "💻"
move_by_extension "cs" "💻code" "💻"

echo "🔬 Moving science files..."
move_by_extension "xml" "🔬science" "🔬"
move_by_extension "asnt" "🔬science" "🔬"
move_by_extension "sdf" "🔬science" "🔬"
move_by_extension "root" "🔬science" "🔬"

echo "📊 Moving spreadsheets..."
move_by_extension "csv" "📊spreadsheets" "📊"
move_by_extension "xlsx" "📊spreadsheets" "📊"
move_by_extension "xls" "📊spreadsheets" "📊"

echo "📦 Moving archives..."
move_by_extension "zip" "📦archives" "📦"

echo "🔧 Moving config files..."
move_by_extension "env" "🔧config" "🔧"
move_by_extension "yaml" "🔧config" "🔧"
move_by_extension "ics" "🔧config" "🔧"
move_by_extension "kdbx" "🔧config" "🔧"

echo "🗃️ Moving misc files..."
move_by_extension "emmx" "🗃️misc" "🗃️"
move_by_extension "mht" "🗃️misc" "🗃️"
move_by_extension "pub" "🗃️misc" "🗃️"
move_by_extension "ppsx" "🗃️misc" "🗃️"
move_by_extension "ipynb" "🗃️misc" "🗃️"

# Handle files without extensions
echo "🗃️ Moving files without extensions..."
for file in *; do
    if [[ -f "$file" && ! "$file" =~ \. && ! "$file" =~ ^🗃️ ]]; then
        echo "Moving special file: $file -> 🗃️misc/🗃️${file}"
        mv "$file" "🗃️misc/🗃️${file}"
    fi
done

echo "✅ Organization complete!"
echo "📊 Final summary:"
for dir in 📝markdown 🗂️json 📄pdf 📃txt 📘docx 🌐html 🐍python ⚙️scripts 📋logs 📦archives 🎵audio 🎬video 🖼️images 📊spreadsheets 💻code 🔬science 🔧config 🗃️misc; do
    if [[ -d "$dir" ]]; then
        count=$(find "$dir" -type f | wc -l)
        echo "  $dir: $count files"
    fi
done