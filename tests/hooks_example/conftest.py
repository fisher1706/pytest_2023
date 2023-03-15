import pytest
from pathlib import Path
# from _pytest.main import Session
# from _pytest.nose import Item
# from _pytest.runner import CallInfo
# from _pytest.config import Config
# from _pytest.terminal import TerminalReporter

FAILURES_FILE = Path()/"failures.txt"


@pytest.hookimpl()
# def pytest_sessionstart(session: Session):
def pytest_sessionstart():
    if FAILURES_FILE.exists():
        FAILURES_FILE.unlink()
    FAILURES_FILE.touch()


@pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item: Item, call: CallInfo):
def pytest_runtest_makereport():
    outcome = yield
    print(f"\noutcome: {outcome}")

    result = outcome.get_result()
    print(f"\nresult: {result}")

    if result.when == 'call' and result.failed:
        try:
            with open(str(FAILURES_FILE), 'a') as f:
                f.write(result.nodeid + "\n")
        except Exception as e:
            print("ERROR", e)
            pass


@pytest.hookimpl(hookwrapper=True)
# def pytest_terminal_summary(terminalreporter: TerminalReporter, exitstatus: int, config: Config):
def pytest_terminal_summary():
    yield
    print(f"Failures output to: {FAILURES_FILE}")
    print(f"to see run\ncat {FAILURES_FILE}")
