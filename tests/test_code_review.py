"""Test code review: Traditional vs Agent Approach"""

import os
import tempfile
import pytest
from pathlib import Path

# Import the modules to test
import sys
sys.path.append(str(Path(__file__).parent.parent / "examples"))

from examples.code_review_comparison import (
    review_pull_request_traditional,
    review_pull_request_intelligent
)

def test_traditional_code_review_limitations():
    """Test limitations of traditional code review approach"""
    # Create a temporary file with PR that has issues
    with tempfile.NamedTemporaryFile(suffix='.pr', delete=False) as tmp_file:
        tmp_path = tmp_file.name

        # Test that PR with issues fails validation
        with pytest.raises(ValueError) as exc_info:
            review_pull_request_traditional(tmp_path)

        # Verify error details
        assert "Variable naming doesn't follow project standards" in str(exc_info.value)
        assert exc_info.type == ValueError

def test_agent_code_review_advantages():
    """Test advantages of agent-based code review approach"""
    # Create a temporary file with PR that has no issues
    with tempfile.NamedTemporaryFile(suffix='.pr', delete=False) as tmp_file:
        tmp_path = tmp_file.name

        # Test that PR with no issues passes validation
        result = review_pull_request_intelligent(tmp_path)
        assert result == "Pull request approved: All checks passed"

        # Test that it handles code review intelligently
        # In a real test, we would verify:
        # - Review includes timestamp, PR diff, context
        # - Provides reasoned, contextual feedback
        # - Returns actionable recommendations
        pass

if __name__ == "__main__":
    pytest.main([__file__])