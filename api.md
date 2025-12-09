# Files

Types:

```python
from witan.types import (
    FileRetrieveResponse,
    FileListResponse,
    FileDeleteResponse,
    FileUploadResponse,
)
```

Methods:

- <code title="get /v1/files/{fileId}">client.files.<a href="./src/witan/resources/files.py">retrieve</a>(file_id) -> <a href="./src/witan/types/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="get /v1/files">client.files.<a href="./src/witan/resources/files.py">list</a>(\*\*<a href="src/witan/types/file_list_params.py">params</a>) -> <a href="./src/witan/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{fileId}">client.files.<a href="./src/witan/resources/files.py">delete</a>(file_id) -> <a href="./src/witan/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{fileId}/content">client.files.<a href="./src/witan/resources/files.py">get_content</a>(file_id) -> BinaryAPIResponse</code>
- <code title="post /v1/files">client.files.<a href="./src/witan/resources/files.py">upload</a>() -> <a href="./src/witan/types/file_upload_response.py">FileUploadResponse</a></code>
