import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BuildScour",
    version="1.0.3",
    license='MIT',  
    keywords = ['CI', 'RECONNAISSANCE', 'TRAVIS','LOGS','CIRCLE-CI'],
    author="Darsh Patel",
    author_email="darshkpatel@gmail.com",
    description="Scours CI Build logs for github Organizations/Users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darshkpatel/BuildScour",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    install_requires=['argparse','requests']
)