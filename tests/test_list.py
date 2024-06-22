import pytest
import sys

from components.ui.cli_controller import main

class TestList:
    def test_list_files(self):
        sys.argv = ["../entrypoint.py", "/users/christinne/developer"]
        main()

    def test_list_files_size(self):
        sys.argv = ["../entrypoint.py", "/users/christinne/developer", "-s"]
        main()
