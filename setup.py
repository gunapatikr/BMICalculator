import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BMICalculator",
    version="1.0.0",
    author="Karthik Gunapati",
    author_email="gunapatikr@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["BMICalculator"],
    python_requires=">=3.8",
)

