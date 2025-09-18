# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install opentelemetry-cpp
#
# You can edit this file again by typing:
#
#     spack edit opentelemetry-cpp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class OpentelemetryCpp(CMakePackage):
    """The OpenTelemetry C++ Client"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "opentelemetry.io/"
    url      = "https://github.com/open-telemetry/opentelemetry-cpp/archive/refs/tags/v1.0.0-rc1.tar.gz"
    git      = "https://github.com/open-telemetry/opentelemetry-cpp"

    # maintainers = ['github_user1', 'github_user2']

    version('main', branch="main")
    version('1.0.1', sha256='32f12ff15ec257e3462883f84bc291c2d5dc30055604c12ec4b46a36dfa3f189')
    version('1.0.0-rc1', sha256='4df1e67296d1f5ac09037d7c12581cdb2ae639f8dfd698efd6be4513a361b6cf')

    variant('shared', default=True, description="build shared libs")

    # FIXME: Add dependencies if required.
    depends_on('thrift+shared', when="+shared")
    depends_on('thrift~shared', when="~shared")

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING:BOOL=OFF",
            "-DWITH_EXAMPLES:BOOL=OFF",
            "-DWITH_JAEGER:BOOL=ON",
        ]
        if "+shared" in self.spec:
            args.append("-DCMAKE_POSITION_INDEPENDENT_CODE=ON")
            args.append("-DBUILD_SHARED_LIBS=ON")
        else:
            args.append("-DCMAKE_POSITION_INDEPENDENT_CODE=OFF")
            args.append("-DBUILD_SHARED_LIBS=OFF")

        return args
