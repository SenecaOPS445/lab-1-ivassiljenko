cat: /etc/redhat-release: No such file or directory
test_0 (__main__.lab1a.test_0)
[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for file creation: ./lab1a.py ... ok
test_a (__main__.lab1a.test_a)
[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for errors running: ./lab1a.py ... /usr/lib/python3.12/subprocess.py:822: ResourceWarning: unclosed file <_io.TextIOWrapper name=3 encoding='UTF-8'>
  _cleanup()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
FAIL

======================================================================
FAIL: test_a (__main__.lab1a.test_a)
[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for errors running: ./lab1a.py
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ivan/lab1-demo/./CheckLab1.py", line 71, in test_a
    self.assertEqual(return_code, 0, msg=error_output)
AssertionError: 1 != 0 : your program exited with a error(HINT: try running your program to see/read the error)

----------------------------------------------------------------------
Ran 2 tests in 0.134s

FAILED (failures=1)
OPS435 Lab Report - System Information for running ./CheckLab1.py
=================================================================
    User login name: ivan
    Linux system name: ivan-VirtualBox
    Linux system version: 
    Python executable: /usr/bin/python3
    Python version: 3123
    OS Platform: linux
    Working Directory: /home/ivan/lab1-demo
    Start at: Fri May 24 14:25:24 2024
=================================================================
