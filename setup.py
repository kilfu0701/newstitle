setup(
      name='NewsTitle',
      version='0.0.1',
      packages=['newstitle'],
      author='GrapherD',
      author_email='grapherd@gmail.com',
      license='MIT',
      install_requires=["lxml>=2.41","httplib2>=0.7.6"],
      description="Catching Taiwan Newspaper title",
      entry_points ={
        'console_scripts':[
            'SlideGen=slidegen.SlideGen:Main'
        ]
      },
      keywords ='html5 slide generator',
      url='https://github.com/reyoung/SlideGen'
)
