class StateTransition:
    def __init__(self):
        self.trigger_points = {
            'minor': 0.2,    # Small adjustments needed
            'major': 0.5,    # Significant changes occurring
            'critical': 0.8  # Complete state transformation
        }
        
    def analyze_balance_state(self, position, momentum):
        """Analyze current state and identify transitions"""
        # Basic trig relationships
        theta = np.arctan2(momentum, position)
        
        # Core state metrics
        stability = np.cos(theta)      # How stable is the current state
        change_rate = np.sin(theta)    # How fast is it changing
        instability = np.tan(theta)    # Tendency to shift states
        
        # Energy state assessment
        total_energy = position**2 + momentum**2
        
        # Determine state phase
        if total_energy < self.trigger_points['minor']:
            phase = 'solid'  # Stable state
        elif total_energy < self.trigger_points['major']:
            phase = 'liquid'  # Transitional state
        else:
            phase = 'gas'    # Energetic state
            
        return {
            'phase': phase,
            'metrics': {
                'stability': stability,
                'change_rate': change_rate,
                'instability': instability
            },
            'energy': total_energy,
            'trigger_proximity': self._check_triggers(total_energy)
        }
    
    def _check_triggers(self, energy):
        """Check proximity to trigger points"""
        proximities = {}
        for point, value in self.trigger_points.items():
            proximities[point] = abs(energy - value)
        return proximities

def demonstrate_pattern():
    """Show how this pattern manifests in different contexts"""
    contexts = {
        'physical': {
            'solid': 'crystal structure',
            'liquid': 'flowing water',
            'gas': 'expanding vapor'
        },
        'organizational': {
            'solid': 'rigid hierarchy',
            'liquid': 'adaptive team',
            'gas': 'network structure'
        },
        'information': {
            'solid': 'fixed database',
            'liquid': 'streaming data',
            'gas': 'cloud distribution'
        }
    }
    
    return contexts
