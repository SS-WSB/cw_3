Makefile

Reguła install: Instaluje zależności
install:
    pip install -r requirements.txt || echo "No requirements file found, skipping installation."

Reguła test: Uruchamia testy jednostkowe
test:
    python -m unittest discover

Reguła run: Uruchamia aplikację
run:
    python main.py
