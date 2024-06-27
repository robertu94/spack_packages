# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.qoz import Qoz as BuiltinQoz


class Qoz(BuiltinQoz):
    """Quality optimized version of SZ3 is the next generation of the SZ compressor framework"""
