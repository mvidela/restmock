========
RestMock
========

Rest mock es una aplicacion que permite definir, documentar y mockear
interfaces RESTull.

Por ejemplo, para mockear una url información de una url puede hacer

    >>> from restmock import URLMock
    >>> mock = URLMock('http://friendpaste.com/1wiKKD5qcZtzKCsrj5mdxM?param1=value1&param2=value2')
    >>> mock.scheme
    'http'
    >>> mock.netloc
    'friendpaste.com'
    >>> mock.path
    '/1wiKKD5qcZtzKCsrj5mdxM'
    >>> mock.params
    {'param2': 'value2', 'param1': 'value1'}

Una vez que el mock ha sido construido puede llamarse sucesivamente
para obtner nuevas respuestas.  Por ejemplo

    >>> mock.force('http://friendpaste.com/1wiKKD5qcZtzKCsrj5mdxM?param1=value1&param2=value2')
    >>> len(mock.responses)
    2



