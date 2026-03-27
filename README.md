
# PYPI Package Build
<i>- PYPI packet build


### PYPI Package Deployment
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
    adding 'hey_utils-0.0.1.dist-info/RECORD'
    removing build\bdist.win-amd64\wheel
    Successfully built hey_utils-0.0.1.tar.gz and hey_utils-0.0.1-py3-none-any.whl
    
    # Test Site
    https://test.pypi.org/manage/projects/

    twine upload --repository testpypi dist/*

    # PYPI Deployment
    twine upload dist/*
  ```
  - __Test Packate Commands__
    ```bash
    python -m venv .test
    source .test/Scripts/activate

    pip install ./dist/*.whl
    pip install ./dist/*.whl --force-reinstall
    ...
    Collecting requests (from hey-utils==0.0.1)
    Downloading requests-2.33.0-py3-none-any.whl.metadata (5.1 kB)
    Collecting charset_normalizer<4,>=2 (from requests->hey-utils==0.0.1)
    Downloading charset_normalizer-3.4.6-cp311-cp311-win_amd64.whl.metadata (41 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.4/41.4 kB 662.0 kB/s eta 0:00:00
    
    $ pip list
    Package            Version
    ------------------ ---------
    certifi            2026.2.25
    charset-normalizer 3.4.6
    hey_utils          0.0.1
    idna               3.11
    pip                24.0
    requests           2.33.0
    setuptools         79.0.1
    urllib3            2.6.3
    ```



### Pytest
- Go to virtual enviroment using `source .test/bin/activate` or `./pytest.sh`
```bash
$ ./pytest.sh 
tests\test_packages.py::test_skip SKIPPED (no way of currently testing this)                                                                                                         [ 33%] 
tests\test_packages.py::test_module_func PASSED                                                                                                                                      [ 66%] 
tests\test_packages.py::test_gRPC PASSED                                                                                                                                             [100%]

===================================================================================== tests coverage ====================================================================================== 
____________________________________________________________________ coverage: platform win32, python 3.11.14-final-0 _____________________________________________________________________ 

Name                     Stmts   Miss  Cover
--------------------------------------------
tests\__init__.py            0      0   100%
tests\test_packages.py      14      1    93%
--------------------------------------------
TOTAL                       14      1    93%
============================================================================== 2 passed, 1 skipped in 0.15s =============================================================================== 
(.test) 
```