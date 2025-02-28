import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """
    Test the GET request to the index route.
    """
    response = client.get('/')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert b"The Bharat Translator" in response.data  # Check if the page title is present
    assert b"Enter text in English" in response.data  # Check if the placeholder text is present
    assert b"Translate" in response.data  # Check if the Translate button is present

def test_index_post(client):
    """
    Test the POST request to the index route with translation.
    """
    response = client.post('/', data={'text_to_translate': 'hello', 'target_language': 'hi'})
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert b"Translation in Hindi:" in response.data  # Check if the translation section is present
    assert "नमस्ते".encode('utf-8') in response.data  # Check if the translated text is present (hello -> नमस्ते)

def test_index_post_invalid_input(client):
    """
    Test the POST request to the index route with invalid input.
    """
    response = client.post('/', data={'text_to_translate': '', 'target_language': 'hi'})
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert b"No text provided for translation." in response.data  # Check for the error message