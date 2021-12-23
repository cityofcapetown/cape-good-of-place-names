"""
    Cape of Good Place Names Service

    This is a stateless service for performing various geotranslation operations, moving between how people describe places and codified coordinate systems.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: opmdata+cogpn-support@capetown.gov.za
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "cape-of-good-place-names-client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Cape of Good Place Names Service",
    author="City of Cape Town Data Science Unit",
    author_email="opmdata+cogpn-support@capetown.gov.za",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Cape of Good Place Names Service"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description="""\
    This is a stateless service for performing various geotranslation operations, moving between how people describe places and codified coordinate systems.  # noqa: E501
    """
)
