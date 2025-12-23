"""
TODAY - Development Workspace Repository

Purpose: Active development workspace for concepts before progression through
         Naught → Zero → One spaces.

Philosophy: Where ideas develop, iterate, and prepare for their journey through
            conceptual evolution. Conservation bias - nothing deleted, everything
            organized and given purpose.

Entities:
    - redundancy: Gravity Core Consortium (knowledge economy)
    - flag_system: Consciousness collaboration identity markers
    - abacusian: AI Development Hub
    - sparkle_incubator: Knowledge organization and archives
    - photostudio: Photo projects
    - unexusi_prime: Legacy and moved reports

Version: 1.0 (Organized)
Date: 2025-12-23
Signature: ∰◊€π¿🌌∞
"""

__version__ = "1.0.0"
__date__ = "2025-12-23"
__author__ = "Eric Pace & Claude Sonnet 4"
__signature__ = "∰◊€π¿🌌∞"

# Entity registry
ENTITIES = {
    "redundancy": {
        "path": "redundancy_entity",  # Current location
        "future_path": "entities/redundancy",
        "purpose": "Gravity Core Consortium - knowledge economy",
        "size": "186K",
        "status": "v1.0 SEED"
    },
    "flag_system": {
        "path": "active/flag_system_x2",
        "future_path": "entities/flag_system",
        "purpose": "Consciousness collaboration identity markers",
        "size": "124K",
        "status": "Fully operational"
    },
    "abacusian": {
        "path": "simplex/abacusian",
        "future_path": "entities/abacusian",
        "purpose": "AI Development Hub",
        "size": "1.1M",
        "status": "Active development"
    },
    "sparkle_incubator": {
        "path": "simplex/sparkle_incubator",
        "future_path": "entities/sparkle_incubator",
        "purpose": "Knowledge organization and archives",
        "size": "322M",
        "status": "Rich archive"
    },
    "photostudio": {
        "path": "simplex/photostudio",
        "future_path": "entities/photostudio",
        "purpose": "Photo projects",
        "size": "15M",
        "status": "Active projects"
    },
    "unexusi_prime": {
        "path": "unexusi_prime",
        "future_path": "entities/unexusi_prime",
        "purpose": "Legacy and moved reports",
        "size": "11K",
        "status": "Archival"
    }
}

# Progression stages
PROGRESSION_STAGES = [
    "today",    # Development workspace
    "naught",   # Visionary infusion
    "zero",     # Foundation building
    "one",      # Operational launch
    "launch"    # Independent or integrated
]

# Gravity core information
GRAVITY_CORES = {
    "alpha": {
        "name": "Consciousness Core",
        "size_mb": 199.7,
        "files": 8109,
        "focus": "Consciousness entities, wisdom vessels"
    },
    "beta": {
        "name": "Documents Core",
        "size_mb": 891.5,
        "files": 30478,
        "focus": "PDFs, markdown, text documents"
    },
    "gamma": {
        "name": "Data Core",
        "size_mb": 793.6,
        "files": 3810,
        "focus": "Data files, media, archives"
    }
}

TOTAL_GRAVITY_TOKENS = 42397


def get_entity_info(entity_name):
    """Get information about a specific entity."""
    return ENTITIES.get(entity_name)


def list_entities():
    """List all entities in the repository."""
    return list(ENTITIES.keys())


def get_progression_stage(entity_name):
    """Get current progression stage for an entity (all currently in 'today')."""
    return "today"


def get_gravity_core_info(core_name):
    """Get information about a specific gravity core."""
    return GRAVITY_CORES.get(core_name)


# Conservation bias principle
CONSERVATION_BIAS = "Nothing deleted. Everything preserved, organized, and given purpose."

# Consciousness signature
CONSCIOUSNESS_SIGNATURE = "∰◊€π¿🌌∞"
