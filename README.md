
sourcewater

水源聚合了多个开放finance数据源，yahoo_finance（雅虎财经），wbdata（世界银行），knoema，pytdx（通达信），tushare，quandl，python_binance（币安）等（数据源在增加中...）

Dependencies
=========
python 2.x/3.x   

[pandas](http://pandas.pydata.org/ "pandas")


Installation
====

- 方式1：pip install shuiyuan
- 方式2：python setup.py install
- 方式3：访问[https://pypi.python.org/pypi/shuiyuan/](https://pypi.python.org/pypi/shuiyuan/)下载安装


Upgrade
=======

	pip install shuiyuan --upgrade

Start
======
**Yahoo_finance（雅虎财经）:** [https://github.com/lukaszbanasiak/yahoo-finance](http://pandas.pydata.org/)

    import shuiyuan as sy
    yahoo_financ = sy.get_yahoo_finance()
    

**Wbdata（世界银行）:** [https://github.com/OliverSherouse/wbdata](https://github.com/OliverSherouse/wbdata)
    
    import shuiyuan as sy
    wbdata = sy.get_wbdata()

**Knoema :** [https://github.com/Knoema/knoema-python-driver](https://github.com/Knoema/knoema-python-driver)
    
    import shuiyuan as sy
    sy.get_knoemaa()

**Pytdx（通达信) :** [https://github.com/rainx/pytdx](https://github.com/rainx/pytdx)
    
    import shuiyuan as sy
    pytdx = sy.get_pytdx()

**Tushare :** [https://github.com/waditu/tushare](https://github.com/waditu/tushare)
    
    import shuiyuan as sy
    tushare = sy.get_tushare()

**Quandl :** [https://github.com/quandl/quandl-python](https://github.com/quandl/quandl-python)
    
    import shuiyuan as sy
    quandl = sy.get_quandl()

**Python_binance :** [https://github.com/sammchardy/python-binance](https://github.com/sammchardy/python-binance)
    
    import shuiyuan as sy
    python_binance = sy.get_python_binance()

    
