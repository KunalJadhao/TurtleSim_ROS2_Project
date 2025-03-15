from setuptools import setup

package_name = 'turtle_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kunal',
    maintainer_email='your-email@example.com',
    description='A simple ROS2 Python package to control a TurtleSim robot.',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'turtle_move = turtle_controller.turtle_move:main',
        ],
    },
)
