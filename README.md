# Use Django In Gevent Mode

sometimes you need to make django in the gevent mode way.
it's ok to do this, the biggest problem is the **MYSQLDB**, which
does not allow to share descriptor between thread, maybe because
it use the mysql c library.

# Require

use pymysql

``` shell
pip install pymysql
```

pymysql is a pure python implemented mysql client, it's ok to use
it as the django mysql backend client, but you need to aware that
it's slower than mysqlDB.

# Run

use uwsgi to run the sample uwsgi config `/3rd/wsgi.ini`.
