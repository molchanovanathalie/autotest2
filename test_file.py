from .checks import checkout
import pytest


folderin = '/home/acer/test'
folderout = '/home/acer/out'
folderext = '/home/acer/folder'



def test_step1():
    assert checkout(f'cd {folderin}; 7z a {folderout}/arh1.7z', 'Everything is Ok'), 'test_step1 FAIL'

def test_step2():
    res1 = checkout('cd {};7z x arx1.7z'.format(folderout), 'Everything is Ok')
    res2 = checkout('ls {}'.format(folderout), 'test_step2')
    assert res1 and res2, 'test_step2 FAIL'

def test_step3():
    assert (checkout('cd {};7z l arx1.7z'.format(folderout), 'test_step3')), 'test_step3 FAIL'

if __name__ == '__main__':
    pytest.main(['-vv'])