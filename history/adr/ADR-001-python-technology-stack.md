# ADR-001: Python Technology Stack for Console Application

## Status
Accepted

## Date
2026-01-27

## Context
The project requires implementing a console-based todo application that operates entirely in memory. The constitution mandates the use of Python 3.8+ with type hints and restricts the use to built-in libraries only to comply with the in-memory storage constraint and avoid external dependencies.

## Decision
We will use Python 3.8+ as the primary language with built-in libraries only for the implementation of the console-based todo application. This includes using standard input/output for the CLI interface and built-in data structures for in-memory storage.

Components of the decision:
- Language: Python 3.8+
- Dependencies: Built-in Python libraries only (no external packages)
- Target: Cross-platform console application (Windows, macOS, Linux)
- Type hints: Required for all functions and classes

## Alternatives Considered
- Python with external frameworks (rejected due to external dependency constraint)
- Other languages like JavaScript or Java (rejected to maintain consistency with constitution)
- Rich library for enhanced console UI (rejected to avoid external dependencies)
- Click or argparse for command-line parsing (rejected as unnecessary complexity for menu-driven interface)

## Consequences
Positive:
- Complies with constitution requirements for Python usage and no external dependencies
- Cross-platform compatibility maintained
- Simplified deployment with no dependency management needed
- Leverages built-in Python features for rapid development

Negative:
- Limited UI capabilities compared to rich console libraries
- Potentially more verbose code for input validation and formatting
- May lack advanced CLI features available in external libraries

## References
- Plan.md: Technical Context section
- Research.md: Language and Framework Choice section
- spec.md: Constraints section