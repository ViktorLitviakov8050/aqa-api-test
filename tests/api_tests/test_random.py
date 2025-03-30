import pytest
from http import HTTPStatus
from tests.schemas.poem_schema import AUTHOR_TITLE_LINECOUNT_ARRAY_SCHEMA, TITLE_ONLY_ARRAY_SCHEMA
from utilities.validators import validate_response_schema, validate_response_count

class TestRandomEndpoint:
    """Tests for the /random endpoint of the PoetryDB API."""
    
    def test_get_random_poems(self, api_client):
        """
        Test Case ID: TC-002
        
        Test that random poems can be retrieved with specified count and fields.
        
        Steps:
        1. Send GET request to /random/3/author,title,linecount
        2. Verify response status code
        3. Validate response structure
        4. Verify response contains exactly 3 poems
        5. Verify each poem has the requested fields
        
        Expected Result:
        Response contains 3 random poems with author, title, and linecount fields
        """
        # Step 1: Send GET request
        count = 3
        fields = "author,title,linecount"
        response = api_client.get_random(count, fields)
        
        # Step 2: Verify response status code
        assert response.status_code == HTTPStatus.OK
        
        # Step 3: Validate response structure
        response_json = response.json()
        validate_response_schema(response_json, AUTHOR_TITLE_LINECOUNT_ARRAY_SCHEMA)
        
        # Step 4: Verify response contains exactly 3 poems
        assert validate_response_count(response_json, count)
        
        # Step 5: Verify each poem has the requested fields
        for poem in response_json:
            assert "author" in poem
            assert "title" in poem
            assert "linecount" in poem
            assert "lines" not in poem
    
    def test_get_random_poems_title_only(self, api_client):
        """Test that random poems can be retrieved with only title field."""
        count = 5
        fields = "title"
        response = api_client.get_random(count, fields)
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        validate_response_schema(response_json, TITLE_ONLY_ARRAY_SCHEMA)
        assert validate_response_count(response_json, count)
        
        for poem in response_json:
            assert "title" in poem
            assert "author" not in poem
            assert "lines" not in poem
    
    def test_random_distribution(self, api_client):
        """Test that random poems appear to have a reasonable distribution."""
        # Make multiple requests and collect titles
        count = 5
        fields = "title"
        iterations = 3
        all_titles = set()
        
        for _ in range(iterations):
            response = api_client.get_random(count, fields)
            assert response.status_code == HTTPStatus.OK
            
            response_json = response.json()
            assert validate_response_count(response_json, count)
            
            # Extract and add titles to our collection
            for poem in response_json:
                all_titles.add(poem['title'])
        
        # We should have more than just a single set of random poems
        # (this test could fail by chance, but it's unlikely)
        assert len(all_titles) > count
    
    def test_random_no_duplicates(self, api_client):
        """Test that a single random response doesn't contain duplicates."""
        count = 10  # Use a larger count to make the test more meaningful
        fields = "title"
        response = api_client.get_random(count, fields)
        
        assert response.status_code == HTTPStatus.OK
        
        response_json = response.json()
        assert validate_response_count(response_json, count)
        
        # Check that all titles are unique within this response
        titles = [poem['title'] for poem in response_json]
        assert len(titles) == len(set(titles)) 