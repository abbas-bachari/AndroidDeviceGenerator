from setuptools import setup, find_packages

setup(
    name='AndroidDeviceGenerator',
    version='1.0.1',
    author='Abbas Bachari',
    author_email='abbas-bachari@hotmail.com',
    description='Android device model and user-agent Generator',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/abbas-bachari/AndroidDeviceGenerator',
    python_requires='>=3.10',
    project_urls={
    "Homepage":'https://github.com/abbas-bachari/AndroidDeviceGenerator',
    'Documentation': 'https://github.com/abbas-bachari/AndroidDeviceGenerator',
    'Source': 'https://github.com/abbas-bachari/AndroidDeviceGenerator/',
    'Tracker': 'https://github.com/abbas-bachari/AndroidDeviceGenerator/issues',
   
},
    
    install_requires=[],
    
    keywords=['useragent', 'fake-useragent', 'python-useragent','android-device', 'AndroidDeviceGenerator',  'api', 'abbas bachari'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
        
        
        
    ],
)


