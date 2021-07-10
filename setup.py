import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uni_t-NSC",  # Replace with your own username
    version="0.0.1",
    author="Nate Costello",
    author_email="natecostello@gmail.com",
    description="A package that collects information from a UNI-T 61E DMM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natecostello/uni_t_status",
    project_urls={
        "Bug Tracker": "https://github.com/natecostello/uni_t_status/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['uni_t'],
    python_requires=">=3.6",
    install_requires=[
        "instrument_logger-NSC @ git+https://github.com/natecostello/instrument_logger.git",
        "ut61e-DM @ git+https://github.com/natecostello/ut61e_py.git"]
)