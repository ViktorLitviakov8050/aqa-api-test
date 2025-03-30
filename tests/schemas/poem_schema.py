# JSON Schemas for PoetryDB API Responses

# Schema for a single poem
POEM_SCHEMA = {
    "type": "object",
    "required": ["title", "author", "lines", "linecount"],
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "lines": {
            "type": "array",
            "items": {"type": "string"}
        },
        "linecount": {"type": ["string", "integer"]}
    },
    "additionalProperties": False
}

# Schema for array of poems
POEMS_ARRAY_SCHEMA = {
    "type": "array",
    "items": POEM_SCHEMA
}

# Schema for title-only response
TITLE_ONLY_SCHEMA = {
    "type": "object",
    "required": ["title"],
    "properties": {
        "title": {"type": "string"}
    },
    "additionalProperties": False
}

# Schema for author-only response
AUTHOR_ONLY_SCHEMA = {
    "type": "object",
    "required": ["author"],
    "properties": {
        "author": {"type": "string"}
    },
    "additionalProperties": False
}

# Schema for linecount-only response
LINECOUNT_ONLY_SCHEMA = {
    "type": "object",
    "required": ["linecount"],
    "properties": {
        "linecount": {"type": ["string", "integer"]}
    },
    "additionalProperties": False
}

# Schema for title and author response
TITLE_AUTHOR_SCHEMA = {
    "type": "object",
    "required": ["title", "author"],
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"}
    },
    "additionalProperties": False
}

# Schema for author, title, linecount response
AUTHOR_TITLE_LINECOUNT_SCHEMA = {
    "type": "object",
    "required": ["author", "title", "linecount"],
    "properties": {
        "author": {"type": "string"},
        "title": {"type": "string"},
        "linecount": {"type": ["string", "integer"]}
    },
    "additionalProperties": False
}

# Schema for an array of author, title, linecount objects
AUTHOR_TITLE_LINECOUNT_ARRAY_SCHEMA = {
    "type": "array",
    "items": AUTHOR_TITLE_LINECOUNT_SCHEMA
}

# Schema for an array of title-only objects
TITLE_ONLY_ARRAY_SCHEMA = {
    "type": "array",
    "items": TITLE_ONLY_SCHEMA
}

# Schema for an array of author-only objects
AUTHOR_ONLY_ARRAY_SCHEMA = {
    "type": "array",
    "items": AUTHOR_ONLY_SCHEMA
} 