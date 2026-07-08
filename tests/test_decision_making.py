"""Test decision making: Traditional vs Agent Approach"""

import os
import tempfile
import pytest
from pathlib import Path

# Import the modules to test
import sys
sys.path.append(str(Path(__file__).parent.parent / "examples"))

from examples.decision_making_comparison import (
    select_database_traditional,
    select_database_intelligent
)

def test_traditional_decision_making_limitations():
    """Test limitations of traditional decision making approach"""
    # Test that traditional approach gives rigid decisions
    requirements = {
        'data_volume': 'large',
        'read_write_ratio': 'balanced',
        'consistency': 'strong',
        'query_complexity': 'simple',
        'team_experience': 'none',
        'budget': 'flexible',
        'deployment': 'cloud'
    }
    result = select_database_traditional(requirements)
    # Traditional approach gives hardcoded decision
    assert result in ['postgresql', 'oracle', 'mongodb', 'mysql']

    # Test that it doesn't consider context
    # In a real test, we would verify:
    # - Decision doesn't include organizational factors
    # - No learning from past decisions
    # - Static decision rules
    pass

def test_agent_decision_making_advantages():
    """Test advantages of agent-based decision making approach"""
    # Test that agent approach gives contextual decisions
    requirements = {
        'data_volume': 'large',
        'read_write_ratio': 'balanced',
        'consistency': 'strong',
        'query_complexity': 'simple',
        'team_experience': 'none',
        'budget': 'flexible',
        'deployment': 'cloud'
    }
    organizational_context = {
        'company_size': 'enterprise',
        'industry': 'finance',
        'regulatory_env': 'strict',
        'tech_stack_maturity': 'modern'
    }
    historical_data = {
        'past_decisions': [
            {'requirements': {
                'data_volume': 'large',
                'read_write_ratio': 'balanced',
                'consistency': 'strong',
                'query_complexity': 'simple',
                'team_experience': 'expert',
                'budget': 'tight',
                'deployment': 'on_prem'
            },
            'decision': 'postgresql',
            'outcome': 'successful'
        }
    ]
    }

    # Test that agent approach considers context
    result = select_database_intelligent(requirements, organizational_context, historical_data)
    # In a real test, we would verify:
    # - Result includes detailed reasoning
    # - Decision factors are explained
    # - Alternatives are considered
    # - Risks are identified and mitigated
    pass

if __name__ == "__main__":
    pytest.main([__file__])