from distutils.core import setup
 
setup(
    name = "mint_django_utils",
    version = "0.0.10",
    url = 'http://github.com/mintchaos/mint_django_utils',
    license = 'BSD',
    description = "A collection of utility functions, template tags and miscellany that I use for my djangos. Might only be useful to me.",
    author = 'Christian Metts',
    author_email = 'xian@mintchaos.com',
    packages = [
        'mint_django_utils',
        'mint_django_utils.templatetags',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)