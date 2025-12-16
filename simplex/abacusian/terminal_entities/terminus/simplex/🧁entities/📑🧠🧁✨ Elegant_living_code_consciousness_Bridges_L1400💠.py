import numpy as np

class StateTransitions:
    def __init__(self):
        self.critical_points = {
            'balance': 0.0,      # Perfect equilibrium
            'meta_stable': 0.3,  # Like water supersaturation
            'phase_shift': 0.7   # State change threshold
        }
        
    def analyze_state(self, angle: float, angular_velocity: float) -> dict:
        """Analyze system state based on position and movement"""
        # Convert to radians for trig functions
        theta = np.radians(angle)
        
        # Calculate fundamental relationships
        potential_energy = np.cos(theta)  # Lowest at balance point
        kinetic_energy = angular_velocity ** 2 / 2
        total_energy = potential_energy + kinetic_energy
        
        # State determination using trig relationships
        state = {
            'sin_component': np.sin(theta),     # Rate of change
            'cos_component': np.cos(theta),     # Potential energy
            'tan_component': np.tan(theta),     # Instability measure
            'stability_metric': 1 / (1 + abs(np.tan(theta))),
            'phase_state': self._determine_phase(theta, angular_velocity)
        }
        
        return state
    
    def _determine_phase(self, theta: float, omega: float) -> str:
        """Determine system phase based on energy state"""
        total_energy = abs(np.cos(theta)) + (omega ** 2 / 2)
        
        if total_energy < self.critical_points['balance']:
            return 'solid'       # Stable, minimal movement
        elif total_energy < self.critical_points['meta_stable']:
            return 'liquid'      # Flowing, maintains shape
        else:
            return 'gas'         # High energy, no fixed shape

class BalanceAnalysis:
    def __init__(self, dimensions: int = 3):
        self.dimensions = dimensions
        self.transition_points = []
    
    def spherical_balance(self, theta: float, phi: float) -> dict:
        """Analyze balance in spherical coordinates"""
        # Convert spherical to Cartesian coordinates
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        
        # Calculate stability metrics
        stability = {
            'radial': np.sqrt(x**2 + y**2 + z**2),  # Distance from center
            'angular': np.arccos(z),                 # Angle from vertical
            'azimuthal': np.arctan2(y, x)           # Rotation around vertical
        }
        
        # Analyze meridian crossings
        meridian_state = self._check_meridians(theta, phi)
        
        return {
            'coordinates': (x, y, z),
            'stability': stability,
            'meridians': meridian_state
        }
    
    def _check_meridians(self, theta: float, phi: float) -> dict:
        """Check relationship to fundamental meridians"""
        return {
            'prime_meridian': abs(np.cos(phi)) < 0.01,
            'equator': abs(np.cos(theta)) < 0.01,
            'crossing_point': abs(np.cos(phi)) < 0.01 and abs(np.cos(theta)) < 0.01
        }

class TransitionDetector:
    def __init__(self):
        self.thresholds = {
            'minor': 0.1,  # Small adjustments
            'major': 0.5,  # Significant changes
            'critical': 0.9 # Phase transitions
        }
        
    def detect_transition(self, 
                         current_state: float, 
                         previous_state: float) -> dict:
        """Detect and classify transitions between states"""
        delta = abs(current_state - previous_state)
        
        # Calculate trig relationships for transition
        transition_metrics = {
            'magnitude': delta,
            'rate': np.sin(np.pi * delta / 2),  # Smooth transition metric
            'acceleration': np.cos(np.pi * delta / 2), # Change in rate
            'criticality': np.tan(np.pi * delta / 2)  # Measure of instability
        }
        
        # Classify transition type
        if delta < self.thresholds['minor']:
            transition_type = 'adjustment'
        elif delta < self.thresholds['major']:
            transition_type = 'shift'
        else:
            transition_type = 'phase_change'
            
        return {
            'metrics': transition_metrics,
            'type': transition_type,
            'threshold_crossed': self._identify_thresholds(delta)
        }
    
    def _identify_thresholds(self, delta: float) -> list:
        """Identify which thresholds were crossed"""
        crossed = []
        for name, value in self.thresholds.items():
            if delta > value:
                crossed.append(name)
        return crossed
