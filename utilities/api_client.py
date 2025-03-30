import requests
from urllib.parse import urljoin

class PoetryDBClient:
    """Client for interacting with the PoetryDB API."""
    
    BASE_URL = "https://poetrydb.org/"
    
    def __init__(self, base_url=None):
        """Initialize the API client.
        
        Args:
            base_url (str, optional): Base URL for the API. Defaults to BASE_URL.
        """
        self.base_url = base_url or self.BASE_URL
    
    def get_by_title(self, title, output_format=None):
        """Get poem(s) by title.
        
        Args:
            title (str): Title to search for
            output_format (str, optional): Output format (e.g., 'lines', 'author')
            
        Returns:
            requests.Response: API response
        """
        endpoint = f"title/{title}"
        if output_format:
            endpoint = f"{endpoint}/{output_format}"
        return self._make_request(endpoint)
    
    def get_by_author(self, author, output_format=None):
        """Get poem(s) by author.
        
        Args:
            author (str): Author to search for
            output_format (str, optional): Output format (e.g., 'lines', 'title')
            
        Returns:
            requests.Response: API response
        """
        endpoint = f"author/{author}"
        if output_format:
            endpoint = f"{endpoint}/{output_format}"
        return self._make_request(endpoint)
    
    def get_random(self, count, fields):
        """Get random poem(s).
        
        Args:
            count (int): Number of random poems to retrieve
            fields (str): Comma-separated list of fields to include
            
        Returns:
            requests.Response: API response
        """
        endpoint = f"random/{count}/{fields}"
        return self._make_request(endpoint)
    
    def combined_search(self, input_fields, search_terms, output_format=None):
        """Perform a combined search with multiple criteria.
        
        Args:
            input_fields (str): Comma-separated list of input fields
            search_terms (str): Semicolon-separated list of search terms
            output_format (str, optional): Output format specification
            
        Returns:
            requests.Response: API response
        """
        endpoint = f"{input_fields}/{search_terms}"
        if output_format:
            endpoint = f"{endpoint}/{output_format}"
        return self._make_request(endpoint)
    
    def _make_request(self, endpoint):
        """Make an API request.
        
        Args:
            endpoint (str): API endpoint to call
            
        Returns:
            requests.Response: API response
        """
        url = urljoin(self.base_url, endpoint)
        response = requests.get(url)
        return response 