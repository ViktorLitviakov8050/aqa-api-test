import jsonschema

def validate_response_schema(response_data, schema):
    """Validate API response against a JSON schema.
    
    Args:
        response_data (dict or list): Response data to validate
        schema (dict): JSON schema to validate against
        
    Raises:
        jsonschema.exceptions.ValidationError: If validation fails
    """
    jsonschema.validate(instance=response_data, schema=schema)

def validate_poem_title(poem, expected_title):
    """Validate that a poem has the expected title.
    
    Args:
        poem (dict): Poem data
        expected_title (str): Expected title
        
    Returns:
        bool: True if the title matches, False otherwise
    """
    return poem.get('title') == expected_title

def validate_poem_author(poem, expected_author):
    """Validate that a poem has the expected author.
    
    Args:
        poem (dict): Poem data
        expected_author (str): Expected author
        
    Returns:
        bool: True if the author matches, False otherwise
    """
    return poem.get('author') == expected_author

def validate_poem_linecount(poem):
    """Validate that a poem's linecount matches the actual number of lines.
    
    Args:
        poem (dict): Poem data containing 'lines' and 'linecount'
        
    Returns:
        bool: True if the linecount is accurate, False otherwise
    """
    if 'lines' not in poem or 'linecount' not in poem:
        return False
    
    actual_count = len(poem['lines'])
    reported_count = int(poem['linecount']) if isinstance(poem['linecount'], str) else poem['linecount']
    
    return actual_count == reported_count

def validate_text_format(response_text, field_name):
    """Validate that a text format response has the expected structure.
    
    Args:
        response_text (str): Response text to validate
        field_name (str): Field name that should be present in each section
        
    Returns:
        bool: True if the text format is valid, False otherwise
    """
    if not response_text:
        return False
    
    lines = response_text.strip().split('\n')
    
    # Text format should have at least one field entry
    if not lines:
        return False
    
    # Each section should start with the field name
    for i in range(0, len(lines), 2):
        if i < len(lines) and not lines[i].startswith(field_name):
            return False
    
    return True

def validate_response_count(response_data, expected_count):
    """Validate that a response contains the expected number of items.
    
    Args:
        response_data (list): Response data
        expected_count (int): Expected number of items
        
    Returns:
        bool: True if the count matches, False otherwise
    """
    return len(response_data) == expected_count 