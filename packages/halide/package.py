# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install halide
#
# You can edit this file again by typing:
#
#     spack edit halide
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Halide(CMakePackage):
    """Halide is a programming language designed to make it easier to write
    high-performance image and array processing code on modern machines"""

    homepage = "https://github.com/halide/Halide"
    url      = "https://www.example.com/example-1.2.3.tar.gz"
    git      = "https://github.com/halide/Halide"
    generator = 'Ninja'

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')
    version('10.0.0', sha256='23808f8e9746aea25349a16da92e89ae320990df3c315c309789fb209ee40f20')

    depends_on('llvm', type=('build','link','run'))
    depends_on('ninja', type='build')
    depends_on('libpng')
    depends_on('libjpeg-turbo')

    variant('shared', default=True, description="build shared libraries")
    variant('python', default=False, description="build shared libraries")

    def cmake_args(self):
        args =  ['-DHalide_SHARED_LLVM=ON',
                 "-DWITH_TESTS=OFF",
                 "-DWITH_TUTORIAL=OFF",
                 "-DWITH_APPS=OFF",
                 '-G' 'Ninja']

        if "+python" in self.spec:
            args.append("-DWITH_PYTHON_BINDINGS=ON")
        else:
            args.append("-DWITH_PYTHON_BINDINGS=OFF")

        if "+shared" in self.spec:
            args.append("-DBUILD_SHARED_LIBS=ON")
        else:
            args.append("-DBUILD_SHARED_LIBS=OFF")

        return args
