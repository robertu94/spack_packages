# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLangchainCommunity(PythonPackage):
    """LangChain Community contains third-party integrations that implement the base interfaces defined in LangChain Core, making them ready-to-use in any LangChain application"""

    homepage = "https://python.langchain.com/docs"
    url = "https://files.pythonhosted.org/packages/44/21/0c26e7f4cbea8ecc22c21dda8cca29a378b9d2795aebaa47ed40b130979d/langchain_community-0.0.20-py3-none-any.whl"

    maintainers("robertu94")

    license("MIT", checked_by="robertu94")

    version("0.0.20", sha256="bd112b5813702919c50f89b1afa2b63adf1da89999df4842b327ee11220f8c39", expand=False)

    depends_on("python@3.8.1:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-langchain-core@0.1.21:2", type=("build","run"))
    depends_on("py-sqlalchemy@2.0.19", type=("build","run"))
    depends_on("py-requests@2", type=("build","run"))
    depends_on("py-numpy@1", type=("build","run"))
    depends_on("py-dataclasses-json@0.5.7:0.6", type=("build","run"))
    depends_on("py-langsmith@0.1:", type=("build","run"))
    depends_on("py-aiohttp@3.8.3:", type=("build","run"))
