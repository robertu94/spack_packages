# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install sperr
#
# You can edit this file again by typing:
#
#     spack edit sperr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Sperr(CMakePackage):
    """SPERR is a lossy scientific (floating-point) data compressor that can perform either error-bounded or size-bounded data compression"""

    homepage = "https://github.com/shaomeng/SPERR"
    git      = "https://github.com/shaomeng/SPERR"

    version('2022.05.25', commit="6e73e57fe4343f9e8bb4ed42cf677b6cba99f570")

    depends_on('git')

    variant('shared', description="build shared libaries", default=True)
    variant('qz', description="coding terminates by quantization level", default=True)
    variant('zstd', description="use Zstd for more compression", default=False)

    def cmake_args(self):
        args = [
            self.define_from_variant('BUILD_SHARED_LIBS',  'shared'),
            self.define_from_variant('QZ_TERM',  'qz'),
            "-DUSE_ZSTD=OFF",
            #self.define_from_variant('USE_ZSTD',  'zstd'), TODO remove packaged deps
            "-DBUILD_CLI_UTILITIES=OFF"
            "-DBUILD_UNIT_TESTS=OFF"
        ]
        return args
