import win32com.client


def get_file_metadata(path, file_name, meta_data):
    # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
    # filename must include extension, i.e. "PID manual.pdf"
    # Returns dictionary containing all file metadata.
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
    ns = sh.NameSpace(path)

    # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
    file_metadata = dict()
    item = ns.ParseName(str(file_name))
    for ind, attribute in enumerate(meta_data):
        attr_value = ns.GetDetailsOf(item, ind)
        if attr_value:
            file_metadata[attribute] = attr_value

    return file_metadata


print('\n!~ Printing important metadata from the provided file ~!\n')
# *Note: you must know the total path to the file.*
# Example usage:
if __name__ == '__main__':
    folder = 'E:\\Software\\GIMP'
    filename = 'gimp.exe'
    metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created']
    print(get_file_metadata(folder, filename, metadata))
