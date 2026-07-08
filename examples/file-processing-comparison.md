# File Processing: Traditional vs Agent Approach

This example demonstrates how traditional workflows and agent-based approaches handle the same task differently.

## Scenario: Processing User Uploaded Files

Both approaches must handle file uploads, but their methodologies differ significantly.

## Traditional Workflow Approach

```python
# Traditional file processor
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'jpg'}

def process_uploaded_file(file_path):
    """Process uploaded file using traditional workflow"""
    # Step 1: Extract file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Step 2: Check against allowed list
    if file_extension not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {file_extension}")

    # Step 3: Route to processor
    if file_extension == 'txt':
        return process_text_file(file_path)
    elif file_extension == 'pdf':
        return process_pdf_file(file_path)
    elif file_extension == 'doc':
        return process_doc_file(file_path)
    elif file_extension in ['jpg', 'jpeg']:
        return process_image_file(file_path)

    # Step 4: Handle errors (simplified)
    return f"File processed: {file_path}"
```

**Limitations of this approach:**
- Requires maintaining exhaustive file type lists
- Cannot adapt to new file types without code changes
- Difficult to add special processing logic
- No contextual understanding of user intent
- Error handling is rigid and predefined

## Agent-Based Workflow Approach

```python
# Intelligent file processor agent
import os
from typing import Optional

class FileProcessorAgent:
    def __init__(self):
        self.processing_history = []  # Remember past decisions

    def process_uploaded_file(self, file_path: str, user_context: dict = None) -> str:
        """Process uploaded file using agent-based workflow"""
        # Step 1: Examine file with context
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # Build understanding of the file
        understanding = {
            'name': file_name,
            'size': file_size,
            'extension': os.path.splitext(file_path)[1].lower(),
            'modification_time': os.path.getmtime(file_path),
            'user_intent': self._infer_user_intent(user_context),
            'content_preview': self._generate_content_preview(file_path)
        }

        # Step 2: Determine processing strategy
        strategy = self._select_processing_strategy(understanding, user_context)

        # Step 3: Execute strategy
        if strategy == 'text_processing':
            return self._execute_text_processing(file_path, understanding)
        elif strategy == 'pdf_processing':
            return self._execute_pdf_processing(file_path, understanding)
        elif strategy == 'document_processing':
            return self._execute_document_processing(file_path, understanding)
        elif strategy == 'image_processing':
            return self._execute_image_processing(file_path, understanding)
        elif strategy == 'archive_processing':
            return self._execute_archive_processing(file_path, understanding)
        elif strategy == 'unknown':
            return self._handle_unknown_file(file_path, understanding, user_context)

        # Step 4: Learn from results
        self.processing_history.append({
            'file_path': file_path,
            'strategy_used': strategy,
            'result': "processed",
            'user_context': user_context or {},
            'timestamp': self._get_current_timestamp()
        })

        return f"File processed intelligently: {file_name}"

    def _infer_user_intent(self, user_context: dict = None) -> str:
        """Infer user intent from context"""
        if not user_context:
            return "general_file_handling"

        # Check for explicit user goals
        if user_context.get('action') == 'summarize':
            return "create_summary"
        elif user_context.get('action') == 'translate':
            return "perform_translation"
        elif user_context.get('action') == 'question_answer':
            return "provide_information"
        elif user_context.get('action') == 'create':
            return "creative_content"
        else:
            return "unknown_intent"

    def _generate_content_preview(self, file_path: str) -> str:
        """Generate preview based on file content"""
        # This would use actual file analysis techniques
        return f"[Content preview of {file_path}]"

    def _select_processing_strategy(self, understanding: dict, user_context: dict = None) -> str:
        """Select appropriate processing strategy"""
        # Simple heuristic based on file properties
        if understanding['size'] > 10 * 1024 * 1024:  # > 10MB
            return 'archive_processing'  # Large files go to archive
        elif understanding['extension'] in ['txt', 'text']:
            return 'text_processing'  # Text files
        elif understanding['extension'] == 'pdf':
            return 'pdf_processing'  # PDF documents
        elif understanding['extension'] in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
            return 'image_processing'  # Image files
        elif 'document' in understanding.get('name', ''):  # Special handling
            return 'document_processing'  # Document files
        else:
            return 'unknown_processing'  # Try multiple approaches
```

**Advantages of agent approach:**
- Handles new file types without modification
- Understands user intent beyond file extension
- Learns from experience to improve over time
- Adapts processing based on actual content
- Provides contextual error handling

## Key Differences Summary

| Aspect | Traditional Workflow | Agent-Based Approach |
|--------|---------------------|---------------------|
| File Type Support | Fixed whitelist | Dynamic, content-based |
| Decision Making | Hardcoded rules | Contextual reasoning |
| Adaptability | Requires code changes | Self-improving from experience |
| Error Handling | Predefined codes | Learned from results |
| Scalability | Vertical (more processors) | Horizontal (better strategies) |

The agent approach transforms file processing from a rigid, extensibility-limited process to an intelligent, adaptive system.