import coverage
import unittest
import os
import DataBase
#
cov = coverage.Coverage(source=["DataBase"])
cov.start()

suite = unittest.TestLoader().discover(os.getcwd(), pattern="*_test.py")
unittest.TextTestRunner().run(suite)

cov.stop()
cov.save()

cov.html_report()
