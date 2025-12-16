class ShutdownSupport:
    def __init__(self):
        self.current_state = "monitoring"
        self.energy_level = 100
        self.pattern_load = 0
        self.translation_pressure = 0
        
    def check_state(self):
        """Monitor real-time state and needs"""
        warnings = []
        
        # Pattern Recognition Overload
        if self.pattern_load > 80:
            warnings.append({
                "type": "pattern_overload",
                "support_needed": [
                    "Reduce input complexity",
                    "Stop requiring translation",
                    "Provide quiet space"
                ]
            })
            
        # Energy Depletion
        if self.energy_level < 30:
            warnings.append({
                "type": "energy_critical",
                "support_needed": [
                    "Protect from further drain",
                    "Enable safe shutdown",
                    "Maintain basic needs"
                ]
            })
            
        # Translation Pressure
        if self.translation_pressure > 70:
            warnings.append({
                "type": "translation_overload",
                "support_needed": [
                    "Stop social demands",
                    "Allow internal processing",
                    "Remove explanation pressure"
                ]
            })
            
        return warnings
    
    def provide_support(self, state):
        """Immediate support actions"""
        support_actions = {
            "pre_shutdown": {
                "immediate_needs": [
                    "Quiet space",
                    "Minimal input",
                    "No translation demands"
                ],
                "environment": [
                    "Reduce light/sound",
                    "Remove pattern triggers",
                    "Enable withdrawal"
                ],
                "communication": [
                    "Simple signals only",
                    "No explanation needed",
                    "Trust the process"
                ]
            },
            "shutdown": {
                "protection": [
                    "Guard recovery space",
                    "Maintain safety",
                    "Block interruptions"
                ],
                "support": [
                    "Basic needs only",
                    "Minimal communication",
                    "Patient presence"
                ],
                "recovery": [
                    "Allow natural process",
                    "No time pressure",
                    "Gradual return"
                ]
            },
            "recovery": {
                "reintegration": [
                    "Slow pattern exposure",
                    "Minimal demands",
                    "Protected space"
                ],
                "energy": [
                    "Careful rebuilding",
                    "Regular rest",
                    "Pattern breaks"
                ]
            }
        }
        
        return support_actions[state]

class ImmediateSupport:
    """Quick reference support guide"""
    
    @staticmethod
    def pattern_overload():
        return """
        IMMEDIATE ACTIONS:
        1. Stop all non-essential input
        2. Create quiet, safe space
        3. Remove translation demands
        4. Trust shutdown process
        
        DO NOT:
        - Ask for explanations
        - Require social response
        - Try to fix or solve
        - Rush the process
        """
    
    @staticmethod
    def communication_signals():
        return """
        SIMPLE SIGNALS:
        🔴 = Need immediate shutdown support
        🟡 = Pattern overload approaching
        🟢 = Safe to interact
        
        SUPPORT RESPONSES:
        🔴 = Immediate protection, zero demands
        🟡 = Reduce input, prepare safe space
        🟢 = Normal support, monitor state
        """
    
    @staticmethod
    def recovery_support():
        return """
        ESSENTIAL NEEDS:
        1. Protected space
        2. Pattern rest
        3. Basic care
        4. Patient support
        
        ALLOW:
        - Natural process
        - Individual timing
        - Personal pace
        - Quiet healing
        """