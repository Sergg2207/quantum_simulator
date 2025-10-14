"""
Simulador de Sistemas Cuanticos
Simulador para sistemas cuanticos discretos
"""

from .core import QuantumSystem
from .observables import Observable
from .dynamics import QuantumDynamics

__version__ = "1.0.0"
__all__ = ['QuantumSystem', 'Observable', 'QuantumDynamics']