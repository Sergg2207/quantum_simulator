import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from quantum_simulator.observables import Observable
import numpy as np

class TestObservable(unittest.TestCase):
    
    def test_hermitian_check(self):
        # Matriz hermitiana
        hermitian_matrix = [[1, 1j], [-1j, 1]]
        observable = Observable(hermitian_matrix)
        
        # Matriz no hermitiana deberia lanzar error
        non_hermitian = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            Observable(non_hermitian)
    
    def test_mean_calculation(self):
        matrix = [[1, 0], [0, -1]]  # Operador sigma_z
        observable = Observable(matrix)
        state = [1/np.sqrt(2), 1/np.sqrt(2)]
        
        mean = observable.mean(state)
        self.assertAlmostEqual(mean, 0.0)
    
    def test_variance_calculation(self):
        matrix = [[1, 0], [0, -1]]
        observable = Observable(matrix)
        state = [1, 0]  # Estado propio
        
        variance = observable.variance(state)
        self.assertAlmostEqual(variance, 0.0)

if __name__ == '__main__':
    unittest.main()