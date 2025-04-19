# This file is part of excluded_visits.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
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

from astropy.table import Table


def test_bad_visit_list():
    """Confirm that the bad visit lists can be loaded successfully.

    Also tests that the exposure values are reasonable. The comment column is
    free-form and is not tested.
    """

    instruments = ["LSSTComCam"]

    for instrument in instruments:

        bad_visits = Table.read(f"{instrument}/bad.ecsv")

        assert (bad_visits['exposure'] > 2024100100000).all()
        assert (bad_visits['exposure'] < 2034010100000).all()
