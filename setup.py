import setuptools


setuptools.setup(
    name="GPTConnect",
    version="0.1.4",
    author="SleepyStew",
    description="A python package to make GPT functions easy",
    packages=["gptconnect"],
    install_requires=["openai"],
    github_url="https://github.com/SleepyStew/gptconnect",
    long_description=open("README.md").read(),
)
