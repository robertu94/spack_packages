# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
from spack.pkg.builtin.szx import Szx as BuiltinSzx



class Szx(BuiltinSzx):
    """An ultra fast error bounded compressor for scientific datasets"""
