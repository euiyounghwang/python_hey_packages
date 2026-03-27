
# PYPI Package Build
<i>- PYPI packet build

- __PYPI Package Deployment__
  - Reference : https://hdevstudy.tistory.com/344#google_vignette, https://blog.advenoh.pe.kr/pypi-%EC%97%85%EB%A1%9C%EB%93%9C-%EA%B0%80%EC%9D%B4%EB%93%9C-%EB%82%98%EB%A7%8C%EC%9D%98-python-%ED%8C%A8%ED%82%A4%EC%A7%80-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0/
  - Trusted Host with `PIP` : `pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"`
  - __Installation Commands__
    ```bash
    pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"
    pip install build --trusted-host pypi.org --trusted-host files.pythonhosted.org

    python -m build
    * Creating isolated environment: venv+pip...
    * Installing packages in isolated environment:
    - setuptools
    - wheel
    * Getting build dependencies for sdist...
    ...

    # Test Site
    https://test.pypi.org/manage/projects/

    twine upload --repository testpypi dist/*

    # PYPI Deployment
    twine upload dist/*
  ```