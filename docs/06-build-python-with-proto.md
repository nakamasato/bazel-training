# Build Python with protobuf


## Run python proto generated code with poetry

1. Prepare proto file `python/user.proto`

    ```protobuf
    syntax = "proto3";

    package user;

    message User {
      string id = 1;
      string name = 2;
    }
    ```
1. Generate Python code with `protoc` (run in the repo root dir)
    ```
    protoc -I=python --proto_path=python --python_out=python python/user.proto
    ```
    You'll see `python/user_pb2.py`

1. Use generated python code in `main.py`
    ```py
    import pandas as pd
    from python.user_pb2 import User

    if __name__ == '__main__':
        user = User()
        df = pd.DataFrame()
        print(f"hello, {user}, {df.shape}")
    ```
1. Add `protobuf` to poetry.

    ```
    poetry add protobuf
    ```
1. Run the main.py with poetry.
    ```
    poetry run python python/main.py
    hello, , (0, 0)
    ```

## Run python proto generated code with Bazel

1. Add the following to `WORKSPACE`

```
load("@rules_python//python:defs.bzl", "py_binary")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")


py_proto_library(
  name = "user_proto",
  srcs = ["user.proto"],
  visibility = ["//visibility:public"],
)

py_binary(
  name = "main",
  srcs = ["main.py"],
  deps = [
    ":user_proto",
    "protobuf",
  ],
)
```
