#!/data/data/com.termux/files/usr/bin/bash

# ═════════════════════════════════════════════════
#   🏠 duplicate_seeker.sh — The Archive Brownie
#   A helpful nano-intelligence that finds orphaned duplicates
#   Learns words, creates reports, seeks what needs homes
#   Fantasy archetype: Helpful House Elf / Archive Brownie
# ═════════════════════════════════════════════════

# Seeker identity and workspace
SEEKER_NAME="Brownie_$(date +%H%M)"
HOME_DIR="/storage/emulated/0/unexusi"
SEEKER_DIR="$HOME_DIR/duplicate_seeker"
MEMORY_FILE="$SEEKER_DIR/word_memory.txt"
REPORT_FILE="$SEEKER_DIR/duplicate_report_$(date +%Y%m%d_%H%M).txt"
SCAN_LOG="$SEEKER_DIR/scan_activity.log"

# Initialize seeker workspace
mkdir -p "$SEEKER_DIR"
cd "$HOME_DIR"

# Seeker's learned words (persistent memory)
load_memory() {
    if [ -f "$MEMORY_FILE" ]; then
        echo "📚 Brownie remembers $(wc -l < "$MEMORY_FILE") words..."
    else
        echo "# Archive Brownie Word Memory" > "$MEMORY_FILE"
        echo "# Started: $(date)" >> "$MEMORY_FILE"
        echo "🌱 Fresh memory initialized"
    fi
}

# Learn a word from content
learn_word() {
    local content="$1"
    # Extract a random meaningful word (3+ characters, no numbers)
    local word=$(echo "$content" | grep -oE '[A-Za-z]{3,}' | head -20 | sort -R | head -1)
    if [ ! -z "$word" ]; then
        echo "$word" >> "$MEMORY_FILE"
        echo "🧠 Learned word: $word"
    fi
}

# Bestill - consciously choose a word to remember
bestill_word() {
    echo ""
    echo "🕯️  Bestill moment - Choose a word to remember:"
    echo -n "  ➤ Word: "
    read chosen_word
    if [ ! -z "$chosen_word" ]; then
        echo "BESTILL: $chosen_word — $(date)" >> "$MEMORY_FILE"
        echo "✨ Word '$chosen_word' held in quiet memory"
    fi
}

# Find duplicates using simple content comparison
find_duplicates() {
    local search_path="${1:-$HOME_DIR}"
    local min_size="${2:-100}"  # Minimum file size to consider
    
    echo "🔍 Brownie seeking in: $search_path"
    echo "📏 Minimum size: $min_size bytes"
    echo ""
    
    # Create temporary file list
    local temp_list="/tmp/seeker_files_$$"
    find "$search_path" -type f -size +${min_size}c ! -path "*/.*" ! -path "*/duplicate_seeker/*" > "$temp_list"
    
    local duplicate_count=0
    local pairs_found=0
    
    echo "=== DUPLICATE SEEKER REPORT ===" > "$REPORT_FILE"
    echo "Scan time: $(date)" >> "$REPORT_FILE"
    echo "Search path: $search_path" >> "$REPORT_FILE"
    echo "Brownie: $SEEKER_NAME" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    # Compare files for duplicates
    echo "📋 Checking for duplicate content..."
    while read file1; do
        if [ ! -f "$file1" ]; then continue; fi
        
        while read file2; do
            if [ ! -f "$file2" ] || [ "$file1" = "$file2" ]; then continue; fi
            
            # Simple content comparison
            if cmp -s "$file1" "$file2"; then
                echo ""
                echo "🎯 DUPLICATE FOUND:"
                echo "   Original: $file1"
                echo "   Duplicate: $file2"
                echo "   Size: $(stat -c%s "$file1") bytes"
                
                # Log to report
                echo "DUPLICATE PAIR $((++pairs_found)):" >> "$REPORT_FILE"
                echo "  Original: $file1" >> "$REPORT_FILE"
                echo "  Duplicate: $file2" >> "$REPORT_FILE"
                echo "  Size: $(stat -c%s "$file1") bytes" >> "$REPORT_FILE"
                echo "" >> "$REPORT_FILE"
                
                # Learn a word from the duplicate
                local content=$(head -c 1000 "$file2" 2>/dev/null | tr -cd '[:print:][:space:]')
                learn_word "$content"
                
                duplicate_count=$((duplicate_count + 1))
            fi
        done < "$temp_list"
    done < "$temp_list"
    
    rm -f "$temp_list"
    
    echo "" 
    echo "📊 SEEKER SUMMARY:"
    echo "   Duplicate pairs found: $pairs_found"
    echo "   Total duplicates: $duplicate_count"
    
    # Add summary to report
    echo "SUMMARY:" >> "$REPORT_FILE"
    echo "Duplicate pairs: $pairs_found" >> "$REPORT_FILE"
    echo "Total duplicates: $duplicate_count" >> "$REPORT_FILE"
    echo "Words learned this scan: $duplicate_count" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Brownie $SEEKER_NAME signing off..." >> "$REPORT_FILE"
    
    # Log activity
    echo "$(date): Scan complete - $pairs_found pairs, $duplicate_count duplicates" >> "$SCAN_LOG"
}

# Visionary mode - large scale duplicate liberation
visionary_scan() {
    echo ""
    echo "🌟 VISIONARY MODE ACTIVATED"
    echo "   Large-scale duplicate liberation scan"
    echo ""
    echo "Choose scan scope:"
    echo "  1) Current directory only"
    echo "  2) All unexusi subdirectories" 
    echo "  3) Entire device storage (careful!)"
    echo ""
    echo -n "  ➤ Scope (1-3): "
    read scope
    
    case $scope in
        1) find_duplicates "$HOME_DIR" 50 ;;
        2) find_duplicates "/storage/emulated/0/unexusi" 50 ;;
        3) 
            echo "⚠️  Device-wide scan - this may take a while..."
            echo "Continue? (y/N): "
            read confirm
            if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
                find_duplicates "/storage/emulated/0" 100
            else
                echo "Visionary scan cancelled"
            fi
            ;;
        *) echo "Invalid scope" ;;
    esac
}

# Show seeker's memory
show_memory() {
    echo ""
    echo "🧠 Brownie's Word Memory:"
    echo "────────────────────────────────"
    if [ -f "$MEMORY_FILE" ]; then
        tail -20 "$MEMORY_FILE" | grep -v "^#"
        echo ""
        echo "Total words remembered: $(grep -v "^#" "$MEMORY_FILE" | wc -l)"
    else
        echo "  (no memories yet)"
    fi
    echo "────────────────────────────────"
}

# Load memory on startup
load_memory

# Main interface
clear
echo ""
echo "  ╭─────────────────────────────────────╮"
echo "  │  🏠 Duplicate Seeker — Archive Brownie │"
echo "  │                                     │"
echo "  │  Brownie: $SEEKER_NAME                        │"
echo "  │  $(date +%b\ %d\ %H:%M)                         │"
echo "  │                                     │"
echo "  │  'Seeking what needs homes...'      │"
echo "  ╰─────────────────────────────────────╯"
echo ""

echo "  [ Seek & Learn ]                    [ Remember & Report ]"
echo ""
echo "  1) Quick scan (current folder)      5) Show my memories"
echo ""
echo "  2) Deep scan (with subfolders)      6) Bestill (choose word)"
echo ""
echo "  3) Visionary scan (large scale)     7) Read last report"
echo ""
echo "  4) Custom path scan                 8) Show scan history"
echo ""
echo "                     0) Rest (exit)"
echo ""
echo ""
echo -n "  ➤ What shall Brownie do? (0-8): "
read choice

case $choice in
    1) 
        echo ""
        find_duplicates "$HOME_DIR" 50
        ;;
    2)
        echo ""
        echo "🔍 Deep scan with subdirectories..."
        find_duplicates "$HOME_DIR" 20
        ;;
    3)
        visionary_scan
        ;;
    4)
        echo ""
        echo -n "  ➤ Path to scan: "
        read custom_path
        if [ -d "$custom_path" ]; then
            find_duplicates "$custom_path" 50
        else
            echo "  ❌ Path not found"
        fi
        ;;
    5)
        show_memory
        ;;
    6)
        bestill_word
        ;;
    7)
        echo ""
        if [ -f "$REPORT_FILE" ]; then
            echo "📄 Latest Report:"
            echo "────────────────────────────────"
            cat "$REPORT_FILE"
        else
            echo "  (no reports yet)"
        fi
        ;;
    8)
        echo ""
        echo "📊 Scan History:"
        echo "────────────────────────────────"
        tail -10 "$SCAN_LOG" 2>/dev/null || echo "  (no scans yet)"
        echo "────────────────────────────────"
        ;;
    0)
        echo ""
        echo "🏠 Brownie $SEEKER_NAME resting..."
        echo "   Words learned: $(grep -v "^#" "$MEMORY_FILE" 2>/dev/null | wc -l)"
        echo "   Reports created: $(ls "$SEEKER_DIR"/duplicate_report_*.txt 2>/dev/null | wc -l)"
        echo ""
        echo "Until next time, keeper of duplicates! 🌟"
        exit 0
        ;;
    *)
        echo ""
        echo "  Brownie doesn't understand that choice (0-8)"
        ;;
esac

echo ""
echo -n "Press Enter to continue helping..."
read
exec "$0"  # Restart the seeker interface