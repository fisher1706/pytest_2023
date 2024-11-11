# https://habr.com/ru/articles/448792/

"""
встроенная фикстура tmpdir создает данные в /tmp/pytest-of-oleg/pytest-21/test_tmpdir0

Значение, возвращаемое из tmpdir, является объектом типа py.path.local.1 это кажется все, что нам нужно для временных
каталогов и файлов. Тем не менее, есть одна хитрость. Поскольку фикстура tmpdir определена как область действия функции
(function scope), tmpdir нельзя использовать для создания папок или файлов, которые должны быть доступны дольше,
чем одна тестовая функция. Для фикстур с областью видимости, отличной от функции (класс, модуль, сеанс),
доступен tmpdir_factory.
"""


def test_tmpdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something_tmpdir.txt')

    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything')

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else_tmpdir.txt')

    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping tmpdir')

    # this write creates 'anything/something_else.txt'
    another_file.write('something different tmpdir')

    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping tmpdir'
    assert another_file.read() == 'something different tmpdir'


"""
Первая строка использует mktemp('mydir') для создания каталога и сохраняет его в a_dir. Для остальной части функции 
можно использовать a_dir так же, как tmpdir, возвращенный из фикстуры tmpdir.

Во второй строке примера tmpdir_factory функция getbasetemp() возвращает базовый каталог, используемый для данного 
сеанса. Оператор print в примере нужен, чтобы можно было посмотреть каталог в вашей системе.
"""


def test_tmpdir_factory(tmpdir_factory):
    # вы должны начать с создания каталога. a_dir действует как
    # объект, возвращенный из фикстуры tmpdir
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp будет родительским каталогом 'mydir' вам не нужно
    # использовать getbasetemp(), чтобы
    # показать, что он доступен
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # остальная часть этого теста выглядит так же,
    # как в Примере 'test_tmpdir ()', за исключением того,
    # что я использую a_dir вместо tmpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
