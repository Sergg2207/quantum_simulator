import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from quantum_simulator.core import QuantumSystem
import numpy as np

class TestQuantumSystem(unittest.TestCase):
    
    def test_initialization(self):
        system = QuantumSystem(3)
        self.assertEqual(system.num_positions, 3)
        self.assertIsNone(system.state)
    
    def test_set_state(self):
        system = QuantumSystem(2)
        system.set_state([1, 1])
        
        # Verificar que el estado esta normalizado
        expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
        np.testing.assert_array_almost_equal(system.state, expected)
    
    def test_position_probability(self):
        system = QuantumSystem(2)
        system.set_state([1, 0])
        
        self.assertAlmostEqual(system.position_probability(0), 1.0)
        self.assertAlmostEqual(system.position_probability(1), 0.0)
    
    def test_transition_probability(self):
        system = QuantumSystem(2)
        system.set_state([1, 0])
        target = [0, 1]
        
        prob = system.transition_probability(target)
        self.assertAlmostEqual(prob, 0.0)
        
        # Transicion a si mismo deberia ser 1
        prob_self = system.transition_probability([1, 0])
        self.assertAlmostEqual(prob_self, 1.0)

if __name__ == '__main__':
    unittest.main()