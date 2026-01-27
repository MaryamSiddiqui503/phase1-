# ADR-002: In-Memory Data Storage Approach

## Status
Accepted

## Date
2026-01-27

## Context
The project constitution mandates that the application operates entirely in memory with no persistence layer. Data will be stored using Python's built-in data structures and will be lost upon application termination. This constraint guides the entire storage architecture.

## Decision
We will implement pure in-memory storage using Python data structures (dictionaries and lists) to store task data. Specifically:
- Tasks will be stored in a Python dictionary with `id` as key and Task object as value
- An auto-increment counter will maintain unique IDs
- All data exists only in application memory and is lost upon program termination
- No external storage mechanisms (files, databases, caches) will be used

## Alternatives Considered
- File-based storage (rejected due to constitution constraint)
- Database storage (rejected due to constitution constraint)
- External caching solutions (rejected due to constitution constraint)
- JSON serialization to file (rejected due to no persistence constraint)

## Consequences
Positive:
- Complies with constitution requirement for no persistence layer
- Faster read/write operations compared to disk-based storage
- Simpler implementation without complex persistence logic
- Reduced security concerns around data storage

Negative:
- Data loss upon application termination
- Limited scalability for large amounts of data
- No ability to save/restore application state
- Session-based usage only

## References
- Plan.md: Technical Context and Storage sections
- Research.md: Data Storage Approach section
- spec.md: Constraints section regarding no persistence
- data-model.md: In-Memory Storage Structure section