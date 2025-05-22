from setuptools import setup, find_packages

setup(
    name='text_corrector',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'language-tool-python>=2.7.0',
        'pyspellchecker>=0.6.2',
        'click>=8.1.0',
    ],
    entry_points={
        'console_scripts': [
            'text-corrector=corrector.cli:main'
        ]
    },
    author='Ваше Имя',
    description='Инструмент для поиска и исправления ошибок в тексте (RU)',
    python_requires='>=3.7',
)
