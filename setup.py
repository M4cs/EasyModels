import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''
    
setuptools.setup(
    name="EasyModels",
    version="1.6",
    author="Max Bridgland",
    install_requires=[
        'requests>=2.21.0',
        'terminaltables>=3.1.0',
        'PySimpleGUIQt>=0.26.0',
        'PySide2>=5.13.0',
        'crayons>=0.2.0'
    ],
    author_email="mabridgland@protonmail.com",
    description="Command Line User Interface for finding pre-trained AI models",
    long_description=readme(),
    long_description_content_type="text/markdown",
    entry_points = {
        'console_scripts': [
            'easymodels = easymodels.__main__:start'
        ]
    },
    keywords="AI, tensorflow, models, training, pre-train, pre-trained, artifical intelligence, keras, YOLO, opencv, pytorch, chainer, easymodels, ezmodels",
    url="https://github.com/M4cs/EasyModels",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
)
