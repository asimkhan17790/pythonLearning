# Similar to args, we van pass dictionary as variable numbe of args

def marks(**kwargs):
    for item in kwargs.keys():
        print(kwargs[item])


marks(shubham=34, asim=54, sana=45)

print("-----")
marks(asim="Guy", sana="Girl", nyc=True, hudson=7302, coffee="yes")
