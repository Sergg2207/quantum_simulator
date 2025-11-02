import numpy as np
from .core import QuantumSystem

class Observable:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=complex)
        self._check_hermitian()
    
    def _check_hermitian(self):
        """Verifica si la matriz es hermitiana"""
        if not np.allclose(self.matrix, self.matrix.conj().T):
            raise ValueError("La matriz del observable debe ser hermitiana")
    
    def mean(self, state):
        """Calcula la media del observable en estado dado"""
        state_vector = np.array(state, dtype=complex).reshape(-1, 1)
        
        # <ψ|O|ψ>
        mean_value = state_vector.conj().T @ self.matrix @ state_vector
        return mean_value[0, 0].real  # Debe ser real para matrices hermitianas
    
    def variance(self, state):
        """Calcula la varianza del observable en estado dado"""
        state_vector = np.array(state, dtype=complex).reshape(-1, 1)
        
        # <ψ|O²|ψ>
        O_squared = self.matrix @ self.matrix
        mean_O_squared = state_vector.conj().T @ O_squared @ state_vector
        mean_O_squared = mean_O_squared[0, 0].real
        
        # <ψ|O|ψ>²
        mean_O = self.mean(state)
        
        variance = mean_O_squared - mean_O**2
        return variance
    
    def eigenvalues_eigenvectors(self):
        """Calcula valores y vectores propios del observable"""
        eigenvalues, eigenvectors = np.linalg.eigh(self.matrix)
        return eigenvalues, eigenvectors
    
    def probability_eigenvalue(self, state, eigenvalue_index):
        """Probabilidad de colapsar a un vector propio especifico despues de medir"""
        eigenvalues, eigenvectors = self.eigenvalues_eigenvectors()
        
        if eigenvalue_index < 0 or eigenvalue_index >= len(eigenvalues):
            raise ValueError("indice de valor propio invalido")
        
        eigenvector = eigenvectors[:, eigenvalue_index]
        state_vector = np.array(state, dtype=complex)
        
        # |<ψ|φ>|²
        probability = abs(np.vdot(eigenvector, state_vector))**2
        return probability
