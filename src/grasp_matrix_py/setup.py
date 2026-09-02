from setuptools import find_packages, setup

package_name = 'grasp_matrix_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shreehank1906',
    maintainer_email='skate@wpi.edu',
    description='Server and client nodes for grasp matrix computation',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'server = grasp_matrix_py.server:main',
            'client = grasp_matrix_py.client:main',
        ],
    },
)
