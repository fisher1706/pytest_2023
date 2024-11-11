from src.ip_adress.ip_address import IPAddress
import pytest
import subprocess


def test_ipaddress_attrs():
    ip1 = IPAddress("10.1.1.1", 25)
    assert ip1.ip == "10.1.1.1"
    assert ip1.mask == 25


def test_ipaddress_str_repr():
    ip1 = IPAddress("10.1.1.1", 25)
    assert str(ip1) == "10.1.1.1/25"
    assert repr(ip1) == "IPAddress('10.1.1.1', 25)"


def test_ipaddress_int():
    ip1 = IPAddress("10.1.1.1", 25)
    assert int(ip1) == 167837953


def test_ipaddress_cmp_basic():
    ip1 = IPAddress("10.2.1.1", 25)
    ip2 = IPAddress("10.10.1.1", 25)
    assert ip1 < ip2
    assert ip2 > ip1
    assert ip1 != ip2
    assert not ip1 == ip2
    assert ip1 <= ip2
    assert ip2 >= ip1


def test_ipaddress_cmp_mask():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = IPAddress("10.2.1.1", 25)
    assert ip1 < ip2
    assert ip2 > ip1
    assert ip1 != ip2
    assert not ip1 == ip2
    assert ip1 <= ip2
    assert ip2 >= ip1


def test_ipaddress_cmp_equal():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = IPAddress("10.2.1.1", 24)
    assert ip1 == ip2


def test_ipaddress_cmp_raise():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = 100
    with pytest.raises(TypeError):
        assert ip1 == ip2


"""
Фикстура capsys в pytest используется для захвата вывода в стандартный поток вывода (stdout)
и стандартный поток ошибок (stderr) во время выполнения тестов. Это полезно для проверки того,
что ваш код выводит правильные сообщения или для отладки.

Фикстура capsys — мощный инструмент для тестирования вывода вашего кода.
Она особенно полезна для написания тестов, которые проверяют правильность сообщений и ошибок,
выводимых вашим кодом, а также для захвата вывода внешних команд.
"""


def test_output(capsys):
    print("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def my_function():
    print("This is a test.")


def test_my_function(capsys):
    my_function()
    captured = capsys.readouterr()
    assert captured.out == "This is a test.\n"


def test_stderr(capsys):
    import sys
    print("This is stdout")
    print("This is stderr", file=sys.stderr)
    captured = capsys.readouterr()
    assert captured.out == "This is stdout\n"
    assert captured.err == "This is stderr\n"


def test_multiple_outputs(capsys):
    print("First output")
    captured1 = capsys.readouterr()
    assert captured1.out == "First output\n"
    assert captured1.err == ""

    print("Second output")
    captured2 = capsys.readouterr()
    assert captured2.out == "Second output\n"
    assert captured2.err == ""


# @pytest.skip
# def test_external_command(capsys):
#     subprocess.run(["echo", "Hello from subprocess"])
#     captured = capsys.readouterr()
#     assert captured.out == "Hello from subprocess\n"


def test_output_disabled(capsys):
    print("Output with capsys enabled")
    with capsys.disabled():
        print("Output with capsys disabled")
    captured = capsys.readouterr()
    assert captured.out == "Output with capsys enabled\n"


"""
Параметризация фикстур в pytest позволяет вам использовать одну фикстуру с разными значениями. Это полезно,
когда вы хотите протестировать одну и ту же функциональность с различными входными данными.
В pytest для этого используется декоратор @pytest.fixture с параметром params.
"""


def test_using_param_fixture(param_fixture):
    assert param_fixture in [1, 2, 3]


def test_multiple_fixtures(fruit_fixture, number_fixture):
    assert isinstance(fruit_fixture, str)
    assert isinstance(number_fixture, int)
