# Code Review: Traditional vs Agent Approach

This example shows how code review processes differ between traditional workflows and agent-based approaches.

## Scenario: Reviewing Pull Request Code

Both approaches aim to ensure code quality, but their methodologies reveal fundamental differences in how work gets done.

## Traditional Workflow Approach

```python
# Traditional code reviewer
def review_pull_request(pr_diff: str, repo_context: dict = None) -> dict:
    """Review pull request using traditional workflow"""
    review_result = {
        'approved': False,
        'comments': [],
        'suggestions': [],
        'risk_level': 'high'
    }

    # Step 1: Check coding standards (hardcoded)
    if not self._check_naming_conventions(pr_diff):
        review_result['comments'].append("Variable naming doesn't follow project standards")
        review_result['suggestions'].append("Use descriptive variable names")

    if not self._check_line_length(pr_diff):
        review_result['comments'].append("Lines exceed maximum length of 80 characters")
        review_result['suggestions'].append("Break long lines into multiple lines")

    if not self._check_indentation(pr_diff):
        review_result['comments'].append("Inconsistent indentation detected")
        review_result['suggestions'].append("Use 4-space indentation consistently")

    # Step 2: Check for common bugs (predefined patterns)
    bug_patterns = [
        r'==\s*None',  # Comparison with None
        r'!=\s*None',  # Not equal to None
        r'\[\s*\]',     # Empty list access
        r'{\s*}',       # Empty dict access
        r'\(\s*\)',     # Empty tuple access
    ]

    for pattern in bug_patterns:
        if re.search(pattern, pr_diff, re.IGNORECASE):
            review_result['comments'].append(f"Potential bug: {pattern}")
            review_result['suggestions'].append(f"Replace with explicit check")

    # Step 3: Check complexity (static thresholds)
    complexity_score = self._calculate_cyclomatic_complexity(pr_diff)
    if complexity_score > 15:
        review_result['comments'].append("Code complexity too high")
        review_result['suggestions'].append("Refactor to reduce complexity")
        review_result['risk_level'] = 'medium'

    # Step 4: Security check (known vulnerabilities)
    vuln_patterns = [
        r'pass\s*=',      # Potential password exposure
        r'api_key\s*=',   # API key in code
        r'secret\s*=',    # Secret value in code
        r'eval\s*\=',     # Use of eval function
        r'exec\s*\=',     # Use of exec function
    ]

    for pattern in vuln_patterns:
        if re.search(pattern, pr_diff, re.IGNORECASE):
            review_result['comments'].append(f"Security concern: {pattern}")
            review_result['suggestions'].append("Remove hardcoded secrets")
            review_result['risk_level'] = 'high'

    # Step 5: Documentation check (required elements)
    required_docs = ['function purpose', 'parameters', 'return value', 'examples']
    missing_docs = []
    for doc in required_docs:
        if not self._has_documentation(pr_diff, doc):
            missing_docs.append(doc)

    if missing_docs:
        review_result['comments'].append(f"Missing documentation: {', '.join(missing_docs)}")
        review_result['suggestions'].append("Add missing documentation")

    # Final decision (based on all checks)
    if not review_result['comments']:
        review_result['approved'] = True
        review_result['risk_level'] = 'low'
    elif len(review_result['comments']) <= 2:
        review_result['approved'] = True  # Minor issues
        review_result['risk_level'] = 'low'
    else:
        review_result['approved'] = False
        # Risk level stays as set by most severe issue found

    return review_result

def _check_naming_conventions(self, diff: str) -> bool:
    """Check if naming follows conventions"""
    # Hardcoded check for camelCase or snake_case
    variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*='
    variables = re.findall(variable_pattern, diff)
    # Simplified: assume all follow convention for demo
    return True

def _check_line_length(self, diff: str) -> bool:
    """Check if lines are within length limit"""
    lines = diff.split('\n')
    return all(len(line) <= 80 for line in lines)

def _check_indentation(self, diff: str) -> bool:
    """Check if indentation is consistent"""
    lines = diff.split('\n')
    # Simplified check
    return True

def _calculate_cyclomatic_complexity(self, diff: str) -> int:
    """Calculate cyclomatic complexity"""
    # Simplified calculation
    return 5  # Always return medium complexity for demo

def _has_documentation(self, diff: str, doc_type: str) -> bool:
    """Check if documentation exists for type"""
    # Simplified check
    return True
```

**Limitations of traditional approach:**
- Cannot adapt to new coding standards without updates
- Misses context-specific issues
- Static thresholds don't account for team experience
- Security checks limited to known patterns
- Documentation checks are binary (present/absent)

## Agent-Based Workflow Approach

```python
# Intelligent code reviewer agent
from typing import List, Optional
import re
from datetime import datetime

class CodeReviewerAgent:
    def __init__(self):
        self.review_history = []  # Learn from past reviews
        self.team_standards = {   # Evolving team standards
            'naming': 'snake_case',  # Can change over time
            'max_line_length': 100,   # Can adapt to team preference
            'indentation_size': 4,    # Can be configured
            'complexity_threshold': 20, # Based on team skill level
        }

    def review_pull_request(self, pr_diff: str, repo_context: dict = None,
                          submitter_info: dict = None) -> dict:
        """Review pull request using agent-based workflow"""
        # Step 1: Build comprehensive understanding
        context = self._build_review_context(
            pr_diff, repo_context, submitter_info
        )

        # Step 2: Generate review through reasoning
        review_result = self._generate_review_reasoning(context)

        # Step 3: Learn from this review
        self.review_history.append({
            'pr_diff': pr_diff,
            'context': context,
            'result': review_result,
            'timestamp': self._get_current_timestamp(),
            'submitter_info': submitter_info or {}
        })

        # Update team standards based on experience
        self._update_team_standards(review_result, submitter_info)

        return review_result

    def _build_review_context(self, pr_diff: str, repo_context: dict = None,
                            submitter_info: dict = None) -> dict:
        """Build rich context for code review"""
        # Analyze the code changes
        code_analysis = self._analyze_code_changes(pr_diff)

        # Understand repository context
        repo_understanding = self._understand_repository(repo_context)

        # Know the submitter
        submitter_profile = self._understand_submitter(submitter_info)

        # Consider current conditions
        current_conditions = self._assess_current_conditions()

        return {
            'pr_diff': pr_diff,
            'timestamp': self._get_current_timestamp(),
            'code_analysis': code_analysis,
            'repo_understanding': repo_understanding,
            'submitter_profile': submitter_profile,
            'current_conditions': current_conditions,
            'review_purpose': self._determine_review_purpose(context)
        }

    def _analyze_code_changes(self, pr_diff: str) -> dict:
        """Analyze what the code changes actually do"""
        # Parse the diff to understand changes
        added_lines = []
        removed_lines = []
        modified_lines = []

        for line in pr_diff.split('\n'):
            if line.startswith('+') and not line.startswith('+++'):
                added_lines.append(line[1:])  # Remove + prefix
            elif line.startswith('-') and not line.startswith('---'):
                removed_lines.append(line[1:])  # Remove - prefix
            elif line.startswith('@@'):
                continue  # Skip hunk headers

        return {
            'added_lines': added_lines,
            'removed_lines': removed_lines,
            'modified_lines': modified_lines,  # Simplified for demo
            'files_changed': len(set([
                self._extract_file_from_line(line)
                for line in pr_diff.split('\n')
                if line.startswith(('+++', '---', '+', '-'))
                and not line.startswith('@@')
            ])),
            'total_changes': len(added_lines) + len(removed_lines),
            'net_additions': len(added_lines) - len(removed_lines),
            'language_distribution': self._analyze_language_use(pr_diff),
            'complexity_metrics': self._calculate_code_complexity(pr_diff),
            'security_scan': self._perform_security_scan(pr_diff),
            'style_analysis': self._analyze_code_style(pr_diff)
        }

    def _extract_file_from_line(self, line: str) -> Optional[str]:
        """Extract filename from diff line"""
        # Simplified extraction
        if line.startswith(('+++', '---', '+', '-')):
            parts = line[1:].split()
            if len(parts) >= 2:
                return parts[1]  # Return filename
        return None

    def _analyze_language_use(self, pr_diff: str) -> dict:
        """Analyze programming language usage"""
        # Count language indicators
        indicators = {
            'python': ['def ', 'import ', 'from ', 'class ', 'self.', 'None', 'True', 'False'],
            'javascript': ['function ', 'var ', 'let ', 'const ', '=>', 'null', 'true', 'false'],
            'java': ['public ', 'private ', 'protected ', 'class ', 'interface ', 'extends ', 'implements '],
            'cpp': ['#include ', 'using namespace ', 'std::', 'class ', 'template ', 'virtual '],
        }

        counts = {}
        for lang, lang_indicators in indicators.items():
            count = 0
            for indicator in lang_indicators:
                count += pr_diff.lower().count(indicator.lower())
            counts[lang] = count

        return counts

    def _calculate_code_complexity(self, pr_diff: str) -> dict:
        """Calculate various complexity metrics"""
        lines = [line for line in pr_diff.split('\n') if line.strip()]
        if not lines:
            return {
                'cyclomatic': 0,
                'cognitive': 0,
                'maintainability': 0
            }

        # Simplified metrics
        return {
            'cyclomatic': len(lines) // 10 + 5,  # Rough estimate
            'cognitive': len(''.join(lines)) // 100,  # Based on length
            'maintainability': 10 - (len(lines) // 20),  # Inverse of size
        }

    def _perform_security_scan(self, pr_diff: str) -> List[str]:
        """Perform contextual security analysis"""
        concerns = []

        # Context-aware password check
        if 'password' in pr_diff.lower() and '=' in pr_diff:
            # Check if it's actually a security issue
            lines = pr_diff.split('\n')
            for line in lines:
                if 'password' in line.lower() and '=' in line:
                    # Look at surrounding context
                    surrounding = ' '.join(lines[max(0, lines.index(line)-2):lines.index(line)+3])
                    if 'hash' not in surrounding.lower() and 'encrypt' not in surrounding.lower():
                        concerns.append("Potential password exposure without hashing")

        # Dynamic secret detection
        secret_indicators = ['key', 'token', 'secret', 'private', 'confidential']
        for indicator in secret_indicators:
            if indicator in pr_diff.lower() and '=' in pr_diff:
                concerns.append(f"Potential {indicator} exposure")

        # Import-based vulnerability check
        import_lines = [line for line in pr_diff.split('\n')
                       if line.strip().startswith(('import ', 'from '))]
        for imp_line in import_lines:
            imp_line_clean = imp_line.strip()
            # Check for known vulnerable imports
            vuln_imports = {
                'pickle': ['pickle'],  # Can be dangerous
                'yaml': ['yaml', 'yml'],  # Unsafe loading
                'marshal': ['marshal'],  # Risks with untrusted data
            }
            for vuln, vuln_indicators in vuln_imports.items():
                if any(ind in imp_line_clean.lower() for ind in vuln_indicators):
                    concerns.append(f"Import of potentially vulnerable {vuln}")

        # Context-aware eval/exec check
        eval_patterns = ['eval(', 'exec(', 'compile(', 'eval_'
        for pattern in eval_patterns:
            if pattern in pr_diff:
                # Check if it's in a safe context
                lines = pr_diff.split('\n')
                for line_idx, line in enumerate(lines):
                    if pattern in line:
                        # Look at broader context
                        context_lines = lines[max(0, line_idx-5):min(len(lines), line_idx+6)]
                        context = ' '.join(context_lines)
                        if ('test' not in context.lower() and
                            'demo' not in context.lower() and
                            'example' not in context.lower()):
                            concerns.append(f"Potentially unsafe {pattern.strip()('(')}")

        return concerns

    def _analyze_code_style(self, pr_diff: str) -> dict:
        """Analyze code style and formatting"""
        lines = [line for line in pr_diff.split('\n') if line.strip()]
        if not lines:
            return {
                'indentation': {'consistent': True, 'size': 0},
                'line_length': {'max': 0, 'over_limit': []},
                'whitespace': {'leading': 0, 'trailing': 0, 'internal': 0},
                'braces': {'balanced': True, 'pairs': 0},
                'naming': {'style': 'unknown', 'violations': []}
            }

        # Simplified style analysis
        return {
            'indentation': {
                'consistent': True,  # Assume consistent for demo
                'size': 4,  # Standard size
            },
            'line_length': {
                'max': max(len(line) for line in lines) if lines else 0,
                'over_limit': [line for line in lines if len(line) > 100]
            },
            'whitespace': {
                'leading': 0,  # Assume no issues for demo
                'trailing': 0,
                'internal': 0,
            },
            'braces': {
                'balanced': True,  # Assume balanced for demo
                'pairs': 0,
            },
            'naming': {
                'style': 'snake_case',  # Team standard
                'violations': [],  # Assume no violations for demo
            }
        }

    def _understand_repository(self, repo_context: dict = None) -> dict:
        """Understand repository context and standards"""
        if not repo_context:
            return {
                'name': 'unknown_repository',
                'description': 'No repository context provided',
                'language': 'unknown',
                'size': {
                    'commits': 0,
                    'contributors': 0,
                    'files': 0
                },
                'maturity': 'unknown',
                'standards': {},
                'recent_activity': 'none'
            }

        # Simplified repository understanding
        return {
            'name': repo_context.get('name', 'unknown_repository'),
            'description': repo_context.get('description', 'Standard repository'),
            'language': repo_context.get('language', 'Polyglot'),
            'size': {
                'commits': repo_context.get('commits', 0),
                'contributors': repo_context.get('contributors', 0),
                'files': 0
            },
            'maturity': repo_context.get('maturity', 'Established'),
            'standards': repo_context.get('standards', {
                'naming': 'snake_case',
                'line_length': 100,
                'indentation': 4
            }),
            'recent_activity': repo_context.get('recent_activity', 'Active')
        }

    def _understand_submitter(self, submitter_info: dict = None) -> dict:
        """Understand who submitted the code"""
        if not submitter_info:
            return {
                'username': 'unknown_submitter',
                'experience_level': 'unknown',
                'trust_level': 'medium',  # Default trust
                'historical_accuracy': 'unknown',
                'specialties': [],
                'recent_activity': 'unknown'
            }

        # Simplified submitter understanding
        return {
            'username': submitter_info.get('username', 'unknown_contributor'),
            'experience_level': submitter_info.get('experience_level', 'intermediate'),
            'trust_level': submitter_info.get('trust_level', 'high'),
            'historical_accuracy': submitter_info.get('historical_accuracy', 'reliable'),
            'specialties': submitter_info.get('specialties', []),
            'recent_activity': submitter_info.get('recent_activity', 'active')
        }

    def _assess_current_conditions(self) -> dict:
        """Assess current system and project conditions"""
        # Simplified condition assessment
        return {
            'system_load': 'low',  # Normal operating conditions
            'time_of_day': 'afternoon',  # Based on current time
            'day_of_week': 'wednesday',   # Based on current date
            'recent_incidents': 'none',   # No recent production issues
            'upcoming_deadlines': 'none',   # No immediate deadlines
            'team_availability': 'high',   # Team is available for collaboration
            'security_level': 'standard',   # No elevated security concerns
        }

    def _determine_review_purpose(self, context: dict) -> str:
        """Determine the purpose of this review"""
        context = context or {}
        submitter = context.get('submitter_profile', {})
        repo = context.get('repo_understanding', {})
        code = context.get('code_analysis', {})

        # Check for explicit purpose indicators
        if submitter.get('username') == 'maintainer':
            return 'maintenance_review'
        elif repo.get('maturity') == 'legacy':
            return 'legacy_system_care'
        elif code.get('language_distribution', {}).get('python', 0) > 50:
            return 'python_focus'
        elif len(code.get('security_scan', [])) > 0:
            return 'security_focus'
        elif code.get('complexity_metrics', {}).get('cyclomatic', 0) > 10:
            return 'complexity_reduction'
        elif repo.get('recent_activity') == 'very_active':
            return 'rapid_development'
        else:
            return 'quality_improvement'

    def _generate_review_reasoning(self, context: dict) -> dict:
        """Generate review through contextual reasoning"""
        context = context or {}
        review_result = {
            'approved': False,
            'comments': [],
            'suggestions': [],
            'risk_level': 'high',
            'confidence': 0.5
        }

        # Reason about code changes
        code_analysis = context.get('code_analysis', {})
        repo_understanding = context.get('repo_understanding', {})
        submitter_profile = context.get('submitter_profile', {})
        current_conditions = context.get('current_conditions', {})

        # Dynamic naming convention check
        naming_style = repo_understanding.get('standards', {}).get('naming', 'snake_case')
        naming_violations = code_analysis.get('style_analysis', {}).get('naming', {}).get('violations', [])

        if naming_violations:
            review_result['comments'].append(
                f"Naming violations: {len(naming_violations)} issues found"
            )
            if len(naming_violations) <= 3:
                review_result['suggestions'].append(
                    "Fix naming inconsistencies to match team standard"
                )
            else:
                review_result['suggestions'].append(
                    "Consider automated refactoring for naming"
                )
            review_result['risk_level'] = min(review_result['risk_level'], 'medium')

        # Context-aware line length check
        max_line_length = repo_understanding.get('standards', {}).get('line_length', 100)
        long_lines = code_analysis.get('style_analysis', {}).get('line_length', {}).get('over_limit', [])

        if long_lines:
            review_result['comments'].append(
                f"{len(long_lines)} lines exceed {max_line_length} characters"
            )
            if len(long_lines) <= 2:
                review_result['suggestions'].append(
                    "Break long lines at logical points"
                )
            else:
                review_result['suggestions'].append(
                    "Consider line wrapping configuration"
                )
            else:
                review_result['suggestions'].append(
                    "Consider line wrapping configuration"
                )
            review_result['risk_level'] = min(review_result['risk_level'], 'medium')

        # Adaptive indentation check
        indentation_size = repo_understanding.get('standards', {}).get('indentation', 4)
        indent_consistent = code_analysis.get('style_analysis', {}).get('indentation', {}).get('consistent', True)

        if not indent_consistent:
            review_result['comments'].append("Inconsistent indentation detected")
            review_result['suggestions'].append(
                f"Use {indentation_size}-space indentation consistently"
            )
            review_result['risk_level'] = min(review_result['risk_level'], 'medium')

        # Experience-based complexity assessment
        complexity_threshold = repo_understanding.get('standards', {}).get('complexity_threshold', 20)
        cyclomatic = code_analysis.get('complexity_metrics', {}).get('cyclomatic', 0)

        if cyclomatic > complexity_threshold:
            review_result['comments'].append(
                f"Code complexity ({cyclomatic}) exceeds team threshold ({complexity_threshold})"
            )
            # Consider submitter experience
            submitter_exp = submitter_profile.get('experience_level', 'intermediate')
            if submitter_exp in ['junior', 'entry_level']:
                review_result['suggestions'].append(
                    "Consider breaking down complex functions"
                )
            elif submitter_exp in ['senior', 'expert']:
                review_result['suggestions'].append(
                    "Team can handle this complexity level"
                )
            else:
                review_result['suggestions'].append(
                    "Provide mentoring for complexity management"
                )
            review_result['risk_level'] = min(review_result['risk_level'], 'medium')

        # Context-aware security evaluation
        security_concerns = code_analysis.get('security_scan', [])
        if security_concerns:
            # Weight concerns by context
            for concern in security_concerns:
                if ('test' in concern.lower() or
                    'demo' in concern.lower() or
                    'example' in concern.lower()):
                    # Lower risk in testing contexts
                    review_result['suggestions'].append(
                        f"Safe to ignore in testing: {concern}"
                    )
                elif ('production' in current_conditions.get('system_load', '') or
                      'high' in current_conditions.get('system_load', '')):
                    # Higher risk in production
                    review_result['comments'].append(
                        f"Needs fixing in production: {concern}"
                    )
                else:
                    review_result['comments'].append(concern)
                    review_result['suggestions'].append(
                        "Investigate and fix: {concern}"
                    )
            # Adjust risk level based on context
            production_load = current_conditions.get('system_load', '')
            if production_load in ['high', 'critical']:
                review_result['risk_level'] = 'high'
            elif production_load in ['medium']:
                review_result['risk_level'] = 'medium'
            else:
                review_result['risk_level'] = min(review_result['risk_level'], 'low')

        # Dynamic documentation check
        required_docs = ['function purpose', 'parameters', 'return value', 'examples']
        missing_docs = []
        context_docs = current_conditions.get('team_availability', '')
        for doc in required_docs:
            # Context-sensitive documentation requirements
            if doc == 'function purpose' and context_docs == 'low':
                # Less critical for internal tools
                continue
            elif doc == 'examples' and repo_understanding.get('maturity', '') == 'legacy':
                # Less important for mature code
                continue
            elif not self._has_documentation_contextual(
                    code_analysis, doc, repo_understanding, submitter_profile
                ):
                missing_docs.append(doc)

        if missing_docs:
            review_result['comments'].append(
                f"Missing documentation: {', '.join(missing_docs)}"
            )
            # Context-aware suggestions
            for doc in missing_docs:
                if doc == 'examples' and repo_understanding.get('maturity', '') == 'active':
                review_result['suggestions'].append(
                    "Add usage examples for active codebase"
                )
                elif doc == 'return value' and submitter_profile.get('experience_level', '') == 'junior':
                review_result['suggestions'].append(
                    "Clarify return types for junior developers"
                )
                else:
                    review_result['suggestions'].append(
                        f"Add missing {doc} documentation"
                    )

        # Final decision with learning
        if not review_result['comments']:
            review_result['approved'] = True
            review_result['risk_level'] = 'low'
            review_result['confidence'] = 0.9  # High confidence in approval
        elif len(review_result['comments']) <= 2:
            review_result['approved'] = True  # Minor issues
            review_result['risk_level'] = 'low'
            review_result['confidence'] = 0.7  # Good confidence
        else:
            review_result['approved'] = False
            # Risk level informed by reasoning, not just counting
            review_result['confidence'] = 0.6  # Reasoned disagreement

        return review_result

    def _has_documentation_contextual(self, code_analysis: dict, doc_type: str,
                                repo_understanding: dict = None,
                                submitter_profile: dict = None) -> bool:
        """Check documentation with context awareness"""
        # Simplified contextual check
        return True

    def _update_team_standards(self, review_result: dict,
                            submitter_info: dict = None) -> None:
        """Update team standards based on review experience"""
        # Learn from this review to improve future reviews
        submitter = submitter_info or {}
        context_conditions = {
            'system_load': 'low',
            'time_of_day': 'afternoon',
            'day_of_week': 'wednesday',
            'recent_incidents': 'none',
            'upcoming_deadlines': 'none',
            'team_availability': 'high',
            'security_level': 'standard'
        }

        # Simple learning mechanism
        if review_result.get('approved', False):
            # Successful review reinforces current standards
            pass
        else:
            # Failed review suggests standards might need adjustment
            # In a real implementation, this would update standards
            # based on what caused the review to fail
            pass

    def _get_current_timestamp(self) -> str:
        """Get current timestamp for learning"""
        # Simplified timestamp
        return "2026-03-29T10:30:00Z"
```

**Advantages of agent approach:**
- Adapts to team-specific standards and practices
- Considers submitter experience and expertise
- Weighs issues based on deployment context
- Learns from review history to improve over time
- Provides nuanced, reasoned feedback

## Key Differences Summary

| Aspect | Traditional Workflow | Agent-Based Approach |
|--------|---------------------|---------------------|
| Standards Checking | Hardcoded rules | Evolving team standards |
| Context Awareness | Limited to file content | Rich contextual understanding |
| Learning Capability | None | Improves from experience |
| Feedback Nuance | Binary (approved/rejected) | Reasoned, contextual feedback |
| Adaptability | Requires manual updates | Self-improving through use |

The agent approach transforms code review from a rigid, checklist-based process to an intelligent, adaptive system that grows wiser with experience.