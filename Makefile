init: requirements.txt
	pip install -r $<

.PHONY = init