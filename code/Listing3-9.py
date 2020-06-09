ref1 = "foo"
ref2 = "foo"

del(ref2)  # reference count = 1 after this line executes
del(ref1)  # reference count = 0 after this line executes
