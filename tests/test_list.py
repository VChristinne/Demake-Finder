import pytest
import sys

from components.ui.cli_controller import main

def test_list_files():
    sys.argv = ["../entrypoint.py", "/users/christinne/developer"]
    main()
