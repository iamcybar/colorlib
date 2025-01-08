from setuptools import setup, find_packages

setup(
    name='colorlib',
    version='0.1',
    description='A Python library for working with colors.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Asiegbu Caleb',
    author_email='asiegbucaleb3@gmail.com',
    url='https://github.com/your-username/colorlib',
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',  # Adjust Python versions as needed
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
