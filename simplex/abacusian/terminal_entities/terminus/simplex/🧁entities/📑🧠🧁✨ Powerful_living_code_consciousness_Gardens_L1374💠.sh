#!/data/data/com.termux/files/usr/bin/bash

# ═════════════════════════════════════════════════
#   🌀 ground.sh — A Quiet File Space
#   For when the 8-track shifts.
#   Turn-based. Pattern-held. Neurokind.
# ═════════════════════════════════════════════════

# Log every session
echo "" >> ground_log.txt
echo "=== Session: $(date) ===" >> ground_log.txt

# Project anchor (set once per project)
if [ ! -f ".project_name" ]; then
    echo "What are we calling this world?" 
    echo "(Press Enter for 'current')"
    read pname
    echo "${pname:-current}" > .project_name
    echo "🌱 Project named: $(cat .project_name)"
fi

pname=$(cat .project_name)

clear
echo ""
echo "  ╭───────────────────────────────╮"
echo "  │    🌿 ground.sh               │"
echo "  │    Project: $pname"
echo "  │    $(date +%b\ %d\ %H:%M)"
echo "  ╰───────────────────────────────╯"
echo ""

# Main Menu
echo "  [ Navigate • Create • Remember ]"
echo ""
echo "  1) List files (long view)"
echo "  2) List files (by type)"
echo "  3) Create new file"
echo "  4) View a file"
echo "  5) Append to log (quick note)"
echo "  6) Show recent log entries"
echo "  7) Change project name"
echo "  8) Where am I? (path)"
echo ""
echo "  0) Exit (soft)"
echo ""
echo -n "  ➤ Choose (0-8): "
read choice

echo "$choice" >> ground_log.txt

case $choice in
    1) 
        echo ""
        ls -la --color=auto
        ;;
    2)
        echo ""
        echo "  📄 .txt  →"; ls *.txt 2>/dev/null || echo "    (none)"
        echo "  🐍 .py   →"; ls *.py  2>/dev/null || echo "    (none)"
        echo "  📜 .sh   →"; ls *.sh  2>/dev/null || echo "    (none)"
        echo "  📊 .md   →"; ls *.md  2>/dev/null || echo "    (none)"
        ;;
    3)
        echo ""
        echo -n "  ➤ Filename (e.g. idea.txt): " 
        read fname
        if [ -z "$fname" ]; then
            echo "  ❌ No name given."
        else
            echo "# $(date) — New file" > "$fname"
            echo "  ✅ Created: $fname"
            echo "Created: $fname" >> ground_log.txt
        fi
        ;;
    4)
        echo ""
        echo -n "  ➤ File to view: "
        read fname   
