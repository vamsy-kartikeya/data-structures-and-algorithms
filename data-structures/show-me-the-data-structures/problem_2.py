import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    
    result 
    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    
    matching_files = []

    # Iterate over all files and directories in the current directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            # Recursively search in subdirectories
            matching_files.extend(find_files(suffix, item_path))
        elif os.path.isfile(item_path) and item.endswith(suffix):
            # If it's a file and matches the suffix, add to the list
            matching_files.append(item_path.split('/')[-1])

        
    
    return matching_files


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    absolute_path = "/Users/vamsyvaddi/Desktop/Learning/data-structures-and-algorithms/data-structures/show-me-the-data-structures"
    masked_path = os.path.relpath(absolute_path, start=os.getcwd())

    print(masked_path)
    result = find_files(".c", "/Users/vamsyvaddi/Desktop/Learning/data-structures-and-algorithms/data-structures/show-me-the-data-structures/testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    # print(os.listdir('/Users/vamsyvaddi/Desktop/Learning/data-structures-and-algorithms/data-structures/show-me-the-data-structures/testdir'))
    # print(os.path.isdir('/Users/vamsyvaddi/Desktop/Learning/data-structures-and-algorithms/data-structures/show-me-the-data-structures/testdir'))
    # Test Case 2
    pass

    # Test Case 3
    pass