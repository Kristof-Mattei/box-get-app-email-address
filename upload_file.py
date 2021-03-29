from boxsdk import Client
import os

def upload_file_to_box(client: Client, target_folder_id: str, content_stream, file_name: str, file_size: int):
    # normal upload
    if file_size < 20000000: 
        new_file = client.folder(target_folder_id).upload_stream(content_stream, file_name, preflight_check=True, preflight_expected_size=file_size)
        print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))
    else:
        upload_session = client.folder(target_folder_id).create_upload_session(file_size, file_name)
        chunked_uploader = upload_session.get_chunked_uploader_for_stream(content_stream, file_size)
        uploaded_file = chunked_uploader.start()
        print('File "{0}" uploaded to Box with file ID {1}'.format(uploaded_file.name, uploaded_file.id))

def get_stream_from_file(path_to_file):
    return (open(path_to_file, 'rb'), os.path.basename(path_to_file), os.stat(path_to_file).st_size)
