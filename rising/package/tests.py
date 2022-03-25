from package.models import *

packages = Package.objects.all()
for package in packages:
    print(package.packagedate_set.all())