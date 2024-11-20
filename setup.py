from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Taisei　Suzuki',
    maintainer_email='iseita31kamekichi@gmail.com',
    description='ロボットシステム学のサンプル',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = mypkg.talker:main', #talker.pyのmain関数という意味
        #'listener = mypkg.listener:main', ←書いておいて後でコメントアウト   
        ],
    },
)
