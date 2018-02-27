"""
The GPIO Zero mode for the Mu editor.

Copyright (c) 2015-2017 Nicholas H.Tollervey and others (see the AUTHORS file).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import logging
from mu.modes.python3 import PythonMode


logger = logging.getLogger(__name__)


class GPIOZeroMode(PythonMode):
    """
    Represents the functionality required by the GPIO Zero mode.
    """

    name = _('GPIO Zero')
    description = _('Use GPIO Zero remote mode.')

    def __init__(self, editor, view):
        os.environ['GPIOZERO_PIN_FACTORY'] = 'pigpio'
        os.environ['PIGPIO_ADDR'] = 'fe80::1%usb0'
        super().__init__(editor, view)
