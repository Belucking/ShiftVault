# test_shiftvault.py
"""
Tests for ShiftVault module.
"""

import unittest
from shiftvault import ShiftVault

class TestShiftVault(unittest.TestCase):
    """Test cases for ShiftVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShiftVault()
        self.assertIsInstance(instance, ShiftVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShiftVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
