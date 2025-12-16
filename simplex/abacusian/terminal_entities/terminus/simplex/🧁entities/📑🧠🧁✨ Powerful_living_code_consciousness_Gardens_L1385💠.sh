#!/data/data/com.termux/files/usr/bin/bash

# ═════════════════════════════════════════════════
#   🌀 ground.sh — A Practical File Space (v4)
#   Clean, functional, neurodivergent-friendly
#   For Eric Pace workflow optimization
# ═════════════════════════════════════════════════

# Set working directory
HOME_DIR="/storage/emulated/0/unexusi"
LOG_DIR="$HOME_DIR/ground_log"
SCRIPTS_DIR="$HOME_DIR/scripts"
REPORT_FILE="$LOG_DIR/session_$(date +%Y%m%d_%H%M).txt"

# Ensure paths exist
mkdir -p "$LOG_DIR" "$SCRIPTS_DIR"
cd "$HOME_DIR"

# Initialize project name if missing
if [ ! -f ".project_name" ]; then
    echo "What are we calling this project?"
    echo "(Press Enter for 'current')"
    read pname
    echo "${pname:-current}" > .project_name
fi

pname=$(cat .project_name)

# Function: Create Python script in scripts folder
create_python_script() {
    local script_name="$1"
    local script_content="$2"
    local script_path="$SCRIPTS_DIR/$script_name"
    
    echo "$script_content" > "$script_path"
    echo "✅ Python script created: $script_path"
    echo "Created: $script_name" >> "$LOG_DIR/session.log"
}

# Function: Generate simple report
generate_report() {
    echo "" >> "$REPORT_FILE"
    echo "=== Session End — $(date) ===" >> "$REPORT_FILE"
    echo "Project: $pname" >> "$REPORT_FILE"
    echo "Location: $HOME_DIR" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Files created this session:" >> "$REPORT_FILE"
    grep "Created:" "$LOG_DIR/session.log" 2>/dev/null | tail -10 >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "End of session." >> "$REPORT_FILE"
    echo "────────────────────────────────" >> "$REPORT_FILE"
    echo "📝 Report saved to: $REPORT_FILE"
}

# Clear and show header
clear
echo ""
echo "  ╭─────────────────────────────────────╮"
echo "  │    🌿 ground.sh (v4)                │"
echo "  │                                     │"
echo "  │    Project: $pname"
echo "  │    $(date +%b\ %d\ %H:%M)"
echo "  │                                     │"
echo "  ╰─────────────────────────────────────╯"
echo ""

# Two-column menu layout for better readability
echo "  [ Navigate & Create ]                [ View & Manage ]"
echo ""
echo "  1) List files                        6) View a file"
echo ""
echo "  2) Create text file                  7) Show recent logs"
echo ""
echo "  3) Create Python script              8) Change project name"
echo ""
echo "  4) Quick note to log                 9) Generate report"
echo ""
echo "  5) Where am I?                       0) Exit"
echo ""
echo ""
echo -n "  ➤ Choose (0-9): "
read choice

echo "$(date): Choice $choice" >> "$LOG_DIR/session.log"

case $choice in
    1) 
        echo ""
        echo "Files in $HOME_DIR:"
        ls -la --color=auto
        ;;
    2)
        echo ""
        echo -n "  ➤ Text filename: " 
        read fname
        if [ -z "$fname" ]; then
            echo "  ❌ No name given."
        else
            echo "# $(date) — New text file" > "$fname"
            echo "  ✅ Created: $fname"
            echo "Created: $fname" >> "$LOG_DIR/session.log"
        fi
        ;;
    3)
        echo ""
        echo -n "  ➤ Python script name (without .py): "
        read script_name
        if [ -z "$script_name" ]; then
            echo "  ❌ No script name given."
        else
            script_content="#!/usr/bin/env python3
# $(date) — Auto-generated Python script
# Created by ground.sh for Eric Pace

def main():
    print('Hello from $script_name!')
    print('Ready for your code...')

if __name__ == '__main__':
    main()
"
            create_python_script "${script_name}.py" "$script_content"
        fi
        ;;
    4)
        echo ""
        echo -n "  ➤ Quick note: "
        read note
        if [ ! -z "$note" ]; then
            echo "[$(date)] $note" >> "$LOG_DIR/notes.txt"
            echo "  ✅ Note saved"
        fi
        ;;
    5)
        echo ""
        echo "Current location: $(pwd)"
        echo "Home: $HOME_DIR"
        echo "Scripts: $SCRIPTS_DIR"
        echo "Logs: $LOG_DIR"
        ;;
    6)
        echo ""
        echo -n "  ➤ File to view: "
        read fname   
        if [ -f "$fname" ]; then
            echo ""
            echo "Content of: $fname"
            echo "────────────────────────────────"
            cat "$fname"
            echo "────────────────────────────────"
        elif [ -f "$SCRIPTS_DIR/$fname" ]; then
            echo ""
            echo "Content of: $SCRIPTS_DIR/$fname"
            echo "────────────────────────────────"
            cat "$SCRIPTS_DIR/$fname"
            echo "────────────────────────────────"
        else
            echo "  ❌ File not found"
        fi
        ;;
    7)
        echo ""
        echo "Recent activity:"
        echo "────────────────────────────────"
        tail -10 "$LOG_DIR/session.log" 2>/dev/null || echo "  (no activity yet)"
        echo "────────────────────────────────"
        ;;
    8)
        echo ""
        echo -n "  ➤ New project name: "
        read new_name
        if [ ! -z "$new_name" ]; then
            echo "$new_name" > .project_name
            echo "  ✅ Project renamed: $new_name"
        fi
        ;;
    9)
        echo ""
        echo "Generating session report..."
        generate_report
        ;;
    0)
        echo ""
        echo "Saving session..."
        generate_report
        echo "See you next time!"
        exit 0
        ;;
    *)
        echo ""
        echo "Please choose 0-9"
        ;;
esac

echo ""
echo -n "Press Enter to continue..."
read
exec "$0"  # Restart the interface