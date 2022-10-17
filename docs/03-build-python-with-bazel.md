# Build Python with bazel


https://github.com/bazelbuild/rules_python


1. WORKSPACE
    ```
    load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
    http_archive(
        name = "rules_python",
        sha256 = "8c8fe44ef0a9afc256d1e75ad5f448bb59b81aba149b8958f02f7b3a98f5d9b4",
        strip_prefix = "rules_python-0.13.0",
        url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.13.0.tar.gz",
    )
    ```

1. `python/main.py`
    ```python
    if __name__ == '__main__':
        print("hello world")
    ```

1. `python/BUILD.bazel`
    ```
    load("@rules_python//python:defs.bzl", "py_binary")

    py_binary(
      name = "main",
      srcs = ["main.py"],
    )
    ```
1. Run python with Bazel
    ```
    bazel run //python:main
    ```

    ```
    INFO: Analyzed target //python:main (0 packages loaded, 0 targets configured).
    INFO: Found 1 target...
    Target //python:main up-to-date:
      bazel-bin/python/main
    INFO: Elapsed time: 0.352s, Critical Path: 0.00s
    INFO: 1 process: 1 internal.
    INFO: Build completed successfully, 1 total action
    INFO: Build completed successfully, 1 total action
    hello world
    ```
