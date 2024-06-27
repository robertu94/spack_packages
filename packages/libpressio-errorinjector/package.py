# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_errorinjector import LibpressioErrorinjector as BuiltinLibPressioErrorInjector


class LibpressioErrorinjector(BuiltinLibPressioErrorInjector):
    """LibPressioErrorInjector injects errors into data for sensitivity studies"""

