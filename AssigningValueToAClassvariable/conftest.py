import pytest

@pytest.yield_fixture(scope='class')
def setUp(request):
    if request.cls is None:
        request.cls.value = 100


