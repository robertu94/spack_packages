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
#     spack install reeber
#
# You can edit this file again by typing:
#
#     spack edit reeber
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Reeber(CMakePackage):
    """A library for shared- and distributed-memory parallel computation of merge trees."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/mrzv/reeber"
    url      = "https://github.com/mrzv/reeber"
    git      = url

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')

    depends_on('diy@master')
    depends_on('mpi')
    depends_on('boost')
    depends_on('amrex+amrdata@20.11', when="+amrex")
    depends_on('intel-tbb', when="+tbb")
    depends_on('hdf5')

    variant("amrex", description="support for armex", default=False)
    variant("tbb", description="support for tbb", default=False)
    variant("examples", description="install examples", default=False)

    patch("install_examples.patch")

    def cmake_args(self):
        args = []
        args.append("-DDIY_INCLUDE_DIR=" + self.spec['diy'].prefix + "/include")
        if "+amrex" in self.spec:
            args.append("-Damrex=ON")
            args.append("-DAMReX_DIR=" + self.spec['amrex'].prefix)
        if "+tbb" in self.spec:
            args.append("-Duse-tbb=ON")
        if "+examples" in self.spec:
            args.append("-Dinstall_examples=ON")
        return args

