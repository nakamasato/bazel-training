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

1. Confirm `WORKSPACE` already contains the following code.
    ```
    http_archive(
        name = "com_google_protobuf",
        sha256 = "930c2c3b5ecc6c9c12615cf5ad93f1cd6e12d0aba862b572e076259970ac3a53",
        strip_prefix = "protobuf-3.21.12",
        urls = [
            "https://mirror.bazel.build/github.com/protocolbuffers/protobuf/archive/v3.21.12.tar.gz",
            "https://github.com/protocolbuffers/protobuf/archive/v3.21.12.tar.gz",
        ],
    )

    load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

    protobuf_deps()
    ```
1. Update `python/BUILD.bazel

    ```
    load("@rules_python//python:defs.bzl", "py_binary")
    load("@poetry//:dependencies.bzl", "dependency")
    load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

    py_binary(
        name = "main",
        srcs = ["main.py"],
        deps = [
            dependency("pandas"),
            ":user_proto",
        ],
    )

    py_proto_library(
        name = "user_proto",
        srcs = ["user.proto"],
    )
    ```
1. Run.
    ```
    bazel run //python:main
    ```

    ```
    INFO: Analyzed target //python:main (2 packages loaded, 21 targets     configured).
    INFO: Found 1 target...
    Target //python:main up-to-date:
      bazel-bin/python/main
    INFO: Elapsed time: 1.692s, Critical Path: 0.13s
    INFO: 1 process: 1 internal.
    INFO: Build completed successfully, 1 total action
    INFO: Running command line: bazel-bin/python/main
    hello, , (0, 0)
    ```
