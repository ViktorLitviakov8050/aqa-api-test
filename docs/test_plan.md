# PoetryDB API Testing Plan

## Introduction

This document outlines the test plan for automated testing of the PoetryDB API (https://poetrydb.org/). The plan includes test case design, validation strategies, tools selection, and implementation details.

## Test Scope

The scope includes testing the following endpoints and functionalities of the PoetryDB API:
- Author-based queries
- Title-based queries
- Random poem retrieval
- Combined search functionality
- Format specifications

## Test Environment

- **Programming Language**: Python 3.8+
- **Test Framework**: pytest
- **API Testing Library**: requests
- **Validation Library**: jsonschema for response validation

## Test Cases

### Test Case 1: Get Poem by Title

| Aspect | Description |
|--------|-------------|
| Test ID | TC-001 |
| Test Description | Verify that a poem can be retrieved by its exact title |
| Endpoint | `/title/{title}` |
| Method | GET |
| Test Steps | 1. Send GET request to `/title/Ozymandias` <br> 2. Verify response status code <br> 3. Validate response structure <br> 4. Verify poem title matches "Ozymandias" |
| Expected Result | Response contains the complete poem "Ozymandias" with correct structure |
| Validation Method | JSON schema validation + specific field check for title |

### Test Case 2: Get Random Poems

| Aspect | Description |
|--------|-------------|
| Test ID | TC-002 |
| Test Description | Verify that random poems can be retrieved with specified count and fields |
| Endpoint | `/random/{count}/{fields}` |
| Method | GET |
| Test Steps | 1. Send GET request to `/random/3/author,title,linecount` <br> 2. Verify response status code <br> 3. Validate response structure <br> 4. Verify response contains exactly 3 poems <br> 5. Verify each poem has the requested fields |
| Expected Result | Response contains 3 random poems with author, title, and linecount fields |
| Validation Method | JSON schema validation + array length check + field presence verification |

### Test Case 3: Combined Search with Multiple Parameters

| Aspect | Description |
|--------|-------------|
| Test ID | TC-003 |
| Test Description | Verify that combined search with multiple criteria works correctly |
| Endpoint | `/{input_fields}/{search_terms}` |
| Method | GET |
| Test Steps | 1. Send GET request to `/title,author/Winter;Shakespeare` <br> 2. Verify response status code <br> 3. Validate response structure <br> 4. Verify all poems have titles containing "Winter" <br> 5. Verify all poems have author "Shakespeare" |
| Expected Result | Response contains only poems matching both criteria |
| Validation Method | JSON schema validation + field value checks |

### Test Case 4: Absolute Match Search

| Aspect | Description |
|--------|-------------|
| Test ID | TC-004 |
| Test Description | Verify that absolute match search works as expected |
| Endpoint | `/{input_field}/{search_term}:abs` |
| Method | GET |
| Test Steps | 1. Send GET request to `/title/Winter:abs` <br> 2. Verify response status code <br> 3. Validate response structure <br> 4. Verify all poems have exact title "Winter" |
| Expected Result | Response contains only poems with exact title "Winter" |
| Validation Method | JSON schema validation + exact field match verification |

### Test Case 5: Text Format Output

| Aspect | Description |
|--------|-------------|
| Test ID | TC-005 |
| Test Description | Verify that text format output works correctly |
| Endpoint | `/{input_field}/{search_term}/{output_field}.text` |
| Method | GET |
| Test Steps | 1. Send GET request to `/author/Shakespeare/title.text` <br> 2. Verify response status code <br> 3. Verify that response is in plain text <br> 4. Verify format follows expected pattern |
| Expected Result | Response contains plain text listing of poem titles by Shakespeare |
| Validation Method | Content-Type header check + text pattern verification |

## Validation Strategy

### JSON Schema Validation
- Define schema for different response types
- Validate structure of each API response against expected schema
- Ensures all required fields are present with correct data types

### Field Value Validation
- Verify exact matches for specific fields
- Check numerical values (e.g., linecount)
- Validate that requested content is present

### Statistical Validation
- For random endpoints, validate statistical properties over multiple runs
- Ensure random distribution appears reasonably uniform

## Implementation Plan

1. **Project Setup**: Create directory structure and configure pytest
2. **Schema Definition**: Create JSON schemas for response validation
3. **Base Test Framework**: Create base test classes and utilities
4. **Test Implementation**: Implement specific test cases
5. **Execution and Reporting**: Configure test execution and reporting

## GitHub Repository Structure

```
aqa-api-test/
├── README.md                # Project description and test case table
├── requirements.txt         # Project dependencies
├── docs/
│   └── test_plan.md         # This test plan document
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # pytest configuration
│   ├── api_tests/           # API tests directory
│   │   ├── __init__.py
│   │   ├── test_author.py   # Author endpoint tests
│   │   ├── test_title.py    # Title endpoint tests
│   │   ├── test_random.py   # Random endpoint tests
│   │   └── test_combined.py # Combined search tests
│   └── schemas/             # JSON schemas for validation
│       ├── __init__.py
│       └── poem_schema.py   # Schema definitions
└── utilities/
    ├── __init__.py
    ├── api_client.py        # API client wrapper
    └── validators.py        # Custom validators
```

## Reporting

Test results will be captured and reported in the following formats:
- JUnit XML for CI/CD integration
- HTML report for human readability
- Console output for immediate feedback 