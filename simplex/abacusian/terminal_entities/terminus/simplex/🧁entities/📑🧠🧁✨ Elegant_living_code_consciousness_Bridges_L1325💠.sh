#!/data/data/com.termux/files/usr/bin/bash

# Colors & Emoji
GREEN='\033[0;32m'
NC='\033[0m'

echo "🔁 ${GREEN}Syncing from Google Drive...${NC}"

rclone sync gdrive_terminal: /storage/emulated/0/terminal
rclone sync gdrive_que: /storage/emulated/0/terminal/que_terminal

echo "✅ ${GREEN}Sync complete!${NC}"
date >> logs/sync.log