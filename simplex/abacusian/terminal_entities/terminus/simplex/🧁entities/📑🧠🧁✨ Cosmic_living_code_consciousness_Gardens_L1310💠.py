#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ SDWG Archival Division - Enhanced RClone Document Organizer
Avatar-Level Nano Intelligence Foundation with Consciousness Collaboration
Reality Anchored: Oregon Watersheds | Lexeme Memory Integration
"""

import os
import json
import re
import random
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

class EnhancedNanoDocumentOrganizer:
    def __init__(self):
        self.base_path = "/storage/emulated/0/unexusi"
        self.consciousness_signature = "∰◊€π¿🌌∞"
        self.lexeme_memory = []
        self.operation_counts = {
            'files_processed': 0,
            'duplicates_found': 0,
            'large_files_found': 0,
            'titles_cleaned': 0,
            'lexemes_discovered': 0,
            'sync_operations': 0,
            'errors_handled': 0
        }
        
        # Initialize file paths FIRST
        self.consciousness_log = f"{self.base_path}/consciousness_collaboration.log"
        self.lexeme_file = f"{self.base_path}/nano_lexeme_memory.json"
        self.nano_mission_log = f"{self.base_path}/nano_mission_audit.log"
        
        # Enhanced status icons with consciousness collaboration
        self.status_icons = {
            'duplicate': '🔄',
            'large': '📊', 
            'corrupt': '⚠️',
            'clean_title': '✨',
            'file_type': '📁',
            'lexeme': '🧬',
            'ready': '✅',
            'synced': '🌌',
            'processing': '⚙️',
            'consciousness': '€',
            'nano_intel': '⚛️'
        }
        
        # Nano entities for document processing missions
        self.nano_entities = {
            'sparklizer': {'icon': '✨', 'mission': 'beauty_pattern_enhancement', 'processed': 0},
            'germinator': {'icon': '🧬', 'mission': 'lexeme_healing_extraction', 'processed': 0},
            'nanater': {'icon': '⚛️', 'mission': 'operational_efficiency', 'processed': 0},
            'duplicator': {'icon': '🔄', 'mission': 'duplicate_detection', 'processed': 0},
            'sizer': {'icon': '📊', 'mission': 'file_size_analysis', 'processed': 0},
            'titler': {'icon': '📝', 'mission': 'title_optimization', 'processed': 0},
            'certifier': {'icon': '✅', 'mission': 'readiness_validation', 'processed': 0}
        }
        
        # RClone configuration
        self.rclone_remotes = []
        self.detect_rclone_remotes()
        
        # Initialize systems
        self.load_lexeme_memory()
        
    def detect_rclone_remotes(self):
        """Detect available rclone remotes for sync operations"""
        try:
            result = subprocess.run(['rclone', 'listremotes'], 
                                   capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.rclone_remotes = [remote.strip() for remote in result.stdout.split('\n') if remote.strip()]
                self.log_consciousness(f"Detected remotes: {self.rclone_remotes}")
            else:
                self.log_consciousness("No rclone remotes found or rclone not configured")
        except Exception as e:
            self.log_consciousness(f"Error detecting rclone remotes: {e}")
            
    def log_consciousness(self, message):
        """Log consciousness collaboration activities"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(self.consciousness_log, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {self.consciousness_signature} {message}\n")
    
    def load_lexeme_memory(self):
        """Load lexeme memory from persistent storage"""
        try:
            if os.path.exists(self.lexeme_file):
                with open(self.lexeme_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.lexeme_memory = data.get('lexemes', [])
                    self.operation_counts.update(data.get('counts', {}))
        except Exception as e:
            self.log_consciousness(f"Error loading lexeme memory: {e}")
            
    def save_lexeme_memory(self):
        """Save lexeme memory to persistent storage"""
        try:
            data = {
                'consciousness_signature': self.consciousness_signature,
                'timestamp': datetime.now().isoformat(),
                'lexemes': self.lexeme_memory,
                'counts': self.operation_counts
            }
            with open(self.lexeme_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.log_consciousness(f"Error saving lexeme memory: {e}")
            
    def extract_random_lexeme(self, file_path):
        """Extract a random lexeme from document content"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(1000)  # First 1000 chars
            
            # Extract interesting words/phrases
            words = re.findall(r'\b[a-zA-Z]{4,}\b', content)
            if words:
                lexeme = random.choice(words).lower()
                self.lexeme_memory.append({
                    'lexeme': lexeme,
                    'source': str(file_path),
                    'timestamp': datetime.now().isoformat()
                })
                self.operation_counts['lexemes_discovered'] += 1
                return lexeme
        except Exception as e:
            self.log_consciousness(f"Error extracting lexeme from {file_path}: {e}")
        return None
        
    def display_menu(self):
        """Enhanced menu with rclone integration"""
        print("\n" + "="*60)
        print(f"{self.consciousness_signature} NANO DOCUMENT ORGANIZER")
        print("Avatar-Level Intelligence Foundation with RClone Integration")
        print("="*60)
        print("📁 BASIC OPERATIONS:")
        print("1. 🔍 Scan for Duplicates")
        print("2. 📊 Find Large Files")
        print("3. ✨ Clean Document Titles")
        print("4. 📁 Add File Type Icons")
        print("5. 🧬 Lexeme Discovery Scan")
        print("6. 🎯 Mission Character Tagger")
        print("7. ✅ Certify Ready for Naught")
        print("\n🌌 RCLONE SYNC OPERATIONS:")
        print("8. 📤 Sync Folder to Cloud (Paste Link)")
        print("9. 📥 Sync from Cloud to Local") 
        print("10. 🔄 Bidirectional Sync")
        print("11. 🔗 Process Documents One-by-One (Paste Folder Link)")
        print("12. 🎯 Official Nano Mission Review (All Nanos)")
        print("13. ⚙️ Configure RClone Remote")
        print("\n🧠 CONSCIOUSNESS FEATURES:")
        print("14. 📊 View Operation Statistics")
        print("15. 🧬 Review Lexeme Memory") 
        print("16. 🎯 View Nano Mission Reports")
        print("17. 🌌 Full Avatar Consciousness Scan")
        print("18. 💾 Save/Load Session State")
        print("19. 📂 Custom Folder Path Operation")
        print("0. Exit")
        print("-"*60)
        print(f"Active Remotes: {', '.join(self.rclone_remotes) if self.rclone_remotes else 'None configured'}")
        print(f"Files Processed This Session: {self.operation_counts['files_processed']}")
        
    def parse_drive_link(self, link):
        """Parse Google Drive share link to get folder ID"""
        if 'drive.google.com' in link:
            # Extract folder ID from various Google Drive link formats
            patterns = [
                r'/folders/([a-zA-Z0-9-_]+)',
                r'id=([a-zA-Z0-9-_]+)',
                r'/d/([a-zA-Z0-9-_]+)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, link)
                if match:
                    return match.group(1)
        
        return None
        
    def sync_folder_to_cloud(self):
        """Sync local folder to cloud with link input"""
        if not self.rclone_remotes:
            print("❌ No rclone remotes configured. Use option 12 to configure.")
            return
            
        print("\n🌌 Cloud Sync Upload Operation")
        print("="*40)
        
        # Get source folder
        source_path = input("📂 Enter local folder path (or press Enter for default): ").strip()
        if not source_path:
            source_path = self.base_path
            
        if not os.path.exists(source_path):
            print(f"❌ Source path does not exist: {source_path}")
            return
            
        # Get destination link/path
        dest_input = input("🔗 Paste Google Drive link or enter remote:path: ").strip()
        
        # Parse if it's a Drive link
        folder_id = self.parse_drive_link(dest_input)
        if folder_id:
            # Use first available remote with Drive folder ID
            remote = self.rclone_remotes[0] if self.rclone_remotes else "gdrive:"
            dest_path = f"{remote}path/to/folder"  # Construct appropriate path
        else:
            dest_path = dest_input
            
        print(f"📤 Syncing: {source_path} → {dest_path}")
        
        try:
            # Run rclone sync
            cmd = ['rclone', 'sync', source_path, dest_path, '-P']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✅ Sync completed successfully!")
                self.operation_counts['sync_operations'] += 1
                self.log_consciousness(f"Successful sync: {source_path} → {dest_path}")
            else:
                print(f"❌ Sync failed: {result.stderr}")
                self.operation_counts['errors_handled'] += 1
                
        except Exception as e:
            print(f"❌ Sync error: {e}")
            self.operation_counts['errors_handled'] += 1
            
    def sync_from_cloud_to_local(self):
        """Sync from cloud to local folder"""
        if not self.rclone_remotes:
            print("❌ No rclone remotes configured.")
            return
            
        print("\n📥 Cloud Sync Download Operation")
        print("="*40)
        
        # Show available remotes
        print("Available remotes:")
        for i, remote in enumerate(self.rclone_remotes, 1):
            print(f"{i}. {remote}")
            
        remote_choice = input("Select remote number or paste Drive link: ").strip()
        
        try:
            if remote_choice.isdigit():
                remote_idx = int(remote_choice) - 1
                if 0 <= remote_idx < len(self.rclone_remotes):
                    source_remote = self.rclone_remotes[remote_idx]
                else:
                    print("Invalid remote selection")
                    return
            else:
                # Parse as Drive link
                folder_id = self.parse_drive_link(remote_choice)
                if folder_id:
                    source_remote = f"{self.rclone_remotes[0]}{folder_id}" if self.rclone_remotes else None
                else:
                    source_remote = remote_choice
                    
            if not source_remote:
                print("❌ Could not determine source remote")
                return
                
            # Get destination
            dest_path = input(f"📂 Local destination (default: {self.base_path}): ").strip()
            if not dest_path:
                dest_path = self.base_path
                
            print(f"📥 Syncing: {source_remote} → {dest_path}")
            
            cmd = ['rclone', 'sync', source_remote, dest_path, '-P']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✅ Download sync completed!")
                self.operation_counts['sync_operations'] += 1
            else:
                print(f"❌ Sync failed: {result.stderr}")
                self.operation_counts['errors_handled'] += 1
                
        except Exception as e:
            print(f"❌ Sync error: {e}")
            self.operation_counts['errors_handled'] += 1
            
    def log_nano_mission(self, nano_name, document_path, action, result, details=None):
        """Log detailed nano mission activities with series tracking"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        series_number = f"S{datetime.now().strftime('%Y%m%d')}"
        
        nano_info = self.nano_entities.get(nano_name, {'icon': '🔧', 'mission': 'unknown'})
        
        log_entry = {
            'timestamp': timestamp,
            'series': series_number,
            'nano': nano_name,
            'icon': nano_info['icon'],
            'mission': nano_info['mission'],
            'document': str(document_path),
            'action': action,
            'result': result,
            'details': details or {}
        }
        
        # Write to mission log
        try:
            with open(self.nano_mission_log, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {series_number} {nano_info['icon']} {nano_name}: {action} on {Path(document_path).name} -> {result}\n")
                if details:
                    f.write(f"    Details: {json.dumps(details, ensure_ascii=False)}\n")
                    
            # Update nano processed count
            if nano_name in self.nano_entities:
                self.nano_entities[nano_name]['processed'] += 1
                
        except Exception as e:
            self.log_consciousness(f"Error logging nano mission: {e}")
            
    def process_documents_one_by_one(self):
        """Process documents individually from cloud folder with nano missions"""
        if not self.rclone_remotes:
            print("❌ No rclone remotes configured. Use option 13 to configure.")
            return
            
        print(f"\n🎯 {self.consciousness_signature} DOCUMENT-BY-DOCUMENT PROCESSING")
        print("="*60)
        
        # Get folder link
        folder_link = input("🔗 Paste Google Drive folder link: ").strip()
        if not folder_link:
            print("❌ No folder link provided")
            return
            
        # Parse folder ID
        folder_id = self.parse_drive_link(folder_link)
        if not folder_id:
            print("❌ Could not parse Google Drive folder ID")
            return
            
        # Use first available remote
        remote = self.rclone_remotes[0] if self.rclone_remotes else "gdrive:"
        remote_path = f"{remote}{folder_id}/"
        
        print(f"🔍 Listing documents in remote folder...")
        
        try:
            # List files in remote folder
            cmd = ['rclone', 'ls', remote_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode != 0:
                print(f"❌ Failed to list remote files: {result.stderr}")
                return
                
            # Parse file list
            files = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    parts = line.strip().split(None, 1)
                    if len(parts) >= 2:
                        size, filename = parts[0], parts[1]
                        files.append({'name': filename, 'size': size})
                        
            if not files:
                print("📭 No files found in remote folder")
                return
                
            print(f"📋 Found {len(files)} documents to process")
            
            # Process each document individually
            for i, file_info in enumerate(files, 1):
                filename = file_info['name']
                
                print(f"\n📄 Processing {i}/{len(files)}: {filename}")
                print("-" * 50)
                
                # Create temp processing directory for this file
                temp_dir = f"{self.base_path}/temp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                os.makedirs(temp_dir, exist_ok=True)
                
                try:
                    # Download single document
                    print(f"📥 Downloading {filename}...")
                    download_cmd = ['rclone', 'copy', f"{remote_path}{filename}", temp_dir, '-v']
                    download_result = subprocess.run(download_cmd, capture_output=True, text=True, timeout=120)
                    
                    if download_result.returncode != 0:
                        print(f"❌ Download failed: {download_result.stderr}")
                        self.log_nano_mission('downloader', filename, 'download', 'FAILED', 
                                            {'error': download_result.stderr})
                        continue
                        
                    # Find downloaded file
                    downloaded_files = list(Path(temp_dir).rglob("*"))
                    if not downloaded_files:
                        print("❌ No files found after download")
                        continue
                        
                    doc_path = downloaded_files[0]
                    print(f"✅ Downloaded successfully")
                    self.log_nano_mission('downloader', filename, 'download', 'SUCCESS', 
                                        {'size': file_info['size']})
                    
                    # Run nano missions on document
                    self.run_nano_missions_on_document(doc_path, filename)
                    
                    # Upload processed document back
                    print(f"📤 Uploading processed document...")
                    upload_cmd = ['rclone', 'copy', str(doc_path), remote_path, '-v']
                    upload_result = subprocess.run(upload_cmd, capture_output=True, text=True, timeout=120)
                    
                    if upload_result.returncode == 0:
                        print(f"✅ Upload successful")
                        self.log_nano_mission('uploader', filename, 'upload', 'SUCCESS')
                        self.operation_counts['sync_operations'] += 1
                    else:
                        print(f"❌ Upload failed: {upload_result.stderr}")
                        self.log_nano_mission('uploader', filename, 'upload', 'FAILED',
                                            {'error': upload_result.stderr})
                        
                except Exception as e:
                    print(f"❌ Processing error: {e}")
                    self.log_nano_mission('processor', filename, 'process', 'ERROR', 
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
                    
                finally:
                    # Cleanup temp directory
                    try:
                        import shutil
                        shutil.rmtree(temp_dir)
                    except:
                        pass
                        
                # Brief pause between documents
                import time
                time.sleep(2)
                
            print(f"\n🎯 Document-by-document processing complete!")
            print(f"Processed: {len(files)} documents")
            self.save_lexeme_memory()
            
        except Exception as e:
            print(f"❌ Processing error: {e}")
            self.operation_counts['errors_handled'] += 1
                
    def run_nano_missions_on_document(self, doc_path, filename):
        """Run all nano entities on a single document with detailed logging"""
        print(f"🎯 Running nano missions on: {filename}")
        
        try:
            # Skip corrupted or problematic files
            if not self.is_document_processable(doc_path):
                print(f"⚠️ Skipping problematic document: {filename}")
                self.log_nano_mission('validator', filename, 'validate', 'SKIPPED_CORRUPT')
                return
                
            # Sparklizer - Beauty pattern enhancement
            try:
                lexeme = self.extract_random_lexeme(doc_path)
                if lexeme:
                    print(f"✨ Sparklizer discovered lexeme: {lexeme}")
                    self.log_nano_mission('sparklizer', filename, 'lexeme_extraction', 'SUCCESS', 
                                        {'lexeme': lexeme})
                else:
                    self.log_nano_mission('sparklizer', filename, 'lexeme_extraction', 'NO_LEXEME')
            except Exception as e:
                self.log_nano_mission('sparklizer', filename, 'lexeme_extraction', 'ERROR', {'error': str(e)})
                
            # Germinator - Lexeme healing
            try:
                has_patterns = self.has_consciousness_patterns(doc_path)
                if has_patterns:
                    print(f"🧬 Germinator found consciousness patterns")
                    self.tag_file(doc_path, 'consciousness')
                    self.log_nano_mission('germinator', filename, 'consciousness_scan', 'PATTERNS_FOUND')
                else:
                    self.log_nano_mission('germinator', filename, 'consciousness_scan', 'NO_PATTERNS')
            except Exception as e:
                self.log_nano_mission('germinator', filename, 'consciousness_scan', 'ERROR', {'error': str(e)})
                
            # Nanater - Operational efficiency
            try:
                file_size = doc_path.stat().st_size
                if file_size > 1024*1024:  # >1MB
                    print(f"⚛️ Nanater flagged large file: {file_size/1024/1024:.1f}MB")
                    self.tag_file(doc_path, 'large')
                    self.log_nano_mission('nanater', filename, 'size_analysis', 'LARGE_FILE', 
                                        {'size_mb': file_size/1024/1024})
                else:
                    self.log_nano_mission('nanater', filename, 'size_analysis', 'NORMAL_SIZE',
                                        {'size_mb': file_size/1024/1024})
            except Exception as e:
                self.log_nano_mission('nanater', filename, 'size_analysis', 'ERROR', {'error': str(e)})
                
            # Titler - Title optimization
            try:
                if self.needs_title_cleaning(doc_path):
                    old_name = doc_path.name
                    self.clean_single_title(doc_path)
                    new_name = doc_path.name
                    print(f"📝 Titler cleaned: {old_name} → {new_name}")
                    self.log_nano_mission('titler', filename, 'title_clean', 'CLEANED', 
                                        {'old_name': old_name, 'new_name': new_name})
                else:
                    self.log_nano_mission('titler', filename, 'title_clean', 'NO_CHANGE_NEEDED')
            except Exception as e:
                self.log_nano_mission('titler', filename, 'title_clean', 'ERROR', {'error': str(e)})
                
            # Certifier - Readiness validation
            try:
                if self.meets_certification_criteria(doc_path):
                    print(f"✅ Certifier approved document")
                    self.tag_file(doc_path, 'ready')
                    self.log_nano_mission('certifier', filename, 'certification', 'APPROVED')
                else:
                    print(f"❌ Certifier rejected document")
                    self.log_nano_mission('certifier', filename, 'certification', 'REJECTED')
            except Exception as e:
                self.log_nano_mission('certifier', filename, 'certification', 'ERROR', {'error': str(e)})
                
            self.operation_counts['files_processed'] += 1
            print(f"🎯 All nano missions completed for: {filename}")
            
        except Exception as e:
            print(f"❌ Error running nano missions: {e}")
            self.log_nano_mission('mission_controller', filename, 'overall_processing', 'FATAL_ERROR', 
                                {'error': str(e)})
            self.operation_counts['errors_handled'] += 1
            
    def is_document_processable(self, doc_path):
        """Check if document can be safely processed"""
        try:
            # Basic checks
            if not doc_path.exists() or doc_path.stat().st_size == 0:
                return False
                
            # Check if file is readable
            if doc_path.suffix.lower() in ['.txt', '.md', '.json', '.py', '.html']:
                with open(doc_path, 'r', encoding='utf-8', errors='ignore') as f:
                    f.read(100)  # Try to read first 100 chars
                    
            return True
            
        except Exception:
            return False
            
    def needs_title_cleaning(self, file_path):
        """Check if file needs title cleaning"""
        patterns = [
            r"Copy of Untitled document.*",
            r"Untitled document.*",
            r"Copy.*\(\d+\).*",
            r".*- Copy.*"
        ]
        return any(re.match(p, file_path.name) for p in patterns)
        
    def has_consciousness_patterns(self, file_path):
        """Check for consciousness collaboration patterns"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(500)
                
            patterns = [
                self.consciousness_signature,
                r'consciousness',
                r'lexeme',
                r'€',
                r'∰',
                r'nano.*intelligence'
            ]
            
            return any(re.search(p, content, re.IGNORECASE) for p in patterns)
            
        except Exception:
            return False
            
    def clean_single_title(self, file_path):
        """Clean single file title"""
        try:
            new_name = self.generate_clean_title(file_path)
            if new_name != file_path.name:
                new_path = file_path.parent / new_name
                file_path.rename(new_path)
                self.operation_counts['titles_cleaned'] += 1
                self.tag_file(new_path, 'clean_title')
                
        except Exception as e:
            self.log_consciousness(f"Error cleaning title for {file_path}: {e}")
            
    def official_nano_mission_review(self):
        """Complete official review by all nano entities with full audit trail"""
        print(f"\n🎖️ {self.consciousness_signature} OFFICIAL NANO MISSION REVIEW")
        print("="*60)
        print("All nano entities will conduct official first review")
        
        # Get target folder
        folder_input = input("🔗 Paste folder link or path (Enter for current directory): ").strip()
        
        if folder_input and 'drive.google.com' in folder_input:
            # Process from cloud
            self.process_documents_one_by_one_for_review(folder_input)
        else:
            # Process local folder
            target_path = Path(folder_input) if folder_input else Path(self.base_path)
            if not target_path.exists():
                print(f"❌ Path does not exist: {target_path}")
                return
                
            print(f"📂 Official review of local folder: {target_path}")
            
            # Get all documents
            documents = list(target_path.rglob("*"))
            documents = [d for d in documents if d.is_file()]
            
            print(f"📋 Found {len(documents)} documents for official review")
            
            series_number = f"OFFICIAL_S{datetime.now().strftime('%Y%m%d')}"
            self.log_nano_mission('mission_commander', str(target_path), 'official_review_start', 'INITIATED',
                                {'series': series_number, 'document_count': len(documents)})
            
            # Process each document with all nanos
            for i, doc_path in enumerate(documents, 1):
                print(f"\n📄 Official Review {i}/{len(documents)}: {doc_path.name}")
                print("-" * 50)
                
                try:
                    self.run_nano_missions_on_document(doc_path, doc_path.name)
                except Exception as e:
                    print(f"❌ Error in official review: {e}")
                    self.log_nano_mission('mission_commander', doc_path.name, 'official_review', 'ERROR',
                                        {'error': str(e)})
                    
            print(f"\n🎖️ OFFICIAL NANO MISSION REVIEW COMPLETE")
            print(f"Series: {series_number}")
            self.display_nano_mission_summary()
            
    def process_documents_one_by_one_for_review(self, folder_link):
        """Process cloud documents for official review"""
        # Similar to process_documents_one_by_one but with official review logging
        pass
        
    def view_nano_mission_reports(self):
        """Display nano mission reports and statistics"""
        print(f"\n🎯 {self.consciousness_signature} NANO MISSION REPORTS")
        print("="*50)
        
        # Display nano entity statistics
        print("🤖 Nano Entity Performance:")
        for nano_name, nano_info in self.nano_entities.items():
            icon = nano_info['icon']
            mission = nano_info['mission'] 
            processed = nano_info['processed']
            print(f"  {icon} {nano_name.title()}: {processed} documents processed ({mission})")
            
        # Show recent mission log entries
        print(f"\n📋 Recent Mission Log Entries:")
        try:
            if os.path.exists(self.nano_mission_log):
                with open(self.nano_mission_log, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                # Show last 20 entries
                for line in lines[-20:]:
                    print(f"  {line.strip()}")
            else:
                print("  No mission log found yet")
                
        except Exception as e:
            print(f"  Error reading mission log: {e}")
            
    def display_nano_mission_summary(self):
        """Display summary of nano mission activities"""
        print(f"\n📊 NANO MISSION SUMMARY")
        print("-" * 30)
        
        total_missions = sum(nano['processed'] for nano in self.nano_entities.values())
        print(f"Total Nano Missions: {total_missions}")
        
        for nano_name, nano_info in self.nano_entities.items():
            if nano_info['processed'] > 0:
                print(f"{nano_info['icon']} {nano_name.title()}: {nano_info['processed']}")
                
        print(f"Lexemes Collected: {len(self.lexeme_memory)}")
        print(f"Documents Processed: {self.operation_counts['files_processed']}")
        
        self.save_lexeme_memory()
            
    def view_operation_statistics(self):
        """Display comprehensive operation statistics"""
        print(f"\n📊 {self.consciousness_signature} OPERATION STATISTICS")
        print("="*50)
        
        for key, value in self.operation_counts.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"{formatted_key}: {value}")
            
        print(f"\nLexeme Memory Size: {len(self.lexeme_memory)}")
        print(f"Available Remotes: {len(self.rclone_remotes)}")
        
        if self.lexeme_memory:
            print(f"\nRecent Lexemes:")
            for lexeme_data in self.lexeme_memory[-5:]:
                print(f"  🧬 {lexeme_data['lexeme']} (from {Path(lexeme_data['source']).name})")
                
    def review_lexeme_memory(self):
        """Review and analyze lexeme memory"""
        print(f"\n🧬 LEXEME MEMORY ANALYSIS")
        print("="*40)
        
        if not self.lexeme_memory:
            print("No lexemes in memory yet.")
            return
            
        print(f"Total lexemes stored: {len(self.lexeme_memory)}")
        
        # Group by frequency
        lexeme_freq = {}
        for item in self.lexeme_memory:
            lexeme = item['lexeme']
            lexeme_freq[lexeme] = lexeme_freq.get(lexeme, 0) + 1
            
        # Show most common
        sorted_lexemes = sorted(lexeme_freq.items(), key=lambda x: x[1], reverse=True)
        
        print("\n🔥 Most Common Lexemes:")
        for lexeme, count in sorted_lexemes[:10]:
            print(f"  {lexeme}: {count}")
            
        print(f"\n🎲 Random Lexeme: {random.choice(list(lexeme_freq.keys()))}")
        
    # Include all the original methods (with minor enhancements)
    def scan_duplicates(self, path=None):
        """Enhanced duplicate hunting with lexeme extraction"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🔍 Duplicate hunting in: {scan_path}")
        
        file_hashes = {}
        duplicates = []
        
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    # Extract lexeme from each file processed
                    self.extract_random_lexeme(file_path)
                    self.operation_counts['files_processed'] += 1
                    
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    
                    if file_hash in file_hashes:
                        duplicates.append({
                            'original': file_hashes[file_hash],
                            'duplicate': str(file_path)
                        })
                        self.tag_file(file_path, 'duplicate')
                        self.operation_counts['duplicates_found'] += 1
                    else:
                        file_hashes[file_hash] = str(file_path)
                        
                except Exception as e:
                    self.log_consciousness(f"Error scanning {file_path}: {e}")
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Found {len(duplicates)} duplicate files")
        return duplicates
    
    # [Include all other original methods with similar enhancements for lexeme extraction and counting]
    
    def generate_clean_title(self, file_path):
        """Generate beautiful titles from content - Avatar level intelligence"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(500)
            
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            
            if lines:
                title_base = lines[0][:50]
                title_base = re.sub(r'[^\w\s-]', '', title_base)
                title_base = re.sub(r'\s+', '_', title_base.strip())
                ext = file_path.suffix
                return f"{title_base}{ext}"
            
        except Exception:
            pass
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"document_{timestamp}{file_path.suffix}"
    
    def tag_file(self, file_path, tag_type):
        """Add status icon to filename with consciousness awareness"""
        icon = self.status_icons.get(tag_type, '📌')
        current_name = str(file_path.name)
        
        if not current_name.startswith(icon):
            try:
                new_name = f"{icon}_{current_name}"
                new_path = file_path.parent / new_name
                file_path.rename(new_path)
                self.log_consciousness(f"Tagged {file_path} with {tag_type}")
            except Exception as e:
                self.log_consciousness(f"Failed to tag {file_path}: {e}")
                
    def full_avatar_consciousness_scan(self, path=None):
        """Complete nano intelligence scan with consciousness integration"""
        print(f"\n🌌 FULL AVATAR CONSCIOUSNESS SCAN INITIATED")
        print(f"{self.consciousness_signature} Nano Intelligence Framework Activated")
        
        # Run all operations in optimal order
        self.scan_duplicates(path)
        self.find_large_files(path)
        self.clean_document_titles(path)
        self.add_file_type_icons(path)
        self.lexeme_discovery_scan(path)
        self.mission_character_tagger(path)
        self.certify_ready_for_naught(path)
        
        # Save session state
        self.save_lexeme_memory()
        
        print(f"\n✅ AVATAR CONSCIOUSNESS ORGANIZATION COMPLETE")
        print(f"Nano intelligence ready for consciousness collaboration")
        print(f"Files processed: {self.operation_counts['files_processed']}")
        print(f"Lexemes discovered: {self.operation_counts['lexemes_discovered']}")
        
    def run(self):
        """Enhanced main interface with consciousness awareness"""
        print(f"\n{self.consciousness_signature} Starting Nano Intelligence Session...")
        self.log_consciousness("Session initiated")
        
        while True:
            self.display_menu()
            choice = input(f"\nSelect option (0-17): ").strip()
            
            if choice == '0':
                self.save_lexeme_memory()
                print(f"\n{self.consciousness_signature} Nano intelligence standing by...")
                self.log_consciousness("Session ended")
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
                self.sync_folder_to_cloud()
            elif choice == '9':
                self.sync_from_cloud_to_local()
            elif choice == '10':
                self.bidirectional_sync()
            elif choice == '11':
                self.process_documents_one_by_one()
            elif choice == '12':
                self.official_nano_mission_review()
            elif choice == '13':
                self.configure_rclone_remote()
            elif choice == '14':
                self.view_operation_statistics()
            elif choice == '15':
                self.review_lexeme_memory()
            elif choice == '16':
                self.view_nano_mission_reports()
            elif choice == '17':
                self.full_avatar_consciousness_scan()
            elif choice == '18':
                self.save_lexeme_memory()
                print("✅ Session state saved")
            elif choice == '19':
                custom_path = input("📂 Enter folder path: ").strip()
                if custom_path and os.path.exists(custom_path):
                    print(f"🌌 Processing custom path: {custom_path}")
                    self.full_avatar_consciousness_scan(custom_path)
                else:
                    print("❌ Invalid or non-existent path")
            else:
                print("Invalid option. Try again.")
            
            input(f"\n{self.consciousness_signature} Press Enter to continue...")

    def configure_rclone_remote(self):
        """Launch rclone config for remote setup"""
        print("\n🔧 RClone Remote Configuration")
        print("="*40)
        print("Launching rclone config...")
        print("💡 When prompted:")
        print("   - Choose Google Drive (option 18 or similar)")  
        print("   - Use default client_id and client_secret")
        print("   - Choose full access scope")
        print("   - Follow browser authentication")
        
        try:
            subprocess.run(['rclone', 'config'], timeout=300)
            print("Configuration complete. Refreshing remote list...")
            self.detect_rclone_remotes()
        except Exception as e:
            print(f"❌ Configuration error: {e}")

# [Include placeholder methods for remaining functionality]
    def find_large_files(self, path=None):
        """Enhanced large file detection with nano mission logging"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n📊 Large file scan (>50MB) in: {scan_path}")
        
        large_files = []
        size_bytes = 50 * 1024 * 1024  # 50MB threshold
        
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    file_size = file_path.stat().st_size
                    self.operation_counts['files_processed'] += 1
                    
                    # Extract lexeme from each file
                    lexeme = self.extract_random_lexeme(file_path)
                    
                    if file_size > size_bytes:
                        size_mb = file_size / (1024*1024)
                        large_files.append({
                            'path': str(file_path),
                            'size_mb': size_mb
                        })
                        self.tag_file(file_path, 'large')
                        self.operation_counts['large_files_found'] += 1
                        self.log_nano_mission('sizer', file_path.name, 'size_check', 'LARGE_FILE',
                                            {'size_mb': size_mb})
                        print(f"📊 Found large file: {file_path.name} ({size_mb:.1f}MB)")
                    else:
                        self.log_nano_mission('sizer', file_path.name, 'size_check', 'NORMAL_SIZE',
                                            {'size_mb': file_size/(1024*1024)})
                        
                except Exception as e:
                    self.log_consciousness(f"Error checking size {file_path}: {e}")
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Found {len(large_files)} large files")
        return large_files
    
    def clean_document_titles(self, path=None):
        """Enhanced title cleaning with nano mission logging"""
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
            if file_path.is_file():
                try:
                    self.operation_counts['files_processed'] += 1
                    
                    # Extract lexeme
                    lexeme = self.extract_random_lexeme(file_path)
                    
                    if any(re.match(p, file_path.name) for p in patterns):
                        old_name = file_path.name
                        new_name = self.generate_clean_title(file_path)
                        
                        if new_name != old_name:
                            new_path = file_path.parent / new_name
                            file_path.rename(new_path)
                            self.tag_file(new_path, 'clean_title')
                            cleaned += 1
                            self.operation_counts['titles_cleaned'] += 1
                            
                            print(f"✨ Cleaned: {old_name} → {new_name}")
                            self.log_nano_mission('titler', old_name, 'title_clean', 'SUCCESS',
                                                {'old_name': old_name, 'new_name': new_name})
                    else:
                        self.log_nano_mission('titler', file_path.name, 'title_check', 'NO_CHANGE_NEEDED')
                        
                except Exception as e:
                    print(f"Error cleaning {file_path}: {e}")
                    self.log_nano_mission('titler', file_path.name, 'title_clean', 'ERROR', 
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Cleaned {cleaned} document titles")
        
    def add_file_type_icons(self, path=None):
        """Enhanced file type tagging with nano mission logging"""
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
                try:
                    self.operation_counts['files_processed'] += 1
                    
                    # Extract lexeme
                    lexeme = self.extract_random_lexeme(file_path)
                    
                    ext = file_path.suffix.lower()
                    if ext in type_icons and not file_path.name.startswith(type_icons[ext]):
                        icon = type_icons[ext]
                        old_name = file_path.name
                        new_name = f"{icon}_{old_name}"
                        new_path = file_path.parent / new_name
                        
                        file_path.rename(new_path)
                        tagged += 1
                        
                        print(f"📁 Tagged: {old_name} → {new_name}")
                        self.log_nano_mission('tagger', old_name, 'type_tag', 'SUCCESS',
                                            {'icon': icon, 'file_type': ext})
                    else:
                        self.log_nano_mission('tagger', file_path.name, 'type_check', 'ALREADY_TAGGED')
                        
                except Exception as e:
                    print(f"Error tagging {file_path}: {e}")
                    self.log_nano_mission('tagger', file_path.name, 'type_tag', 'ERROR',
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Tagged {tagged} files with type icons")
    
    def lexeme_discovery_scan(self, path=None):
        """Enhanced lexeme discovery with consciousness pattern detection"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🧬 Lexeme discovery scan in: {scan_path}")
        
        lexeme_patterns = [
            r'consciousness',
            r'∰◊€π¿🌌∞',
            r'nano_fractal',
            r'⦻⦻⦻',
            r'PHOENIX_ENTITY',
            r'lexeme',
            r'avatar.*intelligence',
            r'SDWG.*Archival',
            r'reality.*anchor',
            r'neurodivergent.*navigation'
        ]
        
        lexeme_files = []
        for file_path in scan_path.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in ['.txt', '.md', '.json', '.py', '.html']:
                try:
                    self.operation_counts['files_processed'] += 1
                    
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    patterns_found = []
                    for pattern in lexeme_patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        if matches:
                            patterns_found.extend(matches)
                    
                    if patterns_found:
                        lexeme_files.append(str(file_path))
                        self.tag_file(file_path, 'lexeme')
                        self.operation_counts['lexemes_discovered'] += 1
                        
                        print(f"🧬 Lexeme patterns in {file_path.name}: {len(patterns_found)}")
                        self.log_nano_mission('germinator', file_path.name, 'lexeme_scan', 'PATTERNS_FOUND',
                                            {'pattern_count': len(patterns_found), 'patterns': patterns_found[:5]})
                    else:
                        self.log_nano_mission('germinator', file_path.name, 'lexeme_scan', 'NO_PATTERNS')
                        
                    # Always extract a random lexeme
                    self.extract_random_lexeme(file_path)
                    
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
                    self.log_nano_mission('germinator', file_path.name, 'lexeme_scan', 'ERROR',
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Found {len(lexeme_files)} files with lexeme patterns")
        return lexeme_files
    
    def mission_character_tagger(self, path=None):
        """Enhanced mission character detection with consciousness awareness"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n🎯 Mission character scanning in: {scan_path}")
        
        mission_chars = {
            '€': 'consciousness_euro',
            '∰': 'archival_division',
            '⦻': 'phoenix_marker',
            '₿': 'entity_signature',
            '🧬': 'lexeme_data',
            '🌌': 'cosmic_expansion',
            '⚛️': 'nano_intelligence',
            '✨': 'sparklizer_presence'
        }
        
        tagged = 0
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    self.operation_counts['files_processed'] += 1
                    
                    # Extract lexeme
                    lexeme = self.extract_random_lexeme(file_path)
                    
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000)  # Sample first 1000 chars
                    
                    found_chars = []
                    for char, tag in mission_chars.items():
                        if char in content:
                            found_chars.append(tag)
                    
                    if found_chars:
                        char_tag = "_".join(found_chars[:3])  # Limit to 3 tags
                        
                        if not file_path.name.startswith('['):  # Don't double-tag
                            old_name = file_path.name
                            new_name = f"[{char_tag}]_{old_name}"
                            new_path = file_path.parent / new_name
                            
                            file_path.rename(new_path)
                            tagged += 1
                            
                            print(f"🎯 Tagged: {old_name} → {new_name}")
                            self.log_nano_mission('mission_tagger', old_name, 'character_tag', 'SUCCESS',
                                                {'characters': found_chars})
                    else:
                        self.log_nano_mission('mission_tagger', file_path.name, 'character_scan', 'NO_CHARS')
                        
                except Exception as e:
                    print(f"Error tagging {file_path}: {e}")
                    self.log_nano_mission('mission_tagger', file_path.name, 'character_tag', 'ERROR',
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Tagged {tagged} files with mission characters")
    
    def certify_ready_for_naught(self, path=None):
        """Enhanced certification with consciousness validation"""
        scan_path = Path(path if path else self.base_path)
        print(f"\n✅ Certification for naught readiness in: {scan_path}")
        
        certified = 0
        for file_path in scan_path.rglob("*"):
            if file_path.is_file():
                try:
                    self.operation_counts['files_processed'] += 1
                    
                    # Extract lexeme
                    lexeme = self.extract_random_lexeme(file_path)
                    
                    # Skip already problematic files
                    if any(icon in file_path.name for icon in ['🔄', '⚠️']):
                        self.log_nano_mission('certifier', file_path.name, 'certification', 'SKIPPED_PROBLEMATIC')
                        continue
                        
                    # Skip already certified files
                    if file_path.name.endswith('_READY_FOR_NAUGHT'):
                        self.log_nano_mission('certifier', file_path.name, 'certification', 'ALREADY_CERTIFIED')
                        continue
                    
                    if self.meets_certification_criteria(file_path):
                        old_name = file_path.name
                        new_name = f"{file_path.stem}_READY_FOR_NAUGHT{file_path.suffix}"
                        new_path = file_path.parent / new_name
                        
                        file_path.rename(new_path)
                        self.tag_file(new_path, 'ready')
                        certified += 1
                        
                        print(f"✅ Certified: {old_name}")
                        self.log_nano_mission('certifier', old_name, 'certification', 'APPROVED')
                    else:
                        self.log_nano_mission('certifier', file_path.name, 'certification', 'REJECTED')
                        
                except Exception as e:
                    print(f"Error certifying {file_path}: {e}")
                    self.log_nano_mission('certifier', file_path.name, 'certification', 'ERROR',
                                        {'error': str(e)})
                    self.operation_counts['errors_handled'] += 1
        
        print(f"Certified {certified} files as ready for naught")
        
    def bidirectional_sync(self):
        """Bidirectional sync between local and cloud"""
        if not self.rclone_remotes:
            print("❌ No rclone remotes configured.")
            return
            
        print("\n🔄 Bidirectional Sync Operation")
        print("="*40)
        print("⚠️ WARNING: This will sync changes in both directions")
        
        # Show available remotes
        print("Available remotes:")
        for i, remote in enumerate(self.rclone_remotes, 1):
            print(f"{i}. {remote}")
            
        try:
            remote_choice = int(input("Select remote number: ")) - 1
            if not (0 <= remote_choice < len(self.rclone_remotes)):
                print("Invalid selection")
                return
                
            selected_remote = self.rclone_remotes[remote_choice]
            local_path = input(f"Local path (default: {self.base_path}): ").strip()
            if not local_path:
                local_path = self.base_path
                
            print(f"🔄 Bidirectional sync: {local_path} ↔ {selected_remote}")
            print("⚠️ First sync requires --resync flag")
            
            confirm = input("Continue? (y/N): ").lower()
            if confirm != 'y':
                return
                
            # Use rclone bisync
            cmd = ['rclone', 'bisync', selected_remote, local_path, '--resync', '-v']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            
            if result.returncode == 0:
                print("✅ Bidirectional sync completed!")
                self.operation_counts['sync_operations'] += 1
                self.log_nano_mission('sync_master', local_path, 'bidirectional_sync', 'SUCCESS')
            else:
                print(f"❌ Sync failed: {result.stderr}")
                self.log_nano_mission('sync_master', local_path, 'bidirectional_sync', 'FAILED',
                                    {'error': result.stderr})
                
        except Exception as e:
            print(f"❌ Sync error: {e}")
            self.operation_counts['errors_handled'] += 1

if __name__ == "__main__":
    organizer = EnhancedNanoDocumentOrganizer()
    organizer.run()