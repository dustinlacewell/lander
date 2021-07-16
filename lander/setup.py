setup(
    name="lander",
    version="1.0.0",
    description="Simple pygame Lunar Landard",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dustinlacewell/lander",
    author="Dustin Lacewell",
    author_email="dlacewell@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["lander"],
    include_package_data=True,
    install_requires=[
        "pygame", "shapely",
    ],
    entry_points={"console_scripts": ["lander=lander:main"]},
)
