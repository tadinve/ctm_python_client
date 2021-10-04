pip uninstall ctm_python_client -y
python -m pytest --cov=ctm_python_client
coverage run -m --source=./ctm_python_client pytest -rA tests/*.py tests/tests_indiv_jobs/*.py   && coverage report -m
pytest --nbmake  examples/python_notebooks/*.ipynb
coverage run -m  --source=./ctm_python_client/core pytest -rA tests/test_core_flow.py tests/test_complete_flow.py && coverage report -m