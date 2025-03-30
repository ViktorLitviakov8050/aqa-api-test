# PoetryDB API Testing Project

This repository contains automated API tests for the [PoetryDB API](https://poetrydb.org/), which is described as "The Internet's first Poetry API." The tests are implemented using Python with pytest and requests libraries.

## Test Cases

Below are the key test cases implemented in this project:

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

## Validation Strategy

The validation approach in this project uses multiple techniques to ensure API functionality:

### 1. JSON Schema Validation

We use the `jsonschema` library to validate API responses against predefined schemas. This approach was chosen because:

- It provides comprehensive validation of the entire response structure
- It ensures all required fields are present with correct data types
- It's a standardized approach for API validation that scales well
- It allows us to catch structural changes in the API early

Example schema validation:
```python
def validate_poem_schema(poem_data):
    """Validate a poem response against the poem schema."""
    schema = POEM_SCHEMA
    jsonschema.validate(instance=poem_data, schema=schema)
```

### 2. Specific Field Validation

Beyond schema validation, we perform specific checks on field values to ensure the API returns exactly what we requested:

- For title-based searches, we verify the returned poem has the expected title
- For author-based searches, we check that each poem is attributed to the correct author
- For linecount parameters, we validate that the reported line count matches the actual number of lines

### 3. Statistical Validation for Random Endpoints

For endpoints that return random poems, we:
- Validate that the requested number of poems is returned
- Over multiple test runs, ensure a reasonable distribution of results
- Verify no duplicates within a single response

## Project Structure

```
aqa-api-test/
├── README.md                # This file
├── requirements.txt         # Project dependencies
├── docs/
│   └── test_plan.md         # Detailed test plan
├── tests/
│   ├── api_tests/           # API tests
│   └── schemas/             # JSON schemas for validation
└── utilities/               # Helper utilities
```

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## Dependencies

- Python 3.8+
- pytest
- requests
- jsonschema 