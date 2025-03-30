import pytest
from http import HTTPStatus
from tests.schemas.poem_schema import POEMS_ARRAY_SCHEMA, TITLE_ONLY_ARRAY_SCHEMA
from utilities.validators import (
    validate_response_schema, 
    validate_poem_title, 
    validate_poem_author,
    validate_text_format
)

class TestCombinedSearchEndpoint:
    """Tests for the combined search functionality of the PoetryDB API."""
    
    def test_combined_search_title_author(self, api_client, expected_author):
        """
        Test Case ID: TC-003
        
        Test that combined search with multiple criteria works correctly.
        
        Steps:
        1. Send GET request to /title,author/Winter;Shakespeare
        2. Verify response status code
        3. Validate response structure
        4. Verify all poems have titles containing "Winter" or "winter"
        5. Verify all poems have author "Shakespeare"
        
        Expected Result:
        Response contains only poems matching both criteria
        """
        # Step 1: Send GET request
        input_fields = "title,author"
        search_terms = "Winter;Shakespeare"
        response = api_client.combined_search(input_fields, search_terms)
        
        # Step 2: Verify response status code
        assert response.status_code == HTTPStatus.OK
        
        # Step 3: Validate response structure
        response_json = response.json()
        validate_response_schema(response_json, POEMS_ARRAY_SCHEMA)
        
        # Step 4-5: Verify all poems match both criteria
        for poem in response_json:
            # Check for case-insensitive match for "winter"
            assert "Winter" in poem['title'] or "winter" in poem['title'].lower()
            assert validate_poem_author(poem, expected_author)
    
    def test_absolute_match_search(self, api_client):
        """
        Test Case ID: TC-004
        
        Test that absolute match search works as expected.
        
        Steps:
        1. Send GET request to /title/Winter:abs
        2. Verify response status code
        3. Validate response structure
        4. Verify all poems have exact title "Winter"
        
        Expected Result:
        Response contains only poems with exact title "Winter"
        """
        # Step the abs flag to the title
        title = "Winter:abs"
        response = api_client.get_by_title(title)
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        validate_response_schema(response_json, POEMS_ARRAY_SCHEMA)
        
        for poem in response_json:
            assert poem['title'] == "Winter"  # Exact match, not just containing
    
    def test_combined_search_with_output_format(self, api_client, expected_author):
        """Test that combined search with specified output fields works correctly."""
        input_fields = "title,author"
        search_terms = "Winter;Shakespeare"
        output_format = "title"
        
        response = api_client.combined_search(input_fields, search_terms, output_format)
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        validate_response_schema(response_json, TITLE_ONLY_ARRAY_SCHEMA)
        
        for poem in response_json:
            assert "title" in poem
            # Check for case-insensitive match for "winter"
            assert "Winter" in poem['title'] or "winter" in poem['title'].lower()
            assert "author" not in poem
            assert "lines" not in poem
    
    def test_combined_search_text_format(self, api_client, expected_author):
        """
        Test Case ID: TC-005
        
        Test that text format output works correctly.
        
        Steps:
        1. Send GET request to /author/Shakespeare/title.text
        2. Verify response status code
        3. Verify that response format is appropriate
        4. Verify response contains poem titles
        
        Expected Result:
        Response contains listing of poem titles by Shakespeare
        """
        input_field = "author"
        search_term = expected_author
        output_format = "title.text"
        
        response = api_client.get_by_author(search_term, output_format)
        
        assert response.status_code == HTTPStatus.OK
        # The API actually returns JSON content type even for .text format
        assert "application/json" in response.headers.get("Content-Type", "")
        
        response_text = response.text
        
        # Should have multiple titles since Shakespeare wrote many poems
        assert len(response_text) > 0
        # Should contain the word "title" as part of the format
        assert "title" in response_text.lower() 