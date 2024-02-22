from pathlib import Path

import pytest

FAILURES_FILE = Path()/"failures.txt"


@pytest.hookimpl()
def pytest_sessionstart():
    if FAILURES_FILE.exists():
        FAILURES_FILE.unlink()
    FAILURES_FILE.touch()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    print(f"\noutcome: {outcome}")

    result = outcome.get_result()
    print(f"\nresult: {result.__dict__}")

    if result.when == 'call' and result.failed:
        try:
            with open(str(FAILURES_FILE), 'a') as f:
                f.write(result.nodeid + "\n")
        except Exception as e:
            print("ERROR", e)
            pass
