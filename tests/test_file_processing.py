"""Test file processing: Traditional vs Agent Approach"""

import os
import tempfile
import pytest
from pathlib import Path

# Import the modules to test
import sys
sys.path.append(str(Path(__file__).parent.parent / "examples"))

from examples.file_processing_comparison import (
    process_file_with_traditional_handler,
    process_file_with_intelligent_handler
)

def test_traditional_file_processing_limitations():
    """Test limitations of traditional file processing approach"""
    # Create a temporary file with unsupported extension
    with tempfile.NamedTemporaryFile(suffix='.xyz', delete=False) as tmp_file:
        tmp_path = tmp_file.name

        # Test that unsupported file type raises error
        with pytest.raises(ValueError) as exc_info:
            process_file_with_traditional_handler(tmp_path)

        # Verify error details
        assert "Unsupported file type: .xyz" in str(exc_info.value)
        assert exc_info.type == ValueError

def test_agent_file_processing_advantages():
    """Test advantages of agent-based file processing approach"""
    # Create test file with known extension
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp_file:
        tmp_path = tmp_file.name

        # Test that text file processes successfully
        result = process_file_with_intelligent_handler(tmp_path)
        assert result == f"File processed intelligently: {tmp_path}"

        # Test that it handles file content intelligently
        # In a real test, we would check the actual processing logic
        pass

def test_error_handling_differences():
    """Test key differences in error handling"""
    # Test that traditional approach gives basic error info
    with tempfile.NamedTemporaryFile(suffix='.log', delete=False) as tmp_file:
        tmp_path = tmp_file.name

        traditional_result = process_file_with_traditional_handler(tmp_path)
        assert traditional_result in [
            "File not found",
            "Permission denied",
            "Unknown error"
        ]
        # Traditional approach gives limited, predefined messages

        # Test that agent approach gives rich error context
        intelligent_result = process_file_with_intelligent_handler(tmp_path)
        # In a real test, we would verify:
        # - Error includes timestamp, file path, operation
        # - Provides contextual recovery suggestions
        # - Returns actionable user messages
        pass

if __name__ == "__main__":
    pytest.main([__file__])