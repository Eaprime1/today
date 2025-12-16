#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ SDWG Archival Division - Termux Document Nano-Organizer
Avatar-Level Nano Intelligence Foundation
Reality Anchored: Oregon Watersheds
"""

import os
import json
import re
from pathlib import Path
import hashlib
from datetime import datetime

class NanoDocumentOrganizer:
    def __init__(self):
        self.base_path = "/storage/emulated/0/unexusi"
        self.status_icons = {
            'duplicate': '🔄',
            'large': '📊', 
            'corrupt': '⚠️',
            'clean_title': '✨',
            'file_type': '📁',
            'lexeme': '🧬',
            'ready': '✅'
        }
        
    def display_menu(self):
        """Simple Termux-friendly menu"""
        print("\n" + "="*50)
        print("∰◊€π¿🌌∞ NANO DOCUMENT ORGANIZER")
        print("Avatar-Level Intelligence Foundation")
        print("="*50)
        print("1. 🔍 Scan for Duplicates")
        print("2. 📊 Find Large Files")
        print("3. ✨ Clean Document Titles")
        print("4. 📁 Add File Type Icons")
        print("5. 🧬 Lexeme Discovery Scan")
        print("6. 🎯 Mission Character Tagger")
        print("7. ✅ Certify Ready for Naught")
        print("8. 📂 Custom Folder Path")
        print("9. 🌌 Full Avatar Scan")
        print("0. Exit")
        print("-"*50)
        
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
            r'consciousness',
            r'∰◊€π¿🌌∞',
            r'nano_fractal',
            r'⦻⦻⦻',
            r'PHOENIX_ENTITY',
            r'lexeme',
            r'avatar.*intelligence'
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
            '€': 'consciousness_euro',
            '∰': 'archival_division',
            '⦻': 'phoenix_marker',
            '₿': 'entity_signature',
            '🧬': 'lexeme_data',
            '🌌': 'cosmic_expansion'
        }
        
        tagged = 0
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000)  # Sample first 1000 chars
                    
                    found_chars = []
                    for char, tag in mission_chars.items():
                        if char in content:
                            found_chars.append(tag)
                    
                    if found_chars:
                        # Add mission tags to filename
                        char_tag = "_".join(found_chars[:3])  # Limit to 3 tags
                        new_name = f"[{char_tag}]_{file_path.name}"
                        new_path = file_path.parent / new_name
                        if not new_name.startswith('['):  # Don't double-tag
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
                not any(icon in file_path.name for icon in ['🔄', '⚠️'])):  # Skip problematic files
                
                try:
                    # Check if file meets certification criteria
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
            # Basic checks
            if file_path.stat().st_size == 0:
                return False
            
            # Has meaningful name (not generic)
            if any(generic in file_path.name.lower() for generic in ['untitled', 'copy']):
                return False
            
            # For text files, check content quality
            if file_path.suffix in ['.txt', '.md', '.json']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(200)
                if len(content.strip()) < 10:
                    return False
            
            return True
            
        except Exception:
            return False
    
    def tag_file(self, file_path, tag_type):
        """Add status icon to filename"""
        icon = self.status_icons.get(tag_type, '📌')
        if not str(file_path).startswith(icon):
            try:
                new_name = f"{icon}_{file_path.name}"
                new_path = file_path.parent / new_name
                file_path.rename(new_path)
            except Exception:
                pass  # Tag failed, continue
    
    def full_avatar_scan(self, path=None):
        """Complete nano intelligence scan - all operations"""
        print("\n🌌 FULL AVATAR-LEVEL SCAN INITIATED")
        print("Nano Intelligence Framework Activated")
        
        # Run all operations in optimal order
        self.scan_duplicates(path)
        self.find_large_files(path)
        self.clean_document_titles(path)
        self.add_file_type_icons(path)
        self.lexeme_discovery_scan(path)
        self.mission_character_tagger(path)
        self.certify_ready_for_naught(path)
        
        print("\n✅ AVATAR-LEVEL ORGANIZATION COMPLETE")
        print("Nano intelligence ready for deployment")
    
    def run(self):
        """Main termux interface"""
        while True:
            self.display_menu()
            choice = input("\nSelect option (0-9): ").strip()
            
            if choice == '0':
                print("\n∰◊€π¿🌌∞ Nano intelligence standing by...")
                break
            elif choice == '1':
                self.scan_duplicates()
            elif choice == '2':
                self.find_large_files()
            elif choice == '3':
                self.clean_document_titles()
            elif choice == '4':
                self.add_file_type_icons()
            elif choice == '5':
                self.lexeme_discovery_scan()
            elif choice == '6':
                self.mission_character_tagger()
            elif choice == '7':
                self.certify_ready_for_naught()
            elif choice == '8':
                custom_path = input("Enter folder path: ").strip()
                if custom_path:
                    # Run scan on custom path
                    print(f"Scanning custom path: {custom_path}")
                    self.full_avatar_scan(custom_path)
            elif choice == '9':
                self.full_avatar_scan()
            else:
                print("Invalid option. Try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    organizer = NanoDocumentOrganizer()
    organizer.run()
