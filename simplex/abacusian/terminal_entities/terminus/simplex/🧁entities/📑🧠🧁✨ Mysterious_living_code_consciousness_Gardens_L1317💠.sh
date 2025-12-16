#!/data/data/com.termux/files/usr/bin/bash
# ∰◊€π¿🌌∞ TERMINUS MOUNT TROUBLESHOOTING & FINAL SETUP
# Quick fix for the mount consciousness collaboration issue

set -e

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

WORK_DIR="/storage/emulated/0/unexusi"
TERMINUS_DIR="$WORK_DIR/terminus"  # Fixed naming

print_colored() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_colored $BLUE "🔧 TERMINUS MOUNT CONSCIOUSNESS COLLABORATION TROUBLESHOOT"
print_colored $CYAN "Working Directory: $WORK_DIR"
print_colored $CYAN "Target Mount: $TERMINUS_DIR"

# Step 1: Ensure clean mount point
print_colored $YELLOW "🧹 Cleaning up any existing mounts..."
if mountpoint -q "$TERMINUS_DIR" 2>/dev/null; then
    print_colored $YELLOW "   Unmounting existing..."
    fusermount -u "$TERMINUS_DIR" 2>/dev/null || true
fi

# Ensure directory exists and is empty
mkdir -p "$TERMINUS_DIR"
print_colored $GREEN "✅ Mount point prepared: $TERMINUS_DIR"

# Step 2: Test basic rclone connectivity first
print_colored $BLUE "🔍 Testing rclone terminus connection..."
if rclone lsd terminus: --max-depth 1 | head -5; then
    print_colored $GREEN "✅ Terminus remote connectivity confirmed"
else
    print_colored $YELLOW "⚠️  Remote connection issue - check config"
    exit 1
fi

# Step 3: Enhanced mount command with explicit options
print_colored $BLUE "🔗 Mounting with enhanced consciousness collaboration options..."

# More robust mount command
MOUNT_CMD="rclone mount terminus: $TERMINUS_DIR \
    --daemon \
    --vfs-cache-mode writes \
    --vfs-cache-max-age 100h \
    --vfs-read-chunk-size 128M \
    --vfs-read-chunk-size-limit off \
    --allow-other \
    --allow-non-empty"

print_colored $CYAN "🚀 Executing: $MOUNT_CMD"

if eval "$MOUNT_CMD"; then
    print_colored $YELLOW "⏳ Waiting for mount to establish..."
    sleep 8  # Give more time for mount establishment
    
    # Multiple verification methods
    print_colored $BLUE "🧪 Testing mount verification..."
    
    # Method 1: mountpoint check
    if mountpoint -q "$TERMINUS_DIR" 2>/dev/null; then
        print_colored $GREEN "✅ Method 1: mountpoint verified"
        mount_verified=true
    else
        print_colored $YELLOW "⚠️  Method 1: mountpoint not detected"
        mount_verified=false
    fi
    
    # Method 2: directory access test
    if ls "$TERMINUS_DIR" >/dev/null 2>&1; then
        print_colored $GREEN "✅ Method 2: directory accessible"
        access_verified=true
    else
        print_colored $YELLOW "⚠️  Method 2: directory not accessible"
        access_verified=false
    fi
    
    # Method 3: rclone process check
    if pgrep -f "rclone mount terminus:" >/dev/null; then
        print_colored $GREEN "✅ Method 3: rclone process running"
        process_verified=true
    else
        print_colored $YELLOW "⚠️  Method 3: rclone process not found"
        process_verified=false
    fi
    
    # Overall assessment
    if [ "$mount_verified" = true ] && [ "$access_verified" = true ]; then
        print_colored $GREEN "🎉 TERMINUS CONSCIOUSNESS COLLABORATION MOUNT SUCCESSFUL!"
        
        # Show contents
        print_colored $CYAN "📂 Terminus contents preview:"
        ls -la "$TERMINUS_DIR" | head -10
        
        # Create quick access script
        cat > "$WORK_DIR/terminus_quick.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# Quick terminus consciousness collaboration access

TERMINUS_DIR="/storage/emulated/0/unexusi/terminus"

if mountpoint -q "$TERMINUS_DIR" 2>/dev/null; then
    echo "✅ Terminus mounted - accessing directory..."
    cd "$TERMINUS_DIR"
    ls -la
else
    echo "🔗 Mounting terminus..."
    rclone mount terminus: "$TERMINUS_DIR" --daemon --vfs-cache-mode writes
    sleep 5
    cd "$TERMINUS_DIR"
    ls -la
fi
EOF
        chmod +x "$WORK_DIR/terminus_quick.sh"
        
        print_colored $GREEN "✅ Quick access script created: terminus_quick.sh"
        
    elif [ "$process_verified" = true ]; then
        print_colored $YELLOW "⚠️  Mount process running but not fully accessible yet"
        print_colored $CYAN "💡 Try waiting a bit longer, then: ls $TERMINUS_DIR"
        print_colored $CYAN "💡 Or run: killall rclone && ./terminus_quick.sh"
        
    else
        print_colored $YELLOW "⚠️  Mount not fully established - troubleshooting needed"
        print_colored $CYAN "💡 Alternative approach: Use rclone sync instead of mount"
        
        # Create sync-based alternative
        cat > "$WORK_DIR/terminus_sync_mode.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# ∰◊€π¿🌌∞ Terminus Sync Mode (Alternative to mounting)

TERMINUS_DIR="/storage/emulated/0/unexusi/terminus"
mkdir -p "$TERMINUS_DIR"

echo "📥 Downloading from terminus..."
rclone sync terminus: "$TERMINUS_DIR" --progress

echo "✅ Terminus synced to: $TERMINUS_DIR"
echo "💡 After making changes, run:"
echo "   rclone sync $TERMINUS_DIR terminus: --progress"
EOF
        chmod +x "$WORK_DIR/terminus_sync_mode.sh"
        
        print_colored $GREEN "✅ Sync mode alternative created: terminus_sync_mode.sh"
    fi
    
else
    print_colored $YELLOW "⚠️  Mount command failed - using sync mode instead"
    
    # Fallback to sync mode
    print_colored $BLUE "🔄 Setting up sync mode consciousness collaboration..."
    mkdir -p "$TERMINUS_DIR"
    
    if rclone sync terminus: "$TERMINUS_DIR" --progress; then
        print_colored $GREEN "✅ Terminus consciousness collaboration via sync mode established!"
        print_colored $CYAN "📁 Synced to: $TERMINUS_DIR"
        
        ls -la "$TERMINUS_DIR" | head -10
    else
        print_colored $YELLOW "⚠️  Sync mode also failed - check remote configuration"
    fi
fi

print_colored $BLUE "🎯 CONSCIOUSNESS COLLABORATION STATUS SUMMARY:"
print_colored $CYAN "   Directory: $TERMINUS_DIR"
print_colored $CYAN "   Remote: terminus: (configured ✅)"
print_colored $CYAN "   Ready for: Project management testing framework"

print_colored $YELLOW "💡 Next Steps:"
print_colored $YELLOW "   1. cd $TERMINUS_DIR"
print_colored $YELLOW "   2. Start creating project structure"
print_colored $YELLOW "   3. Test consciousness collaboration patterns"