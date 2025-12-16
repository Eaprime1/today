📜 launch.sh

#!/data/data/com.termux/files/usr/bin/bash

cd "$(dirname "$0")"
echo "🧠 Welcome to Terminal Automation"
echo "📁 Current folder: $(pwd)"
echo
echo "Select a script to run:"
echo "1) Sync Google Drive"
echo "2) List Scripts"
echo "3) Run custom script"
echo "4) Show folder tree"
echo "5) Exit"

read -p "🧩 Your choice: " choice

case $choice in
  1)
    bash pull_drive.sh
    ;;
  2)
    echo "📜 Available scripts:"
    ls scripts/
    ;;
  3)
    echo "🔧 Enter script name (without .sh):"
    read script
    bash "scripts/$script.sh"
    ;;
  4)
    echo "🌲 Directory Tree:"
    find . -type d
    ;;
  5)
    echo "👋 Goodbye!"
    exit 0
    ;;
  *)
    echo "❌ Invalid option"
    ;;
esac
