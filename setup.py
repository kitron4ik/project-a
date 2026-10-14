from setuptools import setup, find_packages

setup(
    name="project-b-utils",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Гетьман В. С.",
    description="Утилиты для работы с датами и строками",
    python_requires=">=3.8",
)
