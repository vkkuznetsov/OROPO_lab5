all: install test run

install:
	@python3 -m venv venv
	@source venv/bin/activate && pip install -r requirements.txt

test:
	@pytest -q --tb=short --disable-warnings

run:
	@python -m lab

winstall:
	@python -m venv venv
	@.\venv\Scripts\activate && pip install -r requirements.txt