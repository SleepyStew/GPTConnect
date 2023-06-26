import setuptools


setuptools.setup(
    name="GPTConnect",
    version="0.2.4",
    author="SleepyStew",
    description="A python package to make GPT functions easy",
    packages=["gptconnect"],
    install_requires=["openai"],
    url="https://github.com/SleepyStew/gptconnect",
    long_description=open("README.md", encoding="utf-8").read(),
    license="Apache 2.0",
)
