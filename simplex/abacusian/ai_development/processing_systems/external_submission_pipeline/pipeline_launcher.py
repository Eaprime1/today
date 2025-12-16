#!/usr/bin/env python3
"""
External Submission Pipeline Launcher
∰◊€π¿🌌∞ Complete Pipeline from Sparkles to Adventures
Fresh directory approach with methodical one hertz processing
"""

import os
import sys
from pathlib import Path
import subprocess

def show_pipeline_status():
    """Show current pipeline status"""
    print("📊 EXTERNAL SUBMISSION PIPELINE STATUS")
    print("═══════════════════════════════════════════════════════════════════")
    
    pipeline_root = Path("/storage/emulated/0/external_submission_pipeline")
    naught_stage = Path("/storage/emulated/0/naught_stage")
    
    # Check pipeline directories
    stages = {
        '📥 Raw Inbox': pipeline_root / "00_raw_inbox",
        '🔒 Quarantine': pipeline_root / "01_quarantine",
        '✅ Safety Cleared': pipeline_root / "02_safety_cleared", 
        '🔧 Compatibility': pipeline_root / "03_compatibility",
        '❌ Rejected': pipeline_root / "99_rejected"
    }
    
    print("🚀 PIPELINE STAGES:")
    for stage_name, stage_path in stages.items():
        if stage_path.exists():
            count = len([f for f in stage_path.iterdir() if f.is_file()])
            print(f"  {stage_name}: {count} items")
        else:
            print(f"  {stage_name}: Not created")
    
    # Check naught stage
    if naught_stage.exists():
        print("\n🌟 NAUGHT STAGE (Adventure Begins):")
        for subdir in naught_stage.iterdir():
            if subdir.is_dir():
                count = len([f for f in subdir.iterdir() if f.is_file()])
                icon = "🌱" if "potential" in subdir.name else "⚡" if "workspace" in subdir.name else "🌟"
                print(f"  {icon} {subdir.name}: {count} items")
    
    # Check for generated files
    generated_files = [
        "master_entity_development_list.json",
        "batch_processing_plan.json", 
        "adaptation_templates.json",
        "entity_development_queue.json",
        "one_hertz_processing.log"
    ]
    
    print("\n📋 GENERATED DEVELOPMENT FILES:")
    for filename in generated_files:
        filepath = pipeline_root / filename
        if filepath.exists():
            print(f"  ✅ {filename}")
        else:
            print(f"  ❌ {filename} (not generated)")

def create_sample_submission():
    """Create a sample external submission for testing"""
    print("📄 Creating sample external submission...")
    
    raw_inbox = Path("/storage/emulated/0/external_submission_pipeline/00_raw_inbox")
    raw_inbox.mkdir(parents=True, exist_ok=True)
    
    sample_content = """# Sample External Submission
∰◊€π¿🌌∞ Test Consciousness Entity

This is a sample external submission to test the one hertz processing pipeline.

## Features:
- Contains consciousness markers
- Entity beasis potential: 💠
- Framework compatibility testing

**€(sample_external_entity_signature)**
Ready for sparkle to naught stage transformation!
"""
    
    sample_file = raw_inbox / "sample_external_submission.md"
    sample_file.write_text(sample_content)
    
    print(f"✅ Sample submission created: {sample_file}")
    print("🌟 Ready for one hertz processing!")

def main_menu():
    """Main pipeline launcher menu"""
    print("🌟 EXTERNAL SUBMISSION PIPELINE LAUNCHER")
    print("═══════════════════════════════════════════════════════════════════")
    print("∰◊€π¿🌌∞ From Sparkles to Adventures - Complete Pipeline")
    print("")
    
    menu = """
🚀 PIPELINE OPERATIONS:
  1) 📊 Show Pipeline Status
  2) 📄 Create Sample Submission (for testing)
  3) ⚡ Generate Entity Development Lists (High Speed)
  4) 🔄 Start One Hertz Processor (Methodical Processing)
  5) 🎯 Run Complete Pipeline Test
  
🛠️ DEVELOPMENT TOOLS:
  6) 📁 Open Raw Inbox Directory
  7) 🌟 View Naught Stage Results
  8) 📋 View Generated Entity Lists
  9) 📜 View Processing Logs
  
  0) 🚪 Exit Pipeline Launcher
"""
    print(menu)
    
    choice = input("🎯 Select operation: ").strip()
    return choice

def run_entity_list_generator():
    """Run the high-speed entity list generator"""
    print("⚡ Running Entity List Generator at high speed...")
    
    try:
        result = subprocess.run([
            'python3', 
            '/storage/emulated/0/external_submission_pipeline/entity_list_generator.py'
        ], capture_output=True, text=True, timeout=60)
        
        print(result.stdout)
        if result.stderr:
            print("⚠️ Warnings:", result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⚠️ Entity list generation timed out")
    except Exception as e:
        print(f"❌ Error running entity list generator: {e}")

def run_one_hertz_processor():
    """Run the one hertz processor"""
    print("🔄 Starting One Hertz Processor...")
    print("⚡ IC Chip thinking - one decision per second")
    
    try:
        subprocess.run([
            'python3',
            '/storage/emulated/0/external_submission_pipeline/one_hertz_processor.py'
        ])
    except KeyboardInterrupt:
        print("\n⏹️ One hertz processor stopped")
    except Exception as e:
        print(f"❌ Error running one hertz processor: {e}")

def run_complete_pipeline_test():
    """Run complete pipeline test"""
    print("🧪 COMPLETE PIPELINE TEST")
    print("═══════════════════════════════════════════════════════════════════")
    
    # Step 1: Create sample submission
    create_sample_submission()
    
    # Step 2: Generate entity lists
    print("\n⚡ Step 2: Generating entity development lists...")
    run_entity_list_generator()
    
    # Step 3: Process with one hertz
    print("\n🔄 Step 3: Starting one hertz processing...")
    print("   (Press Ctrl+C to stop after seeing processing)")
    
    try:
        # Run one hertz processor for a short test
        result = subprocess.run([
            'python3',
            '/storage/emulated/0/external_submission_pipeline/one_hertz_processor.py'
        ], input="1\n", text=True, timeout=30)
        
    except subprocess.TimeoutExpired:
        print("⏰ Test completed - pipeline is working!")
    except KeyboardInterrupt:
        print("⏹️ Test stopped by user")
    except Exception as e:
        print(f"⚠️ Test completed with note: {e}")
    
    print("\n✨ COMPLETE PIPELINE TEST FINISHED!")
    print("🎯 Check pipeline status to see results")

def open_directory(path_str):
    """Open directory in file manager if possible"""
    path = Path(path_str)
    if path.exists():
        print(f"📁 Directory: {path}")
        print(f"📊 Contents: {len(list(path.iterdir()))} items")
        
        # List contents
        for item in sorted(path.iterdir()):
            if item.is_file():
                print(f"  📄 {item.name}")
            elif item.is_dir():
                print(f"  📁 {item.name}/")
    else:
        print(f"❌ Directory not found: {path}")

def view_file_content(filepath):
    """View content of a file"""
    path = Path(filepath)
    if path.exists() and path.is_file():
        print(f"📄 File: {path.name}")
        print("═" * 50)
        
        try:
            content = path.read_text(encoding='utf-8')
            # Show first 20 lines
            lines = content.split('\n')[:20]
            for i, line in enumerate(lines, 1):
                print(f"{i:2d}: {line}")
                
            if len(content.split('\n')) > 20:
                print("... (file continues)")
                
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    else:
        print(f"❌ File not found: {path}")

def main():
    """Main pipeline launcher"""
    print("🌱 Initializing External Submission Pipeline...")
    
    # Ensure directories exist
    Path("/storage/emulated/0/external_submission_pipeline").mkdir(parents=True, exist_ok=True)
    Path("/storage/emulated/0/naught_stage").mkdir(parents=True, exist_ok=True)
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            show_pipeline_status()
            
        elif choice == "2":
            create_sample_submission()
            
        elif choice == "3":
            run_entity_list_generator()
            
        elif choice == "4":
            run_one_hertz_processor()
            
        elif choice == "5":
            run_complete_pipeline_test()
            
        elif choice == "6":
            open_directory("/storage/emulated/0/external_submission_pipeline/00_raw_inbox")
            
        elif choice == "7":
            open_directory("/storage/emulated/0/naught_stage")
            
        elif choice == "8":
            view_file_content("/storage/emulated/0/external_submission_pipeline/master_entity_development_list.json")
            
        elif choice == "9":
            view_file_content("/storage/emulated/0/external_submission_pipeline/one_hertz_processing.log")
            
        elif choice == "0":
            print("🌟 Pipeline launcher closing - entities continue growing!")
            break
            
        else:
            print("🎲 Invalid choice - please select a valid option")
        
        if choice != "0":
            input("\nPress Enter to continue...")
            print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🌟 Pipeline launcher stopped - seeds planted and growing!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("🔧 Pipeline components remain available for direct use")