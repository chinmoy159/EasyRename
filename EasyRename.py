import os
import shutil


class EasyRename:
    def __init__(self, root):
        self.root = root
        # contains '/' already

    @staticmethod
    def check_if_bokeh(filename):
        filename = filename.split(".")[0].split("_")
        filename = filename[len(filename) - 1]
        if filename.lower().__eq__("cover"):
            return True
        return False

    def recursion(self, cwd):
        cwd_path = os.walk(cwd).__next__()
        list_of_files = cwd_path[2]
        for it in list_of_files:
            bokeh_or_not = self.check_if_bokeh(it)
            src = "{0}/{1}".format(cwd_path[0], it)
            split_up = cwd_path[0].split("/")
            new_file_name = "{0}_{1}.jpg".format(split_up[len(split_up) - 1], "bokeh" if bokeh_or_not else "normal")
            dst = "{0}/{1}".format(cwd_path[0], new_file_name)
            os.rename(src, dst)
            src = dst
            # print("src - {0}".format(src))
            dst = dst.split("/")
            ndst = ""
            jt = 0
            while jt < len(dst) - 2:
                ndst = ndst + dst[jt] + "/"
                jt += 1
            ndst = ndst + dst[len(dst) - 1]
            # print("dst - {0}".format(ndst))
            shutil.move(src, ndst)
        list_of_directories = cwd_path[1]
        for it in list_of_directories:
            self.recursion("{0}/{1}".format(cwd_path[0], it))
        return

    def main(self):
        self.recursion(self.root)


# how to use
# Create an object like below,
# and pass the DCIM directory location as parameter.
# Ensure that the directory has a / (forward slash) at the end of the string.
# call the main() function of the program.
# Expected to create a directory, then add all the bokeh-mode picture folders to that directory.
# example -
# DIR_LOCATION : ~/Pixel_Images/
# where ~/Pixel_Images will have folder/s which contain the bokeh mode photos.

if __name__ == '__main__':
    obj = EasyRename("DIR_LOCATION")
    obj.main()
