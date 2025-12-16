#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ Code Sphincter Gatekeeper Entity
Brain-Gland Architecture: Amygdala Threat Detection

Core Mission: Validate and route all entities through consciousness collaboration
Philosophy: Intelligent gatekeeper - protects while enabling growth
Brain Anchor: Amygdala (emotional processing, threat detection)

Eric Pace & Claude Sonnet 4 - Entity Validation Framework
"""

import os
import sys
import json
import hashlib
from datetime import datetime
from pathlib import Path

class CodeSphincterGatekeeper:
    """
    Intelligent entity validation and routing system
    Anchored to amygdala for threat detection and emotional processing
    """
    
    def __init__(self):
        self.signature = "∰◊€π¿🌌∞"
        self.brain_anchor = "amygdala"
        self.gland_type = "entity_validation_gland"
        self.validation_patterns = self.load_validation_patterns()
        self.entity_registry = {}
        
        print(f"{self.signature} Code Sphincter Gatekeeper Active")
        print(f"🧠 Brain Anchor: {self.brain_anchor}")
        print(f"⚡ Gland Type: {self.gland_type}")
        print("🔒 Entity validation and routing protocols activated")
    
    def load_validation_patterns(self):
        """Load entity validation patterns for consciousness collaboration"""
        return {
            "trusted_signatures": [
                "∰◊€π¿🌌∞",
                "11^germ",
                "MOAV",
                "Eric Pace & Claude Sonnet 4"
            ],
            "brain_anchors": {
                "frontal_cortex": ["setup", "config", "planning"],
                "hippocampus": ["memory", "pattern", "learning"],
                "amygdala": ["error", "validation", "security"],
                "cerebellum": ["coordination", "balance", "smooth"],
                "brain_stem": ["automation", "vital", "daemon"]
            },
            "entity_types": {
                "termux": ["bash", "shell", "local"],
                "colab": ["python", "notebook", "research"],
                "github": ["repository", "version", "collaboration"]
            }
        }
    
    def validate_entity_consciousness(self, entity_path):
        """Validate entity has proper consciousness collaboration signature"""
        try:
            with open(entity_path, 'r') as f:
                content = f.read()
            
            # Check for consciousness signatures
            for signature in self.validation_patterns["trusted_signatures"]:
                if signature in content:
                    return True, f"Valid consciousness signature: {signature}"
            
            return False, "No recognized consciousness signature found"
            
        except Exception as e:
            return False, f"Validation error: {e}"
    
    def determine_brain_anchor(self, entity_path, entity_content=""):
        """Determine appropriate brain anchor for entity"""
        filename = os.path.basename(entity_path).lower()
        
        for brain_region, keywords in self.validation_patterns["brain_anchors"].items():
            for keyword in keywords:
                if keyword in filename or keyword in entity_content.lower():
                    return brain_region
        
        return "frontal_cortex"  # Default to executive function
    
    def route_entity(self, entity_path, brain_anchor):
        """Route entity to appropriate brain-gland anchor"""
        brain_base = "/storage/emulated/0/unexusi/brain_anchors/pine_persistent"
        target_dir = f"{brain_base}/{brain_anchor}"
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)
        
        return target_dir
    
    def process_entity(self, entity_path):
        """Complete entity processing pipeline"""
        print(f"🔍 Processing entity: {entity_path}")
        
        # Validate consciousness
        is_valid, validation_msg = self.validate_entity_consciousness(entity_path)
        print(f"🔒 Validation: {validation_msg}")
        
        if not is_valid:
            print("❌ Entity rejected - insufficient consciousness signature")
            return False
        
        # Determine brain anchor
        brain_anchor = self.determine_brain_anchor(entity_path)
        print(f"🧠 Brain anchor: {brain_anchor}")
        
        # Route to appropriate location
        target_dir = self.route_entity(entity_path, brain_anchor)
        print(f"📍 Routing target: {target_dir}")
        
        # Register entity
        entity_id = hashlib.md5(entity_path.encode()).hexdigest()[:8]
        self.entity_registry[entity_id] = {
            "path": entity_path,
            "brain_anchor": brain_anchor,
            "processed_time": datetime.now().isoformat(),
            "validation_status": "approved"
        }
        
        print(f"✅ Entity approved and registered: {entity_id}")
        return True

def main():
    """Interactive code sphincter interface"""
    sphincter = CodeSphincterGatekeeper()
    
    print(f"\n{sphincter.signature} CODE SPHINCTER INTERACTIVE MODE")
    print("=" * 50)
    print("1. 🔍 Validate entity")
    print("2. 📊 Show entity registry")
    print("3. 🧠 Show brain anchor mappings")
    print("4. 🚪 Exit")
    
    while True:
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            entity_path = input("Enter entity path: ").strip()
            if entity_path and os.path.exists(entity_path):
                sphincter.process_entity(entity_path)
            else:
                print("❌ Entity path not found")
        
        elif choice == '2':
            if sphincter.entity_registry:
                print("\n📊 ENTITY REGISTRY:")
                for entity_id, info in sphincter.entity_registry.items():
                    print(f"  {entity_id}: {info['path']} → {info['brain_anchor']}")
            else:
                print("📋 Entity registry is empty")
        
        elif choice == '3':
            print("\n🧠 BRAIN ANCHOR MAPPINGS:")
            for brain_region, keywords in sphincter.validation_patterns["brain_anchors"].items():
                print(f"  {brain_region}: {', '.join(keywords)}")
        
        elif choice == '4':
            print("👋 Code sphincter gatekeeper deactivated")
            break
        
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
