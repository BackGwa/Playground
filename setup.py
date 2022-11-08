from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    
setup(  name='playground-python',
        version='1.0.1.0',
        description=long_description,
        long_description_content_type='text/markdown',
        author='BACKGWA',
        author_email='backgwa@icloud.com',
        url='https://github.com/BackGwa/Playground',
        license='BSD3',
        py_modules=['playground'],
        python_requires='>=3',
        install_requires=[],
        packages=['playground']
)