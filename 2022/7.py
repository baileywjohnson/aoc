class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.children = []
        self.parent = parent
    
    def add_file(self, name, size):
        self.files.append((name, size))

    def add_child(self, name):
        self.children.append(name)


with open('7.txt') as f:

    def get_dir_size(dir: Directory, map):
        size = 0

        sum_of_children_sizes = 0
        for child in dir.children:
            sum_of_children_sizes += get_dir_size(child, map)

        sum_of_file_sizes = 0
        for file in dir.files:
            sum_of_file_sizes += file[1]

        size = sum_of_children_sizes + sum_of_file_sizes
        
        map[dir] = size # Originally Had This As map[dir.name] = size, Failed Because of Multiple Dirs w/ Same Name
        return size

    root = None
    curDir = ''
    for line in f.readlines():
        line = line.strip()
        if line[0] == '$':
            if line.split()[1] == 'cd':
                if line.split()[2] == '..':
                    curDir = curDir.parent
                else:
                    if line.split()[2] == '/':
                        root = Directory('/')
                        curDir = root
                    else:
                        newDir = Directory(line.split()[2], curDir)
                        curDir.add_child(newDir)
                        curDir = newDir
        else:
            if line[0] != 'd':
                file_size = int(line.split()[0])
                file_name = line.split()[1]
                curDir.add_file(file_name, file_size)
    
    # Iterate Through Map, Sum Sizes of All Dirs w/ Size < 100000
    dir_size_map = {}
    used_space = get_dir_size(root, dir_size_map)

    # Get Size of Unused Space
    unused_space = 70000000 - used_space
    # Update Requires 30000000
    required_deletion = 30000000 - unused_space


    # Need One Atleast required_deletion big, choose smallest though

    current_min_meets_threshold = float('inf')
    total_size = 0
    used_space = 0
    for dir, size in dir_size_map.items():
        if size <= 100000:
            total_size += size
        if size >= required_deletion:
            if size < current_min_meets_threshold:
                current_min_meets_threshold = size
    print(total_size)
    print(current_min_meets_threshold)