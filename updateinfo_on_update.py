# coding: utf8

# Copyright 2016 Michał Kaliński
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function


from dnf.cli.commands.updateinfo import UpdateInfoCommand
import dnf


class UpdateInfoOnUpdatePlugin(dnf.Plugin):
    name = 'updateinfo_on_update'

    def __init__(self, base, cli):
        super(UpdateInfoOnUpdatePlugin, self).__init__(base, cli)

        self.__base = base
        self.__command = UpdateInfoCommand(cli) if cli is not None else None

    def resolved(self):
        if self.__command is None:
            return

        upgraded = list(
                frozenset(
                    pkg.name for pkg in self.__base.transaction.install_set
                    ) &
                frozenset(
                    pkg.name for pkg in self.__base.transaction.remove_set
                    )
                )

        if not upgraded:
            return

        self.__print_banner('Changes in packages to be updated')
        self.__command.run(['info', 'updates'] + upgraded)
        self.__print_banner('End of changelog')

    @staticmethod
    def __print_banner(text):
        print(' {} '.format(text).center(79, '*'))
