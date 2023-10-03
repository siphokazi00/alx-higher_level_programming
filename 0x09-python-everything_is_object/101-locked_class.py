class LockedClass:
    def __setattr__(self, attr, value):
        if attr == "first_name":
            self.__dict__[attr] = value
        else:
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(attr))
