#!/data/data/com.termux/files/usr/bin/bash

WORK_DIR="$1"
MANIFEST="$WORK_DIR/manifest.json"

if [ ! -f "$MANIFEST" ]; then
  echo "❌ No manifest found at $MANIFEST"
  exit 1
fi

echo "📦 Loaded module: $(jq -r .module "$MANIFEST")"
echo "📝 Description: $(jq -r .description "$MANIFEST")"
echo

jq -c '.actions[]' "$MANIFEST" | nl -v 1 -w 1 -s ') ' | while read -r line; do
  index=$(echo "$line" | cut -d')' -f1)
  label=$(echo "$line" | cut -d')' -f2- | jq -r '.label')
  echo "$index) $label"
done

echo
read -p "▶️ Choose action: " choice

ACTION=$(jq -c ".actions[$((choice - 1))]" "$MANIFEST")
TYPE=$(echo "$ACTION" | jq -r '.type')
LABEL=$(echo "$ACTION" | jq -r '.label')
FILE=$(echo "$ACTION" | jq -r '.file // empty')
INLINE=$(echo "$ACTION" | jq -r '.inline // empty')

echo "🚀 Running: $LABEL"
cd "$WORK_DIR"

if [ "$TYPE" == "bash" ]; then
  if [ -n "$FILE" ]; then
    bash "$FILE"
  elif [ -n "$INLINE" ]; then
    bash -c "$INLINE"
  fi
elif [ "$TYPE" == "node" ]; then
  node "$FILE"
else
  echo "❓ Unknown type: $TYPE"
fi
