import numpy as np

class QuantumDynamics:
    def __init__(self, initial_state):
        self.initial_state = np.array(initial_state, dtype=complex)
        self.current_state = self.initial_state.copy()
    
    def apply_unitary_evolution(self, unitary_matrices):
        """Aplica una serie de matrices unitarias al estado"""
        current_state = self.initial_state.copy()
        
        for U in unitary_matrices:
            # Verificar que la matriz sea unitaria
            if not self._is_unitary(U):
                raise ValueError("Todas las matrices deben ser unitarias")
            
            current_state = U @ current_state
        
        self.current_state = current_state
        return current_state
    
    def _is_unitary(self, matrix):
        """Verifica si una matriz es unitaria"""
        return np.allclose(matrix @ matrix.conj().T, np.eye(len(matrix)))
    
    def get_final_state(self):
        """Retorna el estado final después de la evolución"""
        return self.current_state
