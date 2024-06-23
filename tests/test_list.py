import pytest
import sys

from components.ui.cli_controller import main

class TestList:
    def test_list_files(self):
        sys.argv = ["../entrypoint.py", "/users/christinne/developer"]
        main()

    def test_list_size(self):
        sys.argv = ["../entrypoint.py", "/users/christinne/developer", "-s"]
        main()


class TestUserInput:
    @pytest.mark.xfail(reason="Invalid directory", raises=SystemExit)
    def test_invalid_directory(self):
        sys.argv = ["../entrypoint.py", "/invalid"]
        main()

    @pytest.mark.xfail(reason="Invalid argument", raises=SystemExit)
    def test_invalid_args(self):
        sys.argv = ["../entrypoint.py", "/users/christinne/developer", "-x"]
        main()

if __name__ == '__main__':
    TestList()
    TestUserInput()