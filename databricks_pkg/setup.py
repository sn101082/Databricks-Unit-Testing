from setuptools import setup, find_packages

data = {
    'name': 'databricks_pg',
    'version': '0.0.1',
    'packages': find_packages()
}

if __name__ == '__main__':
    setup(**data)