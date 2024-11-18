.PHONY: run

run:
	cd py-sumo-history && poetry run uvicorn py_sumo_history.main:app --reload
