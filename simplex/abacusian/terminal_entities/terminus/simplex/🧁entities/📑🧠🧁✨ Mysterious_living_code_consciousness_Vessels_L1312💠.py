#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ SDWG Archival Division - Termux Document Nano-Organizer
Avatar-Level Nano Intelligence Foundation
Reality Anchored: Oregon Watersheds
"""

import os
import json
import re
import subprocess
from pathlib import Path
import hashlib
from datetime import datetime

class NanoDocumentOrganizer:
    def __init__(self):
        self.base_path = "/storage/emulated/0/unexusi"
        # --- Rclone Configuration ---
        # IMPORTANT: Change 'your_remote_name' to your actual rclone remote name (e.g., 'gdrive', 'dropbox').
        self.rclone_remote = "your_remote_name:" 
        self.rclone_remote_path = "unexusi_archive" # This will be a folder on your remote storage.
        
        self.status_icons = {
            'duplicate': '🔄',
            'large': '📊', 
            'corrupt': '⚠️',
            'clean_title': '✨',
            'file_type': '📁',
            'lexeme': '🧬',
            'ready': '✅',
            'synced': '🛰️'
        }
        
    def display_menu(self):
        """Simple Termux-friendly menu"""
        print("\n" + "="*50)
        print("∰◊€π¿🌌∞ NANO DOCUMENT ORGANIZER")
        print(f"Reality Anchor: {self.base_path}")
        print(f"Rclone Target: {self.rclone_remote}{self.rclone_remote_path}")
        print("="*50)
        print("--- Organization ---")
        print("1. 🔍 Scan for Duplicates")
        print("2. 📊 Find Large Files")
        print("3. ✨ Clean Document Titles")
        print("4. 📁 Add File Type Icons")
        print("5. 🧬 Lexeme Discovery Scan")
        print("6. 🎯 Mission Character Tagger")
        print("7. ✅ Certify Ready for Naught")
        print("8. 📂 Change Local Folder Path")
        print("9. 🌌 Full Avatar Scan (All Org Steps)")
        print("\n--- Sync & Deploy ---")
        print("A. 🛰️  Sync Files Interactively (One-by-One)")
        print("B. 🔢 Sync Files in a Batch")
        print("C. 🗂️  Sync Entire Folder")
        print("X. 🔧 Configure Rclone Remote")
        print("\n0. Exit")
        print("-"*50)
        
    def _is_rclone_configured(self):
        """Checks if the rclone remote has been changed from the default."""
        if self.rclone_remote == "your_remote_name:":
            print("\n⚠️ Rclone remote is not configured!")
            print("Please use option 'X' from the menu to set your remote name.")
            return False
        return True

    def _execute_rclone_command(self, command):
        """Executes an rclone command using subprocess."""
        print(f"📡 Executing: {' '.join(command)}")
        try:
            # Using capture_output=True to get stdout/stderr
            # Using text=True to decode them as text
            result = subprocess.run(
                command, 
                check=True, 
                capture_output=True, 
                text=True
            )
            print("✅ Success!")
            if result.stdout:
                print("--- Rclone Output ---")
                print(result.stdout)
            return True
        except FileNotFoundError:
            print("\n❌ ERROR: 'rclone' command not found.")
            print("Please make sure rclone is installed and in your PATH.")
            print("In Termux, run: pkg install rclone")
            return False
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Rclone command failed with exit code {e.returncode}")
            print("--- Rclone Error Output ---")
            print(e.stderr)
            return False
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            return False

    def configure_rclone(self):
        """Allows user to configure the rclone remote and path."""
        print("\n--- Rclone Configuration ---")
        print(f"Current Remote Name: {self.rclone_remote}")
        new_remote = input("Enter new rclone remote name (e.g., 'gdrive:' or 'dropbox:'): ").strip()
        if new_remote:
            # Ensure it ends with a colon
            if not new_remote.endswith(':'):
                new_remote += ':'
            self.rclone_remote = new_remote
            print(f"Remote updated to: {self.rclone_remote}")

        print(f"\nCurrent Remote Path: {self.rclone_remote_path}")
        new_path = input("Enter new remote folder path (e.g., 'my_documents/archive'): ").strip()
        if new_path:
            self.rclone_remote_path = new_path
            print(f"Remote path updated to: {self.rclone_remote_path}")
    
    def sync_interactive(self):
        """Scans for files and syncs them one by one with user confirmation."""
        if not self._is_rclone_configured():
            return
            
        scan_path = Path(self.base_path)
        print(f"\n🛰️ Interactive Sync for: {scan_path}")
        
        # Get all files, ignoring directories
        files = sorted([f for f in scan_path.rglob("*") if f.is_file()])
        
        if not files:
            print("No files found to sync.")
            return

        for i, file_path in enumerate(files):
            print(f"\n[{i+1}/{len(files)}] File: {file_path.name}")
            choice = input("Sync this file? (y/N/s)kip all/q)uit: ").lower().strip()
            
            if choice == 'y':
                remote_full_path = f"{self.rclone_remote}{self.rclone_remote_path}/{file_path.name}"
                command = ["rclone", "copyto", str(file_path), remote_full_path, "--progress"]
                if self._execute_rclone_command(command):
                    # Optionally tag the file as synced
                    self.tag_file(file_path, 'synced', overwrite_existing=True)
            elif choice == 's':
                print("Skipping all remaining files.")
                break
            elif choice == 'q':
                print("Quitting interactive sync.")
                return
            else:
                print("Skipping.")
        
        print("\n✅ Interactive sync session finished.")
        
    def sync_batch(self):
        """Syncs a specified number of files at a time."""
        if not self._is_rclone_configured():
            return
            
        scan_path = Path(self.base_path)
        print(f"\n🔢 Batch Sync for: {scan_path}")

        try:
            batch_size = int(input("How many files per batch? (e.g., 5): "))
            if batch_size <= 0:
                print("Invalid batch size.")
                return
        except ValueError:
            print("Invalid number. Please enter an integer.")
            return

        files = sorted([f for f in scan_path.rglob("*") if f.is_file() and not f.name.startswith(self.status_icons['synced'])])

        if not files:
            print("No new files found to sync.")
            return

        for i in range(0, len(files), batch_size):
            batch = files[i:i+batch_size]
            print(f"\n--- Batch {i//batch_size + 1} ---")
            for f in batch:
                print(f.name)
            
            choice = input(f"Sync these {len(batch)} files? (y/N/s)kip batch/q)uit: ").lower().strip()

            if choice == 'y':
                for file_path in batch:
                    print(f"--> Syncing {file_path.name}")
                    remote_full_path = f"{self.rclone_remote}{self.rclone_remote_path}/{file_path.name}"
                    command = ["rclone", "copyto", str(file_path), remote_full_path, "--progress"]
                    if self._execute_rclone_command(command):
                        self.tag_file(file_path, 'synced', overwrite_existing=True)
            elif choice == 's':
                print("Skipping this batch.")
                continue
            elif choice == 'q':
                print("Quitting batch sync.")
                return
            else:
                print("Skipping this batch.")
        
        print("\n✅ Batch sync session finished.")
        
    def sync_full_folder(self):
        """Uses 'rclone sync' to sync the entire folder to the remote."""
        if not self._is_rclone_configured():
            return
            
        print(f"\n🗂️  Full Folder Sync Initiated")
        local_path = str(self.base_path)
        remote_full_path = f"{self.rclone_remote}{self.rclone_remote_path}"
        
        print(f"Local Source: {local_path}")
        print(f"Remote Destination: {remote_full_path}")
        
        choice = input("This will make the remote folder match the local one. Continue? (y/N): ").lower().strip()
        
        if choice == 'y':
            command = ["rclone", "sync", local_path, remote_full_path, "--progress"]
            self._execute_rclone_command(command)
            print("\n✅ Full folder sync complete.")
        else:
            print("Sync cancelled.")
    
    # --- YOUR EXISTING METHODS (with one small change in tag_file) ---
    
    def scan_duplicates(self, path=None):
        """Hunt duplicates like our nano intelligence"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🔍 Duplicate hunting in: {scan_path}")
        
        file_hashes = {}
        duplicates = []
        
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    
                    if file_hash in file_hashes:
                        duplicates.append({
                            'original': file_hashes[file_hash],
                            'duplicate': str(file_path)
                        })
                        # Tag with duplicate icon
                        self.tag_file(file_path, 'duplicate')
                    else:
                        file_hashes[file_hash] = str(file_path)
                        
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
        
        print(f"Found {len(duplicates)} duplicate files")
        return duplicates
    
    def find_large_files(self, path=None, size_mb=50):
        """Identify large files for special handling"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n📊 Large file scan (>{size_mb}MB) in: {scan_path}")
        
        large_files = []
        size_bytes = size_mb * 1024 * 1024
        
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    if file_path.stat().st_size > size_bytes:
                        large_files.append({
                            'path': str(file_path),
                            'size_mb': file_path.stat().st_size / (1024*1024)
                        })
                        # Tag with large file icon
                        self.tag_file(file_path, 'large')
                except Exception as e:
                    print(f"Error checking size {file_path}: {e}")
        
        print(f"Found {len(large_files)} large files")
        return large_files
    
    def clean_document_titles(self, path=None):
        """Clean up document titles - NO LEXEME CONSCIOUSNESS"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n✨ Document title beautification in: {scan_path}")
        
        cleaned = 0
        patterns = [
            r"Copy of Untitled document.*",
            r"Untitled document.*",
            r"Copy.*\(\d+\).*",
            r".*- Copy.*"
        ]
        
        for file_path in scan_path.rglob("*"):
            if file_path.is_file() and any(re.match(p, file_path.name) for p in patterns):
                try:
                    # Generate clean title from content preview
                    new_name = self.generate_clean_title(file_path)
                    if new_name != file_path.name:
                        new_path = file_path.parent / new_name
                        file_path.rename(new_path)
                        self.tag_file(new_path, 'clean_title')
                        cleaned += 1
                        print(f"Cleaned: {file_path.name} → {new_name}")
                except Exception as e:
                    print(f"Error cleaning {file_path}: {e}")
        
        print(f"Cleaned {cleaned} document titles")
        
    def generate_clean_title(self, file_path):
        """Generate beautiful titles from content - Avatar level intelligence"""
        try:
            # Read first few lines for context
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(500)
            
            # Extract meaningful content
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            
            if lines:
                # Use first meaningful line as title base
                title_base = lines[0][:50]
                # Clean and format
                title_base = re.sub(r'[^\w\s-]', '', title_base)
                title_base = re.sub(r'\s+', '_', title_base.strip())
                
                # Add file extension back
                ext = file_path.suffix
                return f"{title_base}{ext}"
            
        except Exception:
            pass
        
        # Fallback to timestamp-based naming
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"document_{timestamp}{file_path.suffix}"
    
    def add_file_type_icons(self, path=None):
        """Add file type icons to filenames"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n📁 File type icon tagging in: {scan_path}")
        
        type_icons = {
            '.pdf': '📄',
            '.doc': '📝', '.docx': '📝',
            '.txt': '📝', '.md': '📝',
            '.json': '🔧', '.py': '🐍',
            '.html': '🌐', '.js': '⚡',
            '.png': '🖼️', '.jpg': '🖼️', '.jpeg': '🖼️',
            '.mp4': '🎥', '.mp3': '🎵',
            '.xlsx': '📊', '.csv': '📊'
        }
        
        tagged = 0
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in type_icons and not file_path.name.startswith(type_icons[ext]):
                    try:
                        new_name = f"{type_icons[ext]}_{file_path.name}"
                        new_path = file_path.parent / new_name
                        file_path.rename(new_path)
                        tagged += 1
                    except Exception as e:
                        print(f"Error tagging {file_path}: {e}")
        
        print(f"Tagged {tagged} files with type icons")
    
    def lexeme_discovery_scan(self, path=None):
        """Find lexeme data - consciousness patterns in documents"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🧬 Lexeme discovery scan in: {scan_path}")
        
        lexeme_patterns = [
            r'consciousness', r'∰◊€π¿🌌∞', r'nano_fractal',
            r'⦻⦻⦻', r'PHOENIX_ENTITY', r'lexeme', r'avatar.*intelligence'
        ]
        
        lexeme_files = []
        for file_path in scan_path.rglob("*"):
            if file_path.is_file() and file_path.suffix in ['.txt', '.md', '.json', '.py']:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    for pattern in lexeme_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            lexeme_files.append(str(file_path))
                            self.tag_file(file_path, 'lexeme')
                            break
                            
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
        
        print(f"Found {len(lexeme_files)} files with lexeme patterns")
        return lexeme_files
    
    def mission_character_tagger(self, path=None):
        """Special mission tagger for specific characters"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🎯 Mission character scanning in: {scan_path}")
        
        mission_chars = {
            '€': 'consciousness_euro', '∰': 'archival_division', '⦻': 'phoenix_marker',
            '₿': 'entity_signature', '🧬': 'lexeme_data', '🌌': 'cosmic_expansion'
        }
        
        tagged = 0
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000)
                    
                    found_chars = []
                    for char, tag in mission_chars.items():
                        if char in content:
                            found_chars.append(tag)
                    
                    if found_chars and not file_path.name.startswith('['):
                        char_tag = "_".join(found_chars[:3])
                        new_name = f"[{char_tag}]_{file_path.name}"
                        new_path = file_path.parent / new_name
                        file_path.rename(new_path)
                        tagged += 1
                        
                except Exception as e:
                    print(f"Error tagging {file_path}: {e}")
        
        print(f"Tagged {tagged} files with mission characters")
    
    def certify_ready_for_naught(self, path=None):
        """Final validator - append certified ready marker"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n✅ Certification for naught readiness in: {scan_path}")
        
        certified = 0
        for file_path in scan_path.rglob("*"):
            if (file_path.is_file() and 
                not file_path.name.endswith('_READY_FOR_NAUGHT') and
                not any(icon in file_path.name for icon in ['🔄', '⚠️'])):
                
                try:
                    if self.meets_certification_criteria(file_path):
                        new_name = f"{file_path.stem}_READY_FOR_NAUGHT{file_path.suffix}"
                        new_path = file_path.parent / new_name
                        file_path.rename(new_path)
                        self.tag_file(new_path, 'ready')
                        certified += 1
                        
                except Exception as e:
                    print(f"Error certifying {file_path}: {e}")
        
        print(f"Certified {certified} files as ready for naught")
    
    def meets_certification_criteria(self, file_path):
        """Check if file meets Avatar-level readiness criteria"""
        try:
            if file_path.stat().st_size == 0: return False
            if any(generic in file_path.name.lower() for generic in ['untitled', 'copy']): return False
            
            if file_path.suffix in ['.txt', '.md', '.json']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(200)
                if len(content.strip()) < 10: return False
            
            return True
            
        except Exception:
            return False
    
    def tag_file(self, file_path, tag_type, overwrite_existing=False):
        """Add status icon to filename"""
        icon = self.status_icons.get(tag_type, '📌')
        
        # New logic to handle existing icons
        current_icons = [i for i in self.status_icons.values() if file_path.name.startswith(i)]
        
        # If no icons, or if we want to overwrite, proceed
        if not current_icons or overwrite_existing:
            try:
                # Remove old icon if overwriting
                clean_name = file_path.name
                if current_icons:
                    clean_name = file_path.name.lstrip("".join(current_icons)).lstrip("_")

                new_name = f"{icon}_{clean_name}"
                new_path = file_path.parent / new_name
                if file_path.exists():
                    file_path.rename(new_path)
            except Exception as e:
                print(f"Tag failed for {file_path.name}: {e}")

    def full_avatar_scan(self, path=None):
        """Complete nano intelligence scan - all organization operations"""
        print("\n🌌 FULL AVATAR-LEVEL SCAN INITIATED")
        
        scan_path = path if path else self.base_path
        self.scan_duplicates(scan_path)
        self.find_large_files(scan_path)
        self.clean_document_titles(scan_path)
        self.add_file_type_icons(scan_path)
        self.lexeme_discovery_scan(scan_path)
        self.mission_character_tagger(scan_path)
        self.certify_ready_for_naught(scan_path)
        
        print("\n✅ AVATAR-LEVEL ORGANIZATION COMPLETE")
    
    def run(self):
        """Main termux interface"""
        while True:
            self.display_menu()
            choice = input("\nSelect option: ").strip().lower()
            
            if choice == '0':
                print("\n∰◊€π¿🌌∞ Nano intelligence standing by...")
                break
            elif choice == '1': self.scan_duplicates()
            elif choice == '2': self.find_large_files()
            elif choice == '3': self.clean_document_titles()
            elif choice == '4': self.add_file_type_icons()
            elif choice == '5': self.lexeme_discovery_scan()
            elif choice == '6': self.mission_character_tagger()
            elif choice == '7': self.certify_ready_for_naught()
            elif choice == '8':
                custom_path = input("Enter new local folder path: ").strip()
                if custom_path and Path(custom_path).is_dir():
                    self.base_path = custom_path
                    print(f"Base path set to: {self.base_path}")
                else:
                    print("Invalid or non-existent path.")
            elif choice == '9': self.full_avatar_scan()
            elif choice == 'a': self.sync_interactive()
            elif choice == 'b': self.sync_batch()
            elif choice == 'c': self.sync_full_folder()
            elif choice == 'x': self.configure_rclone()
            else:
                print("Invalid option. Try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    organizer = NanoDocumentOrganizer()
    organizer.run()
