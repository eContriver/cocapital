# ------------------------------------------------------------------------------
#  Copyright (c) 2024 eContriver LLC
#  This file is part of Capital Copilot from eContriver.
#  -
#  Capital Copilot from eContriver is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#  -
#  Capital Copilot from eContriver is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  -
#  You should have received a copy of the GNU General Public License
#  along with Capital Copilot from eContriver.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "common"