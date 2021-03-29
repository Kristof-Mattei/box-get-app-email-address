from .shared import get_box_client
from .get_app_user_login import get_box_client_login
from .upload_file import get_stream_from_file, upload_file_to_box

box_client = get_box_client()

# this value is the user that you need to add to a folder so it has rights
print(get_box_client_login(box_client))


folder_id = '123456'

(stream, file_name, file_size) = get_stream_from_file("/path/to/file")

upload_file_to_box(box_client, folder_id, stream, file_name, file_size)
