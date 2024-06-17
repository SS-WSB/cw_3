import os
import json

# Funkcja do wysyłania żądania HTTP z użyciem curl
def send_request(url):
    response = os.popen(f"curl -s -w '%{{http_code}}' {url}").read()
    http_code = response[-3:]
    content = response[:-3]
    return int(http_code), content

# Funkcja do testowania endpointu
def test_endpoint(url, key):
    http_code, content = send_request(url)
    if http_code == 200:
        data = json.loads(content)
        if isinstance(data, list) and all(key in item for item in data):
            print(f"Test {url}: PASSED")
        else:
            print(f"Test {url}: FAILED - Key '{key}' not found in response JSON.")
    else:
        print(f"Test {url}: FAILED - HTTP status code {http_code}")

# Testy endpointów
def run_tests():
    base_url = "https://jsonplaceholder.typicode.com"
    endpoints = [("/posts", "userId"), ("/users", "id"), ("/todos", "userId")]

    for endpoint, key in endpoints:
        url = base_url + endpoint
        test_endpoint(url, key)

if __name__ == "__main__":
    run_tests()
