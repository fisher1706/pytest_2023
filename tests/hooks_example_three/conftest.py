from pathlib import Path

import pytest

FAILURE_FILE = Path()/"tests/hooks_example_three/failures.txt"


@pytest.hookimpl()
def pytest_sessionstart():
    if FAILURE_FILE.exists():
        FAILURE_FILE.unlink()
    FAILURE_FILE.touch()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    print(f"\noutcome: {outcome}")

    result = outcome.get_result()
    print(f"\nresult: {result.__dict__}")

    if result.when == 'call' and result.failed:
        try:
            with open(str(FAILURE_FILE), 'a') as f:
                f.write(result.nodeid + "\n")
        except Exception as e:
            print("ERROR", e)
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary():
    yield
    print(f"\nFailures outputted to: {FAILURE_FILE} to see run\ncat {FAILURE_FILE}")
