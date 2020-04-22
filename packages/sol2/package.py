# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Sol2(CMakePackage):
    """a C++ <-> Lua API wrapper with advanced features and top notch performance"""

    homepage = "https://github.com/ThePhD/sol2"
    url      = "https://github.com/ThePhD/sol2/archive/v3.0.3.tar.gz"

    version('3.2.0', sha256='733f03d82df6e0e8a15967831840d240dcb2c606982bec753bd173a9cc1b3435')
    version('3.0.3', sha256='bf089e50387edfc70063e24fd7fbb693cceba4a50147d864fabedd1b33483582')

    depends_on('lua@5.1:')
