pip uninstall ctm_python_client -y
python -m pytest --cov=ctm_python_client
coverage run -m --source=./ctm_python_client pytest
pytest --nbmake  examples/python_notebooks/*.ipynb