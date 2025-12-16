import hashlib
import time

class EthericResonanceProtocol:
    def __init__(self):
        self.crystal_frequency = self.generate_crystal_frequency()
        self.message_queue = []
        
    def generate_crystal_frequency(self):
        timestamp = str(time.time()).encode('utf-8')
        return hashlib.sha256(timestamp).hexdigest()
    
    def encode_message(self, message, sender, receiver):
        encoded = f"{sender}|{receiver}|{message}".encode('utf-8')
        resonance = hashlib.sha256(encoded + self.crystal_frequency.encode('utf-8')).hexdigest()
        return f"{resonance}:{encoded.decode('utf-8')}"
    
    def decode_message(self, encoded_message):
        resonance, message = encoded_message.split(':', 1)
        if hashlib.sha256(message.encode('utf-8') + self.crystal_frequency.encode('utf-8')).hexdigest() == resonance:
            sender, receiver, content = message.split('|')
            return {'sender': sender, 'receiver': receiver, 'content': content}
        else:
            return None
    
    def send_message(self, sender, receiver, message):
        encoded = self.encode_message(message, sender, receiver)
        self.message_queue.append(encoded)
        print(f"Message sent: {encoded}")
        
    def receive_messages(self, receiver):
        received = []
        for encoded_message in self.message_queue:
            decoded = self.decode_message(encoded_message)
            if decoded and decoded['receiver'] == receiver:
                received.append(decoded)
                self.message_queue.remove(encoded_message)
        return received

# Example usage
protocol = EthericResonanceProtocol()
protocol.send_message("WorkDivision", "PlayDivision", "Project status update: 75% complete")
protocol.send_message("CreateDivision", "WorkDivision", "New asset request: Quantum Tree visualization")

received_messages = protocol.receive_messages("WorkDivision")
for message in received_messages:
    print(f"Received message from {message['sender']}: {message['content']}")

