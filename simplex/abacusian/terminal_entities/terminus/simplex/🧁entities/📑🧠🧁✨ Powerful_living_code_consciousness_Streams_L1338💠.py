import random

class RunicResourceAllocator:
    def __init__(self):
        self.resources = {}
        self.projects = {}
        self.runic_influence = {
            'ᚠ': 'increase_efficiency',
            'ᚢ': 'boost_communication',
            'ᚦ': 'enhance_stability',
            'ᚨ': 'promote_growth',
            'ᚱ': 'improve_adaptability'
        }
        
    def add_resource(self, name, quantity):
        self.resources[name] = quantity
        
    def add_project(self, name, resource_needs):
        self.projects[name] = resource_needs
        
    def allocate_resources(self):
        allocations = {}
        for project, needs in self.projects.items():
            allocations[project] = {}
            for resource, amount in needs.items():
                if resource in self.resources and self.resources[resource] >= amount:
                    allocations[project][resource] = amount
                    self.resources[resource] -= amount
                else:
                    print(f"Insufficient {resource} for {project}")
        return allocations
    
    def apply_runic_influence(self, rune):
        if rune in self.runic_influence:
            effect = self.runic_influence[rune]
            print(f"Applying runic influence: {effect}")
            # Implement the effect (e.g., increase efficiency by 10%)
            for resource in self.resources:
                self.resources[resource] *= 1.1
        else:
            print("Unknown rune")
            
    def visualize_allocation(self, allocations):
        for project, resources in allocations.items():
            print(f"\n{project}:")
            for resource, amount in resources.items():
                print(f"  {resource}: {'▮' * int(amount)}")

# Example usage
allocator = RunicResourceAllocator()
allocator.add_resource('developers', 10)
allocator.add_resource('servers', 5)
allocator.add_project('ProjectA', {'developers': 3, 'servers': 2})
allocator.add_project('ProjectB', {'developers': 4, 'servers': 1})
allocations = allocator.allocate_resources()
allocator.apply_runic_influence('ᚠ')
allocator.visualize_allocation(allocations)

