import os
import setuptools
import codecs

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


licenses = {
    'prop': ('Owned and distributed by sereact')
}
statuses = ['1 - Planning', '2 - Pre-Alpha', '3 - Alpha',
            '4 - Beta', '5 - Production/Stable', '6 - Mature', '7 - Inactive']
py_versions = '2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8'.split()


setuptools.setup(
    name = "moellava",
    license = licenses["prop"],
    classifiers = [
        'Development Status :: ' + statuses[2],
        'Intended Audience :: Developers' ,
        'License :: ' + licenses["prop"],
        'Natural Language :: English',
    ] + ['Programming Language :: Python :: '+o for o in py_versions[py_versions.index("3.8"):]],
    packages = setuptools.find_packages(),
    include_package_data = True,
    install_requires = [],
    python_requires  = '>=3.8',
    zip_safe = False,
    version='0.0.1'
    )


