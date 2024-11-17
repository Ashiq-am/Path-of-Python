import pkg_resources

installed_packages = pkg_resources.working_set
opencv_version = [
    pkg for pkg in installed_packages if pkg.key == 'opencv-python'][0].version
print("OpenCV version (via pkg_resources):", opencv_version)
