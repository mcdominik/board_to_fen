from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]



setup(
   name='board_to_fen',
   version='0.0.14',
   author='Dominik Maćkiewicz',
   author_email='dominik.mackiewicz@icloud.com',
   packages=find_packages(),
   scripts=[],
   url='http://pypi.python.org/pypi/board_to_fen/',
   license='MIT',
   description='An package that converts digial chessboard image into Forsyth-Edwards notation',
   long_description=open('README.md').read(),
   include_package_data=True,
    long_description_content_type='text/markdown',
   python_requires='>=3.7',
   install_requires=['pillow']
)
