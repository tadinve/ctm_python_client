pip uninstall ctm_python_client -y
python -m pytest --cov=ctm_python_client
pytest --nbmake  examples/python_notebooks/*.ipynb