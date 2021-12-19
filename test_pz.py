import pytest

from pz import summa, maximum, minimum, multi, creategiven


def test_summa():
    assert summa(['1', '3', '3']) == 7

def test_max():
    assert maximum(['1', '3', '4']) == 4

def test_min():
    assert minimum(['1', '3', '4']) == 1

def test_multi():
    assert multi(['1', '2']) == 2

def test_read():
    assert creategiven('text.txt') == ['1', '3', '2', '1']
#Тест на правильное чтение файла, специально для этого был создан файл