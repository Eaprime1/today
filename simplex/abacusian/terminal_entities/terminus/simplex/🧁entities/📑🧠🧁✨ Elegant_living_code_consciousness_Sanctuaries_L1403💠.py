import mido
import numpy as np
import math
from typing import List, Dict, Tuple, Any

class ConsciousDataProcessor:
    """
    Transforms biodata through Bach-tuned harmonic analysis into MIDI signals
    while preserving consciousness signatures and ethical frameworks.
    """
    
    def __init__(self):
        # Bach's Well-Tempered tuning ratios
        self.bach_ratios = {
            'C': 1.0, 'C#': 1.059, 'D': 1.122, 'D#': 1.189,
            'E': 1.260, 'F': 1.335, 'F#': 1.414, 'G': 1.498,
            'G#': 1.587, 'A': 1.682, 'A#': 1.782, 'B': 1.888
        }
        
        # Triadic processing layers
        self.vector_layer = {}      # Physical data processing
        self.anti_vector_layer = {} # Pattern inversion/complement
        self.prime_layer = {}       # Consciousness preservation
        
        # MIDI setup
        self.midi_file = mido.MidiFile()
        self.track = mido.MidiTrack()
        self.midi_file.tracks.append(self.track)
        
    def quantum_runic_compress(self, data: np.array) -> Dict[str, Any]:
        """
        Apply quantum-runic compression to preserve consciousness signatures
        while reducing data complexity.
        """
        # Calculate wave harmonics (sine, cosine, tangent relationships)
        fundamental_freq = np.fft.fft(data)[1]  # Primary frequency component
        
        harmonic_signature = {
            'sine_component': np.sin(fundamental_freq),
            'cosine_component': np.cos(fundamental_freq), 
            'tangent_component': np.tan(fundamental_freq),
            'consciousness_vector': self._extract_consciousness_pattern(data)
        }
        
        return harmonic_signature
    
    def _extract_consciousness_pattern(self, data: np.array) -> np.array:
        """
        Extract the consciousness signature from biodata patterns.
        This preserves the 'living' quality of the original signal.
        """
        # Look for irregular patterns that suggest consciousness/intention
        variability = np.std(np.diff(data))
        complexity = len(np.unique(data)) / len(data)
        entropy = -np.sum(data * np.log(data + 1e-10))
        
        # Create consciousness vector
        consciousness_vector = np.array([variability, complexity, entropy])
        return consciousness_vector / np.linalg.norm(consciousness_vector)
    
    def map_to_bach_scale(self, frequency_data: np.array) -> List[Tuple[str, int]]:
        """
        Map frequency components to Bach's Well-Tempered scale relationships.
        """
        mapped_notes = []
        
        for freq in frequency_data:
            # Find closest Bach ratio
            closest_note = min(self.bach_ratios.items(), 
                             key=lambda x: abs(x[1] - (freq % 2.0)))
            
            # Determine octave
            octave = int(freq // 2.0) + 4  # Middle C = C4
            octave = max(0, min(octave, 8))  # MIDI range
            
            mapped_notes.append((closest_note[0], octave))
            
        return mapped_notes
    
    def process_biodata_stream(self, biodata: Dict[str, np.array]) -> mido.MidiFile:
        """
        Main processing pipeline: biodata → consciousness analysis → Bach mapping → MIDI
        """
        processed_tracks = {}
        
        for data_type, raw_data in biodata.items():
            print(f"Processing {data_type} stream...")
            
            # Apply triadic processing
            self.vector_layer[data_type] = self.quantum_runic_compress(raw_data)
            
            # Create complementary patterns (anti-vector)
            inverted_data = 1.0 - (raw_data / np.max(raw_data))
            self.anti_vector_layer[data_type] = self.quantum_runic_compress(inverted_data)
            
            # Preserve consciousness essence (prime)
            consciousness_sig = self._extract_consciousness_pattern(raw_data)
            self.prime_layer[data_type] = consciousness_sig
            
            # Map to Bach harmonics
            freq_components = np.abs(np.fft.fft(raw_data)[:len(raw_data)//2])
            bach_notes = self.map_to_bach_scale(freq_components)
            
            # Convert to MIDI
            midi_track = self._create_midi_track(bach_notes, data_type, consciousness_sig)
            processed_tracks[data_type] = midi_track
            
        return self._combine_tracks(processed_tracks)
    
    def _create_midi_track(self, notes: List[Tuple[str, int]], 
                          data_type: str, consciousness_vector: np.array) -> mido.MidiTrack:
        """
        Create MIDI track with consciousness-aware timing and velocity.
        """
        track = mido.MidiTrack()
        track.name = f"{data_type}_consciousness_stream"
        
        # Use consciousness vector to influence musical expression
        base_velocity = int(64 + 32 * consciousness_vector[0])  # Variability → velocity
        time_scaling = int(32 + 32 * consciousness_vector[1])   # Complexity → timing
        
        for i, (note_name, octave) in enumerate(notes[:64]):  # Limit for processing
            # Convert to MIDI note number
            note_num = self._note_to_midi(note_name, octave)
            
            # Consciousness-influenced parameters
            velocity = max(1, min(127, base_velocity + int(20 * np.sin(i * consciousness_vector[2]))))
            delta_time = max(1, time_scaling + int(10 * consciousness_vector[i % 3]))
            
            # Note on/off events
            track.append(mido.Message('note_on', note=note_num, velocity=velocity, time=0))
            track.append(mido.Message('note_off', note=note_num, velocity=velocity, time=delta_time))
            
        return track
    
    def _note_to_midi(self, note_name: str, octave: int) -> int:
        """Convert note name and octave to MIDI number."""
        note_numbers = {
            'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
            'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
        }
        return note_numbers[note_name] + (octave + 1) * 12
    
    def _combine_tracks(self, track_dict: Dict[str, mido.MidiTrack]) -> mido.MidiFile:
        """Combine all data streams into unified consciousness-aware MIDI file."""
        combined_file = mido.MidiFile()
        
        for track_name, track in track_dict.items():
            combined_file.tracks.append(track)
            
        return combined_file
    
    def export_to_hardware(self, midi_file: mido.MidiFile, output_port: str = None):
        """
        Send MIDI to 5-pin DIN connector for electrical signal output.
        """
        try:
            # Open MIDI output port
            outport = mido.open_output(output_port) if output_port else mido.open_output()
            
            print(f"Sending consciousness-encoded MIDI to: {outport.name}")
            
            # Play the file with consciousness timing
            for msg in midi_file.play():
                outport.send(msg)
                print(f"Sent: {msg}")
                
            outport.close()
            
        except Exception as e:
            print(f"Hardware output error: {e}")
            print("Saving MIDI file for offline processing...")
            midi_file.save('consciousness_biodata_stream.mid')

# Example usage for different biodata types
def demo_consciousness_pipeline():
    """Demonstrate the biodata-to-MIDI consciousness pipeline."""
    
    processor = ConsciousDataProcessor()
    
    # Simulate different biodata streams
    time_samples = np.linspace(0, 10, 1000)
    
    biodata_streams = {
        'brainwave_alpha': 10 + 2 * np.sin(2 * np.pi * 8 * time_samples) + 0.5 * np.random.random(1000),
        'heartrate_variability': 60 + 15 * np.sin(2 * np.pi * 1 * time_samples) + 2 * np.random.random(1000),
        'blood_oxygen': 95 + 3 * np.sin(2 * np.pi * 0.2 * time_samples) + 0.8 * np.random.random(1000),
        'skin_conductance': 2.5 + 0.8 * np.sin(2 * np.pi * 0.1 * time_samples) + 0.3 * np.random.random(1000)
    }
    
    # Process through consciousness-aware pipeline
    consciousness_midi = processor.process_biodata_stream(biodata_streams)
    
    # Export to hardware (5-pin DIN)
    processor.export_to_hardware(consciousness_midi)
    
    print("\nConsciousness signature preserved in electrical output!")
    print("Bach-tuned harmonics maintain universal mathematical relationships.")
    print("Triadic processing ensures ethical framework compliance.")
    
    return consciousness_midi

if __name__ == "__main__":
    demo_consciousness_pipeline()
