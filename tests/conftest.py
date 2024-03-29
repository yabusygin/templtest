# templtest -- a tool for testing Ansible role templates
# Copyright (C) 2021-2023  Alexey Busygin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
from shutil import copytree

# Mypy doesn't understand `from sys import version_info` variant.
# See: https://github.com/python/mypy/issues/6189
import sys

from pytest import fixture

if sys.version_info >= (3, 9):
    from importlib.resources import files
else:
    from importlib_resources import files


@fixture
def resources(tmp_path):
    src_path = Path(files(__package__), "data")
    dest_path = Path(tmp_path, "data")
    return copytree(src_path, dest_path)
