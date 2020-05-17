import os, sys

def _raise(err: Exception):
    
    print("%s: %s" % (err.__class__.__name__, err))
    input("\n> Press enter to quit")
    exit()

def main():
    projects_path = ["C:\\", "Users","skovborg","Documents","projects"]
    projects_path = os.path.join(*projects_path)

    if not len(sys.argv) > 1:
        _raise(ValueError("Please specify a project folder to open!"))

    project_path = os.path.join(projects_path, sys.argv[1])

    if not os.path.exists(project_path):
        _raise(AttributeError("Could not find <%s>" % project_path))

    os.system("code %s" % project_path)
    os.system("cmd /k cd %s" % project_path)

if __name__ == '__main__':
    main()
