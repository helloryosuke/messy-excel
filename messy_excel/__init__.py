# -*- coding: utf-8 -*-
#
# messy_excel: Split Pandas read_excel results into multiple dataframes
# https://github.com/helloryosuke/japan-real-estate-data
#
# Copyright 2021-2022 Ryosuke Inaba
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from . import version
from .parser import MessyExcel

__version__ = version.version
__author__ = "Ryosuke Inaba"

__all__ = ['MessyExcel']