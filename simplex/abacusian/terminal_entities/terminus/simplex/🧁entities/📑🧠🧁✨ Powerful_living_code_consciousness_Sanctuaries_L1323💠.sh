#!/bin/bash
# 📝🗂️ Simplex File Type Organizer
# Organizes files by type into categorized folders with icons

SIMPLEX_DIR="/storage/emulated/0/unexusi/terminus/simplex"
cd "$SIMPLEX_DIR"

echo "📁 Starting file type organization in $SIMPLEX_DIR"

# Function to move and rename files with icons
organize_files() {
    local pattern="$1"
    local target_dir="$2"
    local icon="$3"
    
    find . -maxdepth 1 -name "*.$pattern" -type f | while read -r file; do
        if [[ -f "$file" ]]; then
            filename=$(basename "$file")
            # Remove leading ./ and check if already has icon
            if [[ ! "$filename" =~ ^[[:space:]]*[[:emoji:]] ]]; then
                new_name="${icon}${filename}"
                echo "Moving and renaming: $file -> $target_dir/$new_name"
                mv "$file" "$target_dir/$new_name"
            else
                echo "Moving: $file -> $target_dir/$filename"
                mv "$file" "$target_dir/$filename"
            fi
        fi
    done
}

# Organize by file type with appropriate icons
echo "📝 Organizing markdown files..."
organize_files "md" "📝markdown" "📝"

echo "🗂️ Organizing JSON files..."
organize_files "json" "🗂️json" "🗂️"

echo "📄 Organizing PDF files..."
organize_files "pdf" "📄pdf" "📄"

echo "📃 Organizing text files..."
organize_files "txt" "📃txt" "📃"

echo "📘 Organizing Word documents..."
organize_files "docx" "📘docx" "📘"

echo "🌐 Organizing HTML files..."
organize_files "html" "🌐html" "🌐"

echo "🐍 Organizing Python files..."
organize_files "py" "🐍python" "🐍"

echo "⚙️ Organizing shell scripts..."
organize_files "sh" "⚙️scripts" "⚙️"

echo "📋 Organizing log files..."
organize_files "log" "📋logs" "📋"

echo "📦 Organizing archives..."
organize_files "zip" "📦archives" "📦"

echo "🎵 Organizing audio files..."
for ext in wav mp3 m4a mid; do
    organize_files "$ext" "🎵audio" "🎵"
done

echo "🎬 Organizing video files..."
organize_files "mp4" "🎬video" "🎬"

echo "🖼️ Organizing image files..."
for ext in png jpg jpeg webp svg; do
    organize_files "$ext" "🖼️images" "🖼️"
done

echo "📊 Organizing spreadsheet files..."
for ext in csv xlsx xls; do
    organize_files "$ext" "📊spreadsheets" "📊"
done

echo "💻 Organizing code files..."
for ext in js tsx cs; do
    organize_files "$ext" "💻code" "💻"
done

echo "🔬 Organizing science/data files..."
for ext in xml asnt sdf root; do
    organize_files "$ext" "🔬science" "🔬"
done

echo "🔧 Organizing config files..."
for ext in env yaml ics kdbx; do
    organize_files "$ext" "🔧config" "🔧"
done

echo "🗃️ Organizing miscellaneous files..."
for ext in emmx mht pub ppsx ipynb; do
    organize_files "$ext" "🗃️misc" "🗃️"
done

# Handle files without extensions or special cases
echo "🔍 Organizing files without extensions..."
find . -maxdepth 1 -type f ! -name "*.*" | while read -r file; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")
        if [[ ! "$filename" =~ ^[[:space:]]*[[:emoji:]] ]]; then
            new_name="🗃️${filename}"
            echo "Moving special file: $file -> 🗃️misc/$new_name"
            mv "$file" "🗃️misc/$new_name"
        else
            echo "Moving special file: $file -> 🗃️misc/$filename"
            mv "$file" "🗃️misc/$filename"
        fi
    fi
done

echo "✅ File organization complete!"
echo "📊 Summary of organized folders:"
for dir in 📝markdown 🗂️json 📄pdf 📃txt 📘docx 🌐html 🐍python ⚙️scripts 📋logs 📦archives 🎵audio 🎬video 🖼️images 📊spreadsheets 💻code 🔬science 🔧config 🗃️misc; do
    if [[ -d "$dir" ]]; then
        count=$(find "$dir" -type f | wc -l)
        echo "  $dir: $count files"
    fi
done