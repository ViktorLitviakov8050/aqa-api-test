import pytest
from http import HTTPStatus
from tests.schemas.poem_schema import POEMS_ARRAY_SCHEMA, TITLE_ONLY_ARRAY_SCHEMA
from utilities.validators import (
    validate_response_schema, 
    validate_poem_title, 
    validate_text_format,
    validate_poem_linecount
)

class TestTitleEndpoint:
    """Tests for the /title endpoint of the PoetryDB API."""
    
    def test_get_poem_by_title(self, api_client, expected_title):
        """
        Test Case ID: TC-001
        
        Test that a poem can be retrieved by its exact title.
        
        Steps:
        1. Send GET request to /title/Ozymandias
        2. Verify response status code
        3. Validate response structure
        4. Verify poem title matches "Ozymandias"
        
        Expected Result:
        Response contains the poem "Ozymandias" with correct structure
        """
        # Step 1: Send GET request
        response = api_client.get_by_title(expected_title)
        
        # Step 2: Verify response status code
        assert response.status_code == HTTPStatus.OK
        
        # Step 3: Validate response structure
        response_json = response.json()
        validate_response_schema(response_json, POEMS_ARRAY_SCHEMA)
        
        # Step 4: Verify poem title matches expected
        for poem in response_json:
            assert validate_poem_title(poem, expected_title)
    
    def test_get_title_specific_output(self, api_client, expected_title):
        """Test that a poem can be retrieved with a specific output field."""
        response = api_client.get_by_title(expected_title, "title")
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        validate_response_schema(response_json, TITLE_ONLY_ARRAY_SCHEMA)
        
        for poem in response_json:
            assert "title" in poem
            assert poem["title"] == expected_title
            assert "author" not in poem
            assert "lines" not in poem
    
    def test_get_title_text_format(self, api_client, expected_title):
        """Test that a poem can be retrieved in text format."""
        response = api_client.get_by_title(expected_title, "title.text")
        
        assert response.status_code == HTTPStatus.OK
        # The API actually returns JSON content type even for .text format
        assert "application/json" in response.headers.get("Content-Type", "")
        
        # Even though Content-Type is JSON, the response body is actually plain text
        response_text = response.text
        
        # Verify the title appears in the response text
        assert expected_title in response_text
    
    def test_get_poem_by_title_linecount_validation(self, api_client, expected_title):
        """Test that a poem's linecount matches the actual number of lines."""
        response = api_client.get_by_title(expected_title)
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        assert response_json
        
        for poem in response_json:
            assert validate_poem_linecount(poem) 