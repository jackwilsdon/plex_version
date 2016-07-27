import io as _io


def get_file_content(filename):
    with _io.open(filename, 'r') as file_stream:
        return file_stream.read()


__all__ = ('get_file_content',)
