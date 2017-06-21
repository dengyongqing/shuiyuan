# Boilerplate for python modules

### How to create python pypi package
* register accounts on [pypi test](https://testpypi.python.org/pypi) and [pypi legacy](https://pypi.python.org/pypi)
* create `~/.pypirc` file with content:
    ```
    [distutils]
    index-servers=
        pypi
        test
    
    [test]
    repository = https://testpypi.python.org/pypi
    username = pypi_test_login
    password = pypi_test_password
    
    [pypi]
    repository = https://pypi.python.org/pypi
    username = pypi_legacy_login
    password = pypi_legacy_password
    ```
* clone [this repository](https://github.com/aLkRicha/pypi_package_template)
* remove `.git` folder
* create your package (for example use `package_name`)
* when you're ready to add a project to pypi edit `setup.py` with your settings
* when the setting is complete, register package on test server:  
    `python setup.py register -r test`
* prepare (build your package):  
    `python setup.py bdist_wheel sdist`
* now you could try test your package in two ways:
    * install package from test pypi:  
        `pip install -i https://testpypi.python.org/pypi PACKAGENAME`
    * install package from wheel:  
        `pip install dist/my-project.whl`
    * in both cases use new `virtualenv` 
* if all is ok, you could register package on legacy pypi server:  
    `python setup.py register -r pypi`
* upload prepared files:  
    `twine upload dist/*`
    
Now you can use you package: `pip install PACKAGENAME` 😎 
