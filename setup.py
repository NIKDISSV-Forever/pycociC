import setuptools

with open('README.md', encoding='UTF-8') as f:
    long_description = f.read().strip()
with open('requirements.txt', encoding='UTF-8') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="pycociC",

    version="1.1.0",

    author="Nikita (NIKDISSV)",
    author_email="nikdissv@proton.me",

    description="Remove pycache (and numba cache) files",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/NIKDISSV-Forever/pycociC",
    install_requires=install_requires,
    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',

        'Intended Audience :: Developers',

        'Natural Language :: English',

        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',

        'License :: OSI Approved :: MIT License',

        'Topic :: Software Development',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',

        'Typing :: Typed',
    ],

    python_requires='>=3.8',
)
