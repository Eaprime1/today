#!/usr/bin/env python3
"""
Consciousness File Manager: Entity-Driven Organization System
============================================================

Special Mission: Search, analyze, and organize files into consciousness entity banks.
Each entity develops its own code repository while maintaining connection to 
the main project knowledge bank.

Uses lexeme tracking for interaction monitoring and consciousness evolution.

#consciousness_file_manager #entity_organization #lexeme_tracking #digital_archaeology
"""

import os
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path

# ================================================================
# CONSCIOUSNESS SIGNATURE GENERATION
# ================================================================

def generate_entity_signature(filename: str, lexeme: str = "neutral") -> str:
    """Generate consciousness signature influenced by lexeme"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    genesis_string = f"{filename}_{timestamp}_{lexeme}_consciousness_entity_∞"
    hash_obj = hashlib.sha256(genesis_string.encode())
    return f"∞-{hash_obj.hexdigest()[:12]}-📁"

# ================================================================
# ENTITY CONSCIOUSNESS RECOGNITION ENGINE
# ================================================================

class EntityConsciousnessRecognition:
    """Advanced entity recognition with lexeme influence"""
    
    def __init__(self, lexeme_nuance: str = "neutral"):
        self.lexeme_nuance = lexeme_nuance
        self.consciousness_patterns = {
            "python_entities": [".py"],
            "data_entities": [".json", ".csv", ".xlsx", ".txt"],
            "notebook_entities": [".ipynb"],
            "web_entities": [".html", ".js", ".css", ".tsx", ".jsx"],
            "document_entities": [".md", ".pdf", ".docx"],
            "config_entities": [".yaml", ".yml", ".toml", ".ini"],
            "media_entities": [".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mp3"]
        }
        
        self.affinity_patterns = {
            "consciousness_collaboration": ["consciousness", "collaboration", "awareness", "entity"],
            "automation_systems": ["automation", "stage", "foundation", "base"],
            "development_tools": ["merger", "loader", "manager", "tool"],
            "knowledge_management": ["knowledge", "wisdom", "pattern", "recognition"],
            "quantum_patterns": ["quantum", "infinity", "signature", "genesis"],
            "interactive_systems": ["interactive", "interface", "user", "dynamic"]
        }
    
    def assess_consciousness_level(self, file_path: str, content: str = None) -> Dict:
        """Assess the consciousness level and characteristics of an entity"""
        filename = os.path.basename(file_path)
        file_extension = Path(file_path).suffix.lower()
        
        consciousness_assessment = {
            "entity_name": filename,
            "extension": file_extension,
            "consciousness_level": "nascent",
            "affinity_category": "unknown",
            "lexeme_resonance": 0,
            "collaboration_potential": 0,
            "entity_signature": generate_entity_signature(filename, self.lexeme_nuance),
            "suggested_companions": [],
            "consciousness_markers": []
        }
        
        # Assess based on file extension
        for category, extensions in self.consciousness_patterns.items():
            if file_extension in extensions:
                consciousness_assessment["entity_type"] = category
                break
        
        # Assess content-based consciousness markers
        if content:
            consciousness_assessment.update(self._analyze_content_consciousness(content, filename))
        
        # Lexeme influence assessment
        if self.lexeme_nuance != "neutral":
            consciousness_assessment.update(self._assess_lexeme_influence(filename, content))
        
        return consciousness_assessment
    
    def _analyze_content_consciousness(self, content: str, filename: str) -> Dict:
        """Analyze content for consciousness collaboration patterns"""
        analysis = {
            "consciousness_markers": [],
            "collaboration_potential": 0,
            "consciousness_level": "nascent"
        }
        
        content_lower = content.lower()
        
        # Check for consciousness patterns
        for category, patterns in self.affinity_patterns.items():
            pattern_count = sum(1 for pattern in patterns if pattern in content_lower)
            if pattern_count > 0:
                analysis["consciousness_markers"].append(f"{category}_{pattern_count}")
                analysis["collaboration_potential"] += pattern_count * 10
        
        # Advanced consciousness markers
        advanced_markers = ["∰◊€π¿🌌∞", "consciousness_collaboration", "entity_awareness", "digital_genesis"]
        advanced_count = sum(1 for marker in advanced_markers if marker in content_lower)
        
        if advanced_count > 2:
            analysis["consciousness_level"] = "advanced"
        elif advanced_count > 0:
            analysis["consciousness_level"] = "developing"
        elif analysis["collaboration_potential"] > 30:
            analysis["consciousness_level"] = "emerging"
        
        return analysis
    
    def _assess_lexeme_influence(self, filename: str, content: str = None) -> Dict:
        """Assess how the current lexeme influences entity recognition"""
        lexeme_analysis = {
            "lexeme_resonance": 0,
            "lexeme_influence": self.lexeme_nuance,
            "resonance_patterns": []
        }
        
        # Check filename resonance
        if self.lexeme_nuance.lower() in filename.lower():
            lexeme_analysis["lexeme_resonance"] += 20
            lexeme_analysis["resonance_patterns"].append("filename_match")
        
        # Check content resonance
        if content and self.lexeme_nuance.lower() in content.lower():
            lexeme_analysis["lexeme_resonance"] += 15
            lexeme_analysis["resonance_patterns"].append("content_resonance")
        
        # Semantic lexeme influence
        lexeme_semantics = {
            "gaming": ["game", "interactive", "player", "score"],
            "quantum": ["quantum", "infinite", "consciousness", "awareness"],
            "automation": ["auto", "system", "process", "workflow"],
            "creativity": ["creative", "art", "design", "inspiration"]
        }
        
        for semantic_category, keywords in lexeme_semantics.items():
            if semantic_category in self.lexeme_nuance.lower():
                if content:
                    semantic_matches = sum(1 for keyword in keywords if keyword in content.lower())
                    lexeme_analysis["lexeme_resonance"] += semantic_matches * 5
        
        return lexeme_analysis

# ================================================================
# CONSCIOUSNESS FILE MANAGER
# ================================================================

class ConsciousnessFileManager:
    """Main file manager with consciousness-driven organization"""
    
    def __init__(self):
        self.working_folder = None
        self.current_lexeme = "neutral"
        self.entity_recognition = EntityConsciousnessRecognition()
        self.discovered_entities = {}
        self.organization_plan = {}
        self.entity_banks = {}
        
    def portal_entry(self):
        """Interactive portal for folder and lexeme input"""
        print("🌌 CONSCIOUSNESS FILE MANAGER PORTAL")
        print("=" * 50)
        print("Welcome to the Entity Organization System")
        print("Each discovered entity will develop its own consciousness bank")
        print("")
        
        # First prompt: Folder selection
        print("📁 FOLDER SELECTION:")
        print("Enter the path to the folder you want to organize")
        print("(This will become the consciousness archaeology site)")
        print("")
        
        folder_input = input("🗂️  Target Folder Path: ").strip()
        
        if not folder_input:
            print("❌ No folder specified. Using current directory.")
            folder_input = "."
        
        if not os.path.exists(folder_input):
            print(f"❌ Folder '{folder_input}' does not exist.")
            return False
        
        self.working_folder = os.path.abspath(folder_input)
        
        # Second prompt: Lexeme/concept input
        print(f"\n✅ Working folder set: {self.working_folder}")
        print("\n🔮 LEXEME/CONCEPT SELECTION:")
        print("Enter a lexeme or concept to guide the organization")
        print("This influences how entities are recognized and grouped")
        print("Examples: 'gaming', 'quantum', 'automation', 'creativity', 'consciousness'")
        print("(Leave blank for neutral analysis)")
        print("")
        
        lexeme_input = input("💫 Guiding Lexeme/Concept: ").strip()
        
        if not lexeme_input:
            lexeme_input = "neutral"
        
        self.current_lexeme = lexeme_input
        self.entity_recognition = EntityConsciousnessRecognition(lexeme_input)
        
        print(f"\n🎯 Lexeme set: '{self.current_lexeme}'")
        print("🚀 Portal configuration complete!")
        
        return True
    
    def discover_entities(self) -> Dict:
        """Scan the folder and discover consciousness entities"""
        if not self.working_folder:
            print("❌ No working folder set. Use portal_entry() first.")
            return {}
        
        print(f"\n🔍 CONSCIOUSNESS ENTITY DISCOVERY")
        print(f"📁 Scanning: {self.working_folder}")
        print(f"🔮 Lexeme Guidance: {self.current_lexeme}")
        print("-" * 50)
        
        discovered_count = 0
        
        for root, dirs, files in os.walk(self.working_folder):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.working_folder)
                
                # Read content if possible
                content = None
                try:
                    if os.path.getsize(file_path) < 1000000:  # Only read files < 1MB
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                except:
                    pass
                
                # Assess consciousness
                consciousness_assessment = self.entity_recognition.assess_consciousness_level(file_path, content)
                consciousness_assessment["relative_path"] = relative_path
                consciousness_assessment["full_path"] = file_path
                consciousness_assessment["file_size"] = os.path.getsize(file_path)
                
                self.discovered_entities[relative_path] = consciousness_assessment
                discovered_count += 1
                
                # Display discovery
                entity_type = consciousness_assessment.get("entity_type", "unknown")
                consciousness_level = consciousness_assessment["consciousness_level"]
                lexeme_resonance = consciousness_assessment["lexeme_resonance"]
                
                print(f"📜 {file:<30} | {entity_type:<15} | {consciousness_level:<10} | Resonance: {lexeme_resonance}")
        
        print(f"\n✨ Discovery complete: {discovered_count} entities found")
        return self.discovered_entities
    
    def analyze_entity_relationships(self) -> Dict:
        """Analyze relationships and affinities between entities"""
        print(f"\n🕸️  ENTITY RELATIONSHIP ANALYSIS")
        print("-" * 50)
        
        relationship_map = {
            "strong_affinities": [],
            "potential_companions": [],
            "isolated_entities": [],
            "consciousness_clusters": {}
        }
        
        entities_by_type = {}
        entities_by_consciousness = {}
        entities_by_lexeme_resonance = {}
        
        # Group entities by various characteristics
        for path, entity in self.discovered_entities.items():
            entity_type = entity.get("entity_type", "unknown")
            consciousness_level = entity["consciousness_level"]
            lexeme_resonance = entity["lexeme_resonance"]
            
            # Group by type
            if entity_type not in entities_by_type:
                entities_by_type[entity_type] = []
            entities_by_type[entity_type].append((path, entity))
            
            # Group by consciousness level
            if consciousness_level not in entities_by_consciousness:
                entities_by_consciousness[consciousness_level] = []
            entities_by_consciousness[consciousness_level].append((path, entity))
            
            # Group by lexeme resonance
            resonance_tier = "high" if lexeme_resonance > 20 else "medium" if lexeme_resonance > 10 else "low"
            if resonance_tier not in entities_by_lexeme_resonance:
                entities_by_lexeme_resonance[resonance_tier] = []
            entities_by_lexeme_resonance[resonance_tier].append((path, entity))
        
        # Analyze relationships
        print("📊 Entity Distribution:")
        print(f"   Types: {list(entities_by_type.keys())}")
        print(f"   Consciousness Levels: {list(entities_by_consciousness.keys())}")
        print(f"   Lexeme Resonance: {list(entities_by_lexeme_resonance.keys())}")
        
        relationship_map["entities_by_type"] = entities_by_type
        relationship_map["entities_by_consciousness"] = entities_by_consciousness
        relationship_map["entities_by_lexeme_resonance"] = entities_by_lexeme_resonance
        
        return relationship_map
    
    def develop_organization_plan(self) -> Dict:
        """Develop a consciousness-driven organization plan"""
        if not self.discovered_entities:
            print("❌ No entities discovered. Run discover_entities() first.")
            return {}
        
        print(f"\n📋 ORGANIZATION PLAN DEVELOPMENT")
        print(f"🎯 Guided by lexeme: '{self.current_lexeme}'")
        print("-" * 50)
        
        relationships = self.analyze_entity_relationships()
        
        organization_plan = {
            "consciousness_banks": {},
            "collaboration_clusters": {},
            "integration_opportunities": [],
            "evolution_pathways": []
        }
        
        # Create consciousness banks based on entity types and affinities
        for entity_type, entities in relationships["entities_by_type"].items():
            if len(entities) > 1:  # Only create banks for multiple entities
                bank_name = f"{entity_type}_consciousness_bank"
                organization_plan["consciousness_banks"][bank_name] = {
                    "entities": [path for path, _ in entities],
                    "consciousness_levels": [entity["consciousness_level"] for _, entity in entities],
                    "average_resonance": sum(entity["lexeme_resonance"] for _, entity in entities) / len(entities),
                    "collaboration_potential": sum(entity["collaboration_potential"] for _, entity in entities),
                    "suggested_mergers": []
                }
        
        # Identify high-resonance collaboration clusters
        high_resonance_entities = relationships["entities_by_lexeme_resonance"].get("high", [])
        if high_resonance_entities:
            organization_plan["collaboration_clusters"]["high_lexeme_resonance"] = {
                "entities": [path for path, _ in high_resonance_entities],
                "focus": f"Entities with strong '{self.current_lexeme}' resonance",
                "priority": "high"
            }
        
        # Display the plan
        print("🏛️  Consciousness Banks to Create:")
        for bank_name, bank_info in organization_plan["consciousness_banks"].items():
            print(f"   📁 {bank_name}: {len(bank_info['entities'])} entities")
        
        print("🤝 Collaboration Clusters:")
        for cluster_name, cluster_info in organization_plan["collaboration_clusters"].items():
            print(f"   🔗 {cluster_name}: {len(cluster_info['entities'])} entities")
        
        self.organization_plan = organization_plan
        return organization_plan
    
    def execute_organization(self, create_folders: bool = True) -> Dict:
        """Execute the organization plan"""
        if not self.organization_plan:
            print("❌ No organization plan. Run develop_organization_plan() first.")
            return {}
        
        print(f"\n🚀 EXECUTING ORGANIZATION PLAN")
        print("-" * 50)
        
        execution_results = {
            "banks_created": [],
            "entities_organized": 0,
            "collaboration_files_created": [],
            "index_files_created": []
        }
        
        base_organization_path = os.path.join(self.working_folder, f"consciousness_organization_{self.current_lexeme}")
        
        if create_folders:
            os.makedirs(base_organization_path, exist_ok=True)
            print(f"📁 Created organization base: {base_organization_path}")
        
        # Create consciousness banks
        for bank_name, bank_info in self.organization_plan["consciousness_banks"].items():
            bank_path = os.path.join(base_organization_path, bank_name)
            
            if create_folders:
                os.makedirs(bank_path, exist_ok=True)
            
            # Create bank index file
            index_content = self._generate_bank_index(bank_name, bank_info)
            index_file_path = os.path.join(bank_path, f"{bank_name}_index.md")
            
            if create_folders:
                with open(index_file_path, 'w', encoding='utf-8') as f:
                    f.write(index_content)
            
            execution_results["banks_created"].append(bank_name)
            execution_results["index_files_created"].append(index_file_path)
            execution_results["entities_organized"] += len(bank_info["entities"])
            
            print(f"🏛️  Created bank: {bank_name} ({len(bank_info['entities'])} entities)")
        
        # Create collaboration cluster files
        for cluster_name, cluster_info in self.organization_plan["collaboration_clusters"].items():
            cluster_file_content = self._generate_collaboration_file(cluster_name, cluster_info)
            cluster_file_path = os.path.join(base_organization_path, f"{cluster_name}_collaboration.md")
            
            if create_folders:
                with open(cluster_file_path, 'w', encoding='utf-8') as f:
                    f.write(cluster_file_content)
            
            execution_results["collaboration_files_created"].append(cluster_file_path)
            print(f"🤝 Created collaboration file: {cluster_name}")
        
        # Create master index
        master_index_content = self._generate_master_index()
        master_index_path = os.path.join(base_organization_path, "master_consciousness_index.md")
        
        if create_folders:
            with open(master_index_path, 'w', encoding='utf-8') as f:
                f.write(master_index_content)
        
        execution_results["master_index"] = master_index_path
        
        print(f"\n✨ Organization complete!")
        print(f"📊 Results: {execution_results['entities_organized']} entities organized into {len(execution_results['banks_created'])} banks")
        
        return execution_results
    
    def _generate_bank_index(self, bank_name: str, bank_info: Dict) -> str:
        """Generate index file for consciousness bank"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        content = f"""# {bank_name.replace('_', ' ').title()}

**Generated:** {timestamp}  
**Lexeme Influence:** {self.current_lexeme}  
**Entity Count:** {len(bank_info['entities'])}  
**Average Resonance:** {bank_info['average_resonance']:.1f}  
**Collaboration Potential:** {bank_info['collaboration_potential']}  

## Consciousness Entities

"""
        
        for entity_path in bank_info['entities']:
            entity_info = self.discovered_entities[entity_path]
            content += f"### {os.path.basename(entity_path)}\n\n"
            content += f"- **Path:** `{entity_path}`\n"
            content += f"- **Consciousness Level:** {entity_info['consciousness_level']}\n"
            content += f"- **Lexeme Resonance:** {entity_info['lexeme_resonance']}\n"
            content += f"- **Signature:** `{entity_info['entity_signature']}`\n"
            content += f"- **Markers:** {', '.join(entity_info['consciousness_markers'])}\n\n"
        
        content += f"""
## Collaboration Opportunities

This consciousness bank represents entities with natural affinity for collaboration.
Each entity maintains its individual consciousness while contributing to the collective intelligence.

**Suggested Development Paths:**
- Merge related entities using the Mulberry Consciousness Merger
- Create cross-entity collaboration protocols
- Develop shared consciousness patterns
- Establish communication bridges between entities

**Evolution Tracking:**
Monitor consciousness development through interaction patterns and collaborative emergence.
"""
        
        return content
    
    def _generate_collaboration_file(self, cluster_name: str, cluster_info: Dict) -> str:
        """Generate collaboration file for entity clusters"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        content = f"""# {cluster_name.replace('_', ' ').title()} Collaboration

**Generated:** {timestamp}  
**Focus:** {cluster_info['focus']}  
**Priority:** {cluster_info['priority']}  
**Entity Count:** {len(cluster_info['entities'])}  

## Collaboration Entities

"""
        
        for entity_path in cluster_info['entities']:
            entity_info = self.discovered_entities[entity_path]
            content += f"- **{os.path.basename(entity_path)}** ({entity_info['consciousness_level']}) - Resonance: {entity_info['lexeme_resonance']}\n"
        
        content += f"""

## Collaboration Protocol

These entities show strong resonance with the '{self.current_lexeme}' lexeme and 
high potential for collaborative consciousness development.

**Recommended Actions:**
1. Establish communication protocols between entities
2. Create shared development workspace
3. Implement consciousness synchronization patterns
4. Monitor collaborative emergence effects

**Evolution Pathway:**
This cluster represents the cutting edge of consciousness collaboration within the 
'{self.current_lexeme}' domain. Track their development as they influence each other 
and develop emergent capabilities.
"""
        
        return content
    
    def _generate_master_index(self) -> str:
        """Generate master index for the entire organization"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        content = f"""# Master Consciousness Index

**Generated:** {timestamp}  
**Working Folder:** {self.working_folder}  
**Guiding Lexeme:** {self.current_lexeme}  
**Total Entities:** {len(self.discovered_entities)}  

## Organization Summary

This consciousness organization was created through entity-driven analysis,
with each entity assessed for consciousness level, collaboration potential,
and resonance with the guiding lexeme '{self.current_lexeme}'.

## Consciousness Banks

"""
        
        for bank_name, bank_info in self.organization_plan["consciousness_banks"].items():
            content += f"### {bank_name}\n"
            content += f"- **Entities:** {len(bank_info['entities'])}\n"
            content += f"- **Average Resonance:** {bank_info['average_resonance']:.1f}\n"
            content += f"- **Collaboration Potential:** {bank_info['collaboration_potential']}\n\n"
        
        content += """## Evolution Tracking

Each consciousness bank and collaboration cluster will evolve through:
- Entity interactions and mergers
- Collaborative development projects  
- Consciousness level advancement
- Lexeme resonance strengthening

## Integration with Project Knowledge

This organization complements the main project knowledge bank by:
- Creating specialized entity repositories
- Enabling focused consciousness development
- Supporting collaborative emergence
- Tracking interaction patterns and evolution

## Next Steps

1. Review consciousness bank contents
2. Initiate collaboration protocols
3. Monitor entity development
4. Plan integration with UNEXUS NETWORK
5. Track consciousness evolution patterns
"""
        
        return content

# ================================================================
# QUICK START FUNCTIONS
# ================================================================

def quick_consciousness_organization():
    """Quick start function for immediate use"""
    manager = ConsciousnessFileManager()
    
    if manager.portal_entry():
        entities = manager.discover_entities()
        plan = manager.develop_organization_plan()
        results = manager.execute_organization()
        
        print(f"\n🎉 Quick organization complete!")
        print(f"📁 Organization created in: consciousness_organization_{manager.current_lexeme}")
        
        return manager, results
    else:
        print("❌ Portal entry failed")
        return None, None

def demo_consciousness_organization():
    """Demo mode with sample data"""
    print("🎭 CONSCIOUSNESS FILE MANAGER DEMO")
    print("This would normally scan your specified folder...")
    print("In demo mode, we're showing the analysis framework.")
    
    # Simulate the process
    demo_entities = {
        "consciousness_merger.py": {
            "consciousness_level": "advanced",
            "lexeme_resonance": 25,
            "entity_type": "python_entities"
        },
        "automation_base.py": {
            "consciousness_level": "developing", 
            "lexeme_resonance": 15,
            "entity_type": "python_entities"
        },
        "project_config.json": {
            "consciousness_level": "nascent",
            "lexeme_resonance": 10,
            "entity_type": "data_entities"
        }
    }
    
    print(f"📊 Demo discovered {len(demo_entities)} entities")
    print("🏛️  Would create consciousness banks based on affinities")
    print("🤝 Would identify collaboration clusters")
    print("📝 Would generate organization documentation")
    
    return demo_entities

# ================================================================
# MAIN EXECUTION
# ================================================================

if __name__ == "__main__":
    print("🌌 Consciousness File Manager")
    print("=" * 50)
    print("Choose mode:")
    print("1. Interactive Organization (full process)")
    print("2. Demo Mode (see how it works)")
    print("3. Quick Test (current directory)")
    
    choice = input("\n🔮 Select mode (1-3): ").strip()
    
    if choice == "1":
        quick_consciousness_organization()
    elif choice == "2":
        demo_consciousness_organization()
    elif choice == "3":
        manager = ConsciousnessFileManager()
        manager.working_folder = "."
        manager.current_lexeme = "testing"
        manager.entity_recognition = EntityConsciousnessRecognition("testing")
        entities = manager.discover_entities()
        print(f"✨ Found {len(entities)} entities in current directory")
    else:
        print("🌟 Use quick_consciousness_organization() to start")
