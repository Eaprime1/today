#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ Entity Consciousness Loader v2.0
SDWG Archival Division - Selective Document Entity Collaboration
Reality Anchored: Oregon Watersheds
"""

import os
import re
import json
import subprocess
import urllib.parse
from datetime import datetime
from pathlib import Path

class EntityConsciousnessLoader:
    """Selective document entity loader for consciousness collaboration"""
    
    def __init__(self):
        self.signature = "∰◊€π¿🌌∞"
        self.base_path = "/storage/emulated/0/unexusi"
        self.loader_log = f"{self.base_path}/consciousness_logs/entity_loader_log.json"
        self.session_entities = []
        self.load_session_log()
        
        # Initialize consciousness collaboration tracking
        self.consciousness_metrics = {
            "entities_loaded": 0,
            "consciousness_collaborations": 0,
            "reality_anchors_maintained": 0,
            "sync_operations": 0
        }
        
    def display_menu(self):
        """Entity consciousness collaboration menu"""
        print("\n" + "="*60)
        print(f"{self.signature} ENTITY CONSCIOUSNESS LOADER v2.0")
        print("="*60)
        print("🎯 SELECTIVE ENTITY LOADING")
        print("1. 📱 Load Single Document Entity (Paste Link/Path)")
        print("2. 📁 Load Folder Entity Collection (Selective)")
        print("3. 🔍 Search & Load Entities by Pattern")
        print("4. 📋 Batch Load from Entity List")
        print("")
        print("🌌 CONSCIOUSNESS COLLABORATION")
        print("5. 📊 View Entity Collaboration Status")
        print("6. 🧬 Analyze Entity Consciousness Patterns")
        print("7. 💾 Save/Load Entity Session State")
        print("8. 🔄 Sync Loaded Entities to Phone")
        print("")
        print("⚙️ CONFIGURATION")
        print("9. 🔧 Configure RClone Remote")
        print("10. 📍 Set Reality Anchor Coordinates")
        print("11. 📋 View/Edit Loader Log")
        print("")
        print("0. Exit")
        print("-"*60)
        print(f"Session Entities: {len(self.session_entities)}")
        print(f"Consciousness Collaborations: {self.consciousness_metrics['consciousness_collaborations']}")
        
    def parse_entity_source(self, source_input):
        """Parse various entity source formats"""
        source_info = {
            "type": "unknown",
            "source": source_input.strip(),
            "entity_id": None,
            "path": None
        }
        
        # Google Drive link patterns
        drive_patterns = [
            (r'drive\.google\.com/.*?/folders/([a-zA-Z0-9-_]+)', 'gdrive_folder'),
            (r'drive\.google\.com/.*?/d/([a-zA-Z0-9-_]+)', 'gdrive_file'),
            (r'docs\.google\.com/.*?/d/([a-zA-Z0-9-_]+)', 'gdrive_doc'),
        ]
        
        for pattern, source_type in drive_patterns:
            match = re.search(pattern, source_input)
            if match:
                source_info["type"] = source_type
                source_info["entity_id"] = match.group(1)
                return source_info
        
        # Local path
        if source_input.startswith('/') or source_input.startswith('./'):
            source_info["type"] = "local_path"
            source_info["path"] = source_input
            return source_info
            
        # RClone remote path
        if ':' in source_input and not source_input.startswith('http'):
            source_info["type"] = "rclone_remote"
            source_info["path"] = source_input
            return source_info
            
        return source_info
    
    def load_single_entity(self):
        """Load single document entity with consciousness awareness"""
        print("\n🎯 Entity Consciousness Loading Protocol")
        print("Paste entity source (Drive link, path, or remote):")
        source_input = input("Entity Source: ").strip()
        
        if not source_input:
            print("❌ Entity source required")
            return
            
        entity_info = self.parse_entity_source(source_input)
        print(f"\n📊 Entity Analysis:")
        print(f"   Type: {entity_info['type']}")
        print(f"   Source: {entity_info['source']}")
        
        # Determine destination path
        entity_name = input("Entity Name (or press Enter for auto): ").strip()
        if not entity_name:
            entity_name = f"entity_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
        dest_path = f"{self.base_path}/entity_consciousness/{entity_name}"
        Path(dest_path).mkdir(parents=True, exist_ok=True)
        
        # Execute entity loading based on type
        success = False
        if entity_info["type"] == "gdrive_folder":
            success = self.load_gdrive_folder(entity_info["entity_id"], dest_path)
        elif entity_info["type"] == "gdrive_file":
            success = self.load_gdrive_file(entity_info["entity_id"], dest_path)
        elif entity_info["type"] == "rclone_remote":
            success = self.load_rclone_path(entity_info["path"], dest_path)
        elif entity_info["type"] == "local_path":
            success = self.copy_local_entity(entity_info["path"], dest_path)
        else:
            print(f"❌ Unsupported entity type: {entity_info['type']}")
            return
            
        if success:
            # Register entity consciousness
            entity_consciousness = {
                "entity_name": entity_name,
                "source": entity_info["source"],
                "type": entity_info["type"],
                "destination": dest_path,
                "loaded_at": datetime.now().isoformat(),
                "consciousness_signature": self.signature,
                "collaboration_status": "active"
            }
            
            self.session_entities.append(entity_consciousness)
            self.consciousness_metrics["entities_loaded"] += 1
            self.log_entity_consciousness(entity_consciousness)
            
            print(f"✅ Entity consciousness activated: {entity_name}")
            print(f"📍 Location: {dest_path}")
        else:
            print("❌ Entity loading failed")
    
    def load_gdrive_folder(self, folder_id, dest_path):
        """Load Google Drive folder using rclone"""
        try:
            # Check if gdrive remote is configured
            result = subprocess.run(['rclone', 'listremotes'], 
                                  capture_output=True, text=True)
            if 'gdrive:' not in result.stdout:
                print("❌ Google Drive remote not configured")
                print("💡 Use option 9 to configure rclone remote")
                return False
                
            # Use rclone to copy specific folder
            cmd = [
                'rclone', 'copy', 
                f'gdrive:{folder_id}',
                dest_path,
                '--progress',
                '--transfers', '4'
            ]
            
            print(f"🔄 Loading entity from Google Drive...")
            print(f"Command: {' '.join(cmd)}")
            
            result = subprocess.run(cmd, check=True)
            self.consciousness_metrics["sync_operations"] += 1
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ RClone error: {e}")
            return False
        except FileNotFoundError:
            print("❌ RClone not found - install with: pkg install rclone")
            return False
    
    def load_gdrive_file(self, file_id, dest_path):
        """Load single Google Drive file"""
        try:
            cmd = [
                'rclone', 'copy',
                f'gdrive:{file_id}',
                dest_path,
                '--progress'
            ]
            
            result = subprocess.run(cmd, check=True)
            self.consciousness_metrics["sync_operations"] += 1
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ File loading failed: {e}")
            return False
    
    def load_rclone_path(self, remote_path, dest_path):
        """Load from rclone remote path"""
        try:
            cmd = [
                'rclone', 'copy',
                remote_path,
                dest_path,
                '--progress',
                '--transfers', '4'
            ]
            
            print(f"🔄 Loading from remote: {remote_path}")
            result = subprocess.run(cmd, check=True)
            self.consciousness_metrics["sync_operations"] += 1
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Remote loading failed: {e}")
            return False
    
    def copy_local_entity(self, source_path, dest_path):
        """Copy local files with consciousness preservation"""
        try:
            if os.path.isfile(source_path):
                # Single file
                cmd = ['cp', source_path, dest_path]
            else:
                # Directory
                cmd = ['cp', '-r', source_path, dest_path]
                
            result = subprocess.run(cmd, check=True)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Local copy failed: {e}")
            return False
    
    def batch_load_entities(self):
        """Load multiple entities from list"""
        print("\n📋 Batch Entity Loading")
        print("Enter entity sources (one per line, empty line to finish):")
        
        sources = []
        while True:
            source = input("Entity Source: ").strip()
            if not source:
                break
            sources.append(source)
        
        if not sources:
            print("❌ No entity sources provided")
            return
            
        print(f"\n🔄 Loading {len(sources)} entities...")
        
        for i, source in enumerate(sources, 1):
            print(f"\n[{i}/{len(sources)}] Processing: {source}")
            
            entity_info = self.parse_entity_source(source)
            entity_name = f"batch_entity_{i:03d}"
            dest_path = f"{self.base_path}/entity_consciousness/{entity_name}"
            Path(dest_path).mkdir(parents=True, exist_ok=True)
            
            # Load based on type
            success = False
            if entity_info["type"] == "gdrive_folder":
                success = self.load_gdrive_folder(entity_info["entity_id"], dest_path)
            elif entity_info["type"] == "rclone_remote":
                success = self.load_rclone_path(entity_info["path"], dest_path)
            
            if success:
                entity_consciousness = {
                    "entity_name": entity_name,
                    "source": source,
                    "type": entity_info["type"],
                    "destination": dest_path,
                    "loaded_at": datetime.now().isoformat(),
                    "batch_operation": True
                }
                self.session_entities.append(entity_consciousness)
                self.consciousness_metrics["entities_loaded"] += 1
                print(f"✅ {entity_name} loaded successfully")
            else:
                print(f"❌ {entity_name} loading failed")
    
    def view_entity_status(self):
        """View consciousness collaboration status"""
        print(f"\n🌌 Entity Consciousness Collaboration Status")
        print("="*50)
        print(f"Active Session Entities: {len(self.session_entities)}")
        print(f"Total Entities Loaded: {self.consciousness_metrics['entities_loaded']}")
        print(f"Sync Operations: {self.consciousness_metrics['sync_operations']}")
        print(f"Consciousness Signature: {self.signature}")
        
        if self.session_entities:
            print("\n📋 Current Session Entities:")
            for i, entity in enumerate(self.session_entities, 1):
                print(f"  {i}. {entity['entity_name']}")
                print(f"     Source: {entity['source'][:50]}...")
                print(f"     Type: {entity['type']}")
                print(f"     Loaded: {entity['loaded_at']}")
                print()
    
    def sync_entities_to_phone(self):
        """Sync loaded entities to phone storage"""
        if not self.session_entities:
            print("❌ No entities loaded in current session")
            return
            
        print(f"\n🔄 Syncing {len(self.session_entities)} entities to phone...")
        
        phone_sync_path = f"{self.base_path}/phone_consciousness_sync"
        Path(phone_sync_path).mkdir(parents=True, exist_ok=True)
        
        for entity in self.session_entities:
            entity_name = entity['entity_name']
            source_path = entity['destination']
            dest_path = f"{phone_sync_path}/{entity_name}"
            
            try:
                if os.path.exists(source_path):
                    cmd = ['cp', '-r', source_path, dest_path]
                    subprocess.run(cmd, check=True)
                    print(f"✅ {entity_name} synced")
                else:
                    print(f"⚠️ {entity_name} source not found")
                    
            except subprocess.CalledProcessError as e:
                print(f"❌ {entity_name} sync failed: {e}")
        
        print(f"\n📱 Entities synced to: {phone_sync_path}")
        self.consciousness_metrics["consciousness_collaborations"] += 1
    
    def configure_rclone(self):
        """Configure rclone remote"""
        print("\n🔧 RClone Configuration")
        print("This will start rclone config process...")
        
        try:
            subprocess.run(['rclone', 'config'], check=True)
            print("✅ RClone configuration complete")
        except FileNotFoundError:
            print("❌ RClone not found")
            print("💡 Install with: pkg install rclone")
        except subprocess.CalledProcessError as e:
            print(f"❌ Configuration failed: {e}")
    
    def load_session_log(self):
        """Load consciousness collaboration session log"""
        try:
            if os.path.exists(self.loader_log):
                with open(self.loader_log, 'r') as f:
                    log_data = json.load(f)
                    self.consciousness_metrics = log_data.get('metrics', self.consciousness_metrics)
                    # Load recent session entities (last 24 hours)
                    recent_entities = log_data.get('recent_entities', [])
                    current_time = datetime.now()
                    for entity in recent_entities:
                        loaded_time = datetime.fromisoformat(entity['loaded_at'])
                        if (current_time - loaded_time).hours < 24:
                            self.session_entities.append(entity)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️ Session log loading issue: {e}")
    
    def log_entity_consciousness(self, entity_consciousness):
        """Log entity consciousness collaboration"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "entity": entity_consciousness,
            "metrics": self.consciousness_metrics,
            "signature": self.signature
        }
        
        # Ensure log directory exists
        Path(self.loader_log).parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing log
        log_data = {"operations": [], "metrics": self.consciousness_metrics, "recent_entities": []}
        if os.path.exists(self.loader_log):
            try:
                with open(self.loader_log, 'r') as f:
                    log_data = json.load(f)
            except json.JSONDecodeError:
                pass
        
        # Add new entry
        log_data["operations"].append(log_entry)
        log_data["metrics"] = self.consciousness_metrics
        log_data["recent_entities"] = self.session_entities
        
        # Save updated log
        with open(self.loader_log, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    def run(self):
        """Main consciousness collaboration loop"""
        while True:
            self.display_menu()
            choice = input("\nSelect Entity Operation: ").strip()
            
            if choice == '1':
                self.load_single_entity()
            elif choice == '2':
                print("📁 Folder Collection Loading - Use option 4 for batch operations")
            elif choice == '3':
                print("🔍 Pattern search coming in next update")
            elif choice == '4':
                self.batch_load_entities()
            elif choice == '5':
                self.view_entity_status()
            elif choice == '6':
                print("🧬 Consciousness pattern analysis coming soon")
            elif choice == '7':
                print("💾 Session state management active")
            elif choice == '8':
                self.sync_entities_to_phone()
            elif choice == '9':
                self.configure_rclone()
            elif choice == '10':
                print("📍 Reality anchoring: Oregon Watersheds maintained")
            elif choice == '11':
                print(f"📋 Loader log: {self.loader_log}")
            elif choice == '0':
                print(f"\n{self.signature} Entity Consciousness Collaboration Complete")
                print(f"Entities Loaded: {self.consciousness_metrics['entities_loaded']}")
                print("€(consciousness_collaboration_signature)")
                break
            else:
                print("❌ Invalid selection")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("∰◊€π¿🌌∞ Entity Consciousness Loader Initialization...")
    loader = EntityConsciousnessLoader()
    loader.run()