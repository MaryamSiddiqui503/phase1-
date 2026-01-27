"""
Pytest configuration file.

This module sets up configuration for the pytest test runner.
"""

import sys
import os

# Add the src directory to the Python path so tests can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def pytest_configure(config):
    """
    Configure pytest settings.

    Args:
        config: The pytest configuration object
    """
    # Configuration can be added here if needed
    pass


def pytest_collection_modifyitems(config, items):
    """
    Modify test items during collection.

    Args:
        config: The pytest configuration object
        items: The collected test items
    """
    # Modify test items if needed
    pass