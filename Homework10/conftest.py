import pytest
import time

@pytest.fixture(scope="class")
def class_fixture(request):
    start_time = time.time()
    print(f"\nНачало выполнения класса {request.cls.__name__}: {time.ctime(start_time)}")
    yield
    end_time = time.time()
    print(f"\nОкончание выполнения класса {request.cls.__name__}: {time.ctime(end_time)}")

@pytest.fixture
def test_duration_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nВремя выполнения теста: {duration:.2f} секунд")