# templtest -- a tool for testing Ansible role templates
# Copyright (C) 2021  Alexey Busygin
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


class GenericError(Exception):
    pass


class TestDefinitionError(GenericError):
    # Notify pytest that this is not a test class.
    # See: https://github.com/pytest-dev/pytest/issues/1879
    __test__ = False


class AssertError(GenericError):
    pass
