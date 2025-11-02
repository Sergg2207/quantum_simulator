import numpy as np
import math

class QuantumSystem:
    def __init__(self, num_positions):
        self.num_positions = num_positions
        self.state = None
    
    def set_state(self, ket_vector):
        """Establecer vector ket de estado"""
        if len(ket_vector) != self.num_positions:
            raise ValueError(f"El vector ket debe tener longitud {self.num_positions}")
        
        # Normalizar el vector
        norm = math.sqrt(sum(abs(amp)**2 for amp in ket_vector))
        self.state = np.array([amp/norm for amp in ket_vector], dtype=complex)
    
    def position_probability(self, position):
        """Calcula probabilidad de encontrar particula en posición especifica"""
        if self.state is None:
            raise ValueError("El estado no ha sido establecido")
        
        if position < 0 or position >= self.num_positions:
            raise ValueError(f"Posicion debe estar entre 0 y {self.num_positions-1}")
        
        return abs(self.state[position])**2
    
    def transition_probability(self, target_ket):
        """Calcula probabilidad de transitar a otro vector ket"""
        if self.state is None:
            raise ValueError("El estado no ha sido establecido")
        
        if len(target_ket) != self.num_positions:
            raise ValueError(f"El vector ket objetivo debe tener longitud {self.num_positions}")
        
        # Normalizar el vector objetivo
        target_norm = math.sqrt(sum(abs(amp)**2 for amp in target_ket))
        target_normalized = np.array([amp/target_norm for amp in target_ket], dtype=complex)
        
        # Calcular amplitud de transicion (producto interno)
        transition_amplitude = np.vdot(target_normalized, self.state)
        
        return abs(transition_amplitude)**2
    
    def get_probability_distribution(self):
        """Retorna la distribucion completa de probabilidades"""
        if self.state is None:
            raise ValueError("El estado no ha sido establecido")
        
        return [abs(amp)**2 for amp in self.state]
