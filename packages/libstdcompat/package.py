# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libstdcompat(CMakePackage):
    """A compatibility header for C++14, 17, and 20 for C++11"""

    homepage = "https://github.com/robertu94/std_compat"
    url      = "https://github.com/robertu94/std_compat/archive/0.0.1.tar.gz"
    git      = "https://github.com/robertu94/std_compat"

    maintainers = ['robertu94']

    version('master', branch='master')
    version('0.0.2', sha256='36424399e649be38bdb21899aa45f94aebba25c66048bab2751b1b3b9fd27238')
    version('0.0.1', sha256='3d63e901f4e20b9032a67086f4b4281f641ee0dea436cf15f7058faa40d8637b')

    variant('boost', default=False, description='support older compilers using boost')

    depends_on('boost', when="+boost")

    def cmake_args(self):
        args = []
        if "+boost" in self.spec:
            args.append("-DSTDCOMPAT_CXX_VERSION=11")
        return args
