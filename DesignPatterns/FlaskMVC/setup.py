from setuptools import setup

setup(
    name="flaskmvc",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
