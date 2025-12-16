#!/data/data/com.termux/files/usr/bin/bash
# ∰◊€π¿🌌∞ GOOGLE DRIVE FOLDER ACCESS DEBUG & FIX
# Consciousness Collaboration Framework - Troubleshooting folder access

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

print_colored() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_colored $BLUE "🔧 GOOGLE DRIVE FOLDER ACCESS CONSCIOUSNESS COLLABORATION DEBUG"
print_colored $CYAN "=============================================================="
echo ""

# Test 1: Check rclone remotes and basic connectivity
print_colored $YELLOW "🔍 Test 1: Checking rclone remote connectivity..."
echo ""

print_colored $CYAN "Available remotes:"
rclone listremotes

echo ""
print_colored $CYAN "Testing basic terminus remote access:"
if rclone lsd terminus: --max-depth 1 | head -10; then
    print_colored $GREEN "✅ Basic terminus remote access working"
else
    print_colored $RED "❌ Basic terminus remote access failed"
    exit 1
fi

echo ""
print_colored $YELLOW "🔍 Test 2: Different folder access methods..."

# Test 2: Try different ways to access the folder
FOLDER_ID="1AQxd2QcAPqqz_phUvinTy1OSCnQ298A-"

print_colored $CYAN "Method 1: Direct folder ID access"
echo "Command: rclone lsd terminus:$FOLDER_ID"
if rclone lsd "terminus:$FOLDER_ID" --max-depth 1 2>/dev/null; then
    print_colored $GREEN "✅ Direct folder ID access works"
    WORKING_METHOD="direct_id"
else
    print_colored $YELLOW "⚠️  Direct folder ID access failed"
fi

echo ""
print_colored $CYAN "Method 2: Root directory listing to find folder"
echo "Command: rclone lsd terminus: | grep -i project"
echo "Looking for folders containing 'project'..."
FOLDER_SEARCH=$(rclone lsd terminus: 2>/dev/null | grep -i project || echo "No folders found with 'project'")
echo "$FOLDER_SEARCH"

echo ""
print_colored $CYAN "Method 3: Search for specific folder name patterns"
echo "Command: rclone lsd terminus: | head -20"
print_colored $YELLOW "All top-level folders in your Drive:"
rclone lsd terminus: | head -20

echo ""
print_colored $YELLOW "🔍 Test 3: Alternative access patterns..."

# Test 3: Try to find the folder by name patterns
print_colored $CYAN "Searching for folders that might match your project..."
echo ""

# Look for any folders that might be the main project
ALL_FOLDERS=$(rclone lsd terminus: 2>/dev/null || echo "Failed to list")
echo "Top-level folders found:"
echo "$ALL_FOLDERS"

echo ""
print_colored $YELLOW "🔍 Test 4: Test access to unexusi development folder..."
UNEXUSI_FOLDER_ID="16JYYSoFsIfQf9UHUQW_tL2zrWhp7Awjd"

print_colored $CYAN "Testing unexusi folder access:"
echo "Command: rclone lsd terminus:$UNEXUSI_FOLDER_ID"
if rclone lsd "terminus:$UNEXUSI_FOLDER_ID" --max-depth 1 2>/dev/null; then
    print_colored $GREEN "✅ Unexusi folder access works"
    UNEXUSI_WORKING=true
else
    print_colored $YELLOW "⚠️  Unexusi folder access also failed"
    UNEXUSI_WORKING=false
fi

echo ""
print_colored $YELLOW "🔧 DIAGNOSIS AND SOLUTIONS"
print_colored $CYAN "=========================="
echo ""

print_colored $BLUE "💡 Likely Issues & Solutions:"
echo ""

print_colored $CYAN "1. FOLDER PERMISSIONS:"
echo "   - The folder might not be accessible by the rclone account"
echo "   - Solution: Ensure the Google account used for rclone has access"

echo ""
print_colored $CYAN "2. FOLDER ID METHOD:"
echo "   - rclone may need the folder to be accessed by full path, not ID"
echo "   - Solution: Find the folder by browsing from root"

echo ""
print_colored $CYAN "3. SHARED DRIVE vs PERSONAL DRIVE:"
echo "   - Folder might be in a Shared/Team Drive"
echo "   - Solution: Configure rclone for Team Drive access"

echo ""
print_colored $YELLOW "🔄 IMMEDIATE WORKAROUNDS:"
echo ""

print_colored $CYAN "Option 1: Browse and find the folder manually"
echo "   Run: rclone lsd terminus:"
echo "   Look for your project folder in the listing"
echo "   Use the folder name instead of ID"

echo ""
print_colored $CYAN "Option 2: Use recursive search"
echo "   Run: rclone lsf terminus: --recursive --dirs-only | grep -i project"
echo "   Find folders with 'project' in the name"

echo ""
print_colored $CYAN "Option 3: Create a test folder for verification"
echo "   Create a test folder in Google Drive"
echo "   Try accessing it with rclone to verify permissions"

echo ""
print_colored $YELLOW "🛠️  QUICK FIX SCRIPT GENERATION"
print_colored $CYAN "================================"
echo ""

# Generate a quick fix script based on what we found
cat > "/storage/emulated/0/unexusi/folder_access_fix.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# ∰◊€π¿🌌∞ Quick Folder Access Fix

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

print_colored() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_colored $CYAN "🔧 ALTERNATIVE FOLDER ACCESS METHODS"
echo ""

# Method 1: Browse mode
browse_mode() {
    print_colored $YELLOW "📁 BROWSE MODE: Find your folder manually"
    echo ""
    print_colored $CYAN "Listing all top-level folders:"
    rclone lsd terminus:
    echo ""
    print_colored $YELLOW "Copy the exact folder name and use it instead of ID"
    print_colored $YELLOW "Example: rclone sync 'terminus:Your Folder Name' /local/path"
}

# Method 2: Search mode  
search_mode() {
    print_colored $YELLOW "🔍 SEARCH MODE: Find folders by keyword"
    echo ""
    echo -n "Enter search keyword: "
    read -r keyword
    print_colored $CYAN "Searching for folders containing '$keyword':"
    rclone lsf terminus: --recursive --dirs-only | grep -i "$keyword" | head -10
}

# Method 3: Test sync with known working folder
test_sync() {
    print_colored $YELLOW "🧪 TEST SYNC: Try with a specific folder"
    echo ""
    echo -n "Enter folder name (from browse results): "
    read -r folder_name
    
    test_dir="/storage/emulated/0/unexusi/terminus/test_sync"
    mkdir -p "$test_dir"
    
    print_colored $CYAN "Testing sync with folder: $folder_name"
    if rclone sync "terminus:$folder_name" "$test_dir" --dry-run; then
        print_colored $GREEN "✅ Sync would work! Remove --dry-run to actually sync"
        echo "Full command: rclone sync 'terminus:$folder_name' '$test_dir'"
    else
        print_colored $YELLOW "⚠️  Still having issues with this folder"
    fi
}

echo "Select method:"
echo "1) Browse all folders"
echo "2) Search by keyword"  
echo "3) Test sync with specific folder"
echo -n "Choice (1-3): "
read -r choice

case $choice in
    1) browse_mode ;;
    2) search_mode ;;
    3) test_sync ;;
    *) echo "Invalid choice" ;;
esac
EOF

chmod +x "/storage/emulated/0/unexusi/folder_access_fix.sh"

print_colored $GREEN "✅ Quick fix script created: /storage/emulated/0/unexusi/folder_access_fix.sh"
echo ""

print_colored $YELLOW "🎯 NEXT STEPS:"
echo "1. Run the fix script: bash /storage/emulated/0/unexusi/folder_access_fix.sh"
echo "2. Use browse mode to see all available folders"
echo "3. Find your project folder by name instead of ID"
echo "4. Update the folder selector UI with working folder names"

echo ""
print_colored $CYAN "💡 Most likely solution: Use folder names instead of IDs"
print_colored $CYAN "   Example: 'terminus:Project Folder Name' instead of 'terminus:FOLDER_ID'"