from setuptools import find_packages, setup

# imports lets us get setup to install the launch folder?
from glob import glob
import os

package_name = 'remote_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # tells setup to install the launch folder?
        ((os.path.join('share', package_name, 'launch')),
            glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kimhu',
    maintainer_email='huangkim@seas.upenn.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'remote_control = remote_control.joy_listener:main'
        ],
    },
)
