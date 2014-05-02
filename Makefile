PROJECT_NAME=bigfitnessgains

clean:
	rm -rf $(PROJECT_NAME)/static/CACHE
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*~" -exec rm -rf {} \;
