export PYTHONPATH=$PWD:$PYTHONPATH
pip uninstall ctm_python_client -y
coverage run -m --source=./ctm_python_client/jobs pytest -rA  tests/tests_indiv_jobs/*.py   && coverage report -m
pytest --nbmake  examples/python_notebooks/*.ipynb
coverage run -m  --source=./ctm_python_client/core pytest -rA tests/test_core_flow.py tests/test_complete_flow.py && coverage report -m