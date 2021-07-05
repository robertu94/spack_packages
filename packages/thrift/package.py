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
#     spack install thrift
#
# You can edit this file again by typing:
#
#     spack edit thrift
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Thrift(CMakePackage):
    """A lightweight, language-independent software stack for point-to-point RPC implementation"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/apache/thrift"
    url      = "https://github.com/apache/thrift/archive/refs/tags/v0.14.1.tar.gz"
    git = "https://github.com/apache/thrift"

    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')
    version('0.14.1', sha256='5ae1c4d16452a22eaf9d802ba7489907147c2b316ff38c9758918552fae5132c')
    version('0.12.0', sha256='b7452d1873c6c43a580d2b4ae38cfaf8fa098ee6dc2925bae98dce0c010b1366')
    version('0.11.0', url="https://github.com/apache/thrift/archive/refs/tags/0.11.0.tar.gz", sha256='0e324569321a1b626381baabbb98000c8dd3a59697292dbcc71e67135af0fefd')

    # FIXME: Add dependencies if required.
    depends_on('flex+lex')
    depends_on('openssl')
    depends_on('boost')
    depends_on('zlib')
    depends_on('libevent')

    variant('shared', default=True, description="build shared libraries")

    def cmake_args(self):
        args = [
                "-DBUILD_CPP:BOOL=ON",
                "-DBUILD_C_GLIB:BOOL=OFF",
                "-DBUILD_JAVA:BOOL=OFF",
                "-DBUILD_JAVASCRIPT:BOOL=OFF",
                "-DBUILD_NODEJS:BOOL=OFF",
                "-DBUILD_PYTHON:BOOL=OFF",
                "-DBUILD_HASKELL:BOOL=OFF",
                "-DBUILD_TESTING:BOOL=OFF",
        ]

        if "+shared" in self.spec:
            args.append("-DBUILD_SHARED_LIBS:BOOL=ON")
        else:
            args.append("-DBUILD_SHARED_LIBS:BOOL=OFF")

        return args
