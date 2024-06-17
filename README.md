Automatyzacja testów API z wykorzystaniem curl

Opis
Skrypt w języku Python do automatyzacji testów API z wykorzystaniem narzędzia `curl`. Skrypt wysyła żądania HTTP do publicznej API (JSONPlaceholder) i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

Wymagania
- Python 3.x
- curl

## Endpointy API
Testowane endpointy:
- `/posts` - sprawdza obecność klucza `userId` w odpowiedzi JSON.
- `/users` - sprawdza obecność klucza `id` w odpowiedzi JSON.
- `/todos` - sprawdza obecność klucza `userId` w odpowiedzi JSON.
