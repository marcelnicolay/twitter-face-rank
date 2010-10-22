clean:
	@echo "Cleaning up build and *.pyc files..."
	@find . -name '*.pyc' -exec rm -rf {} \;
	@rm -rf build

start:
	@echo "Running twittface http://localhost:8080..."
	@cd twittface && python start.py start