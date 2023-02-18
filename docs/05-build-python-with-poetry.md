# [Build Python with poetry dependencies](https://github.com/soniaai/rules_poetry)

## Poetry version

version <1.3.0 (as poetry rule hasn't supported [new poetry.lock format introduced in 1.3.0](https://python-poetry.org/blog/announcing-poetry-1.3.0/#new-lock-file-format))

```
curl -sSL https://install.python-poetry.org | python3 - --version 1.2.2
```

## Prepare Python app with poetry
1. Add poetry to `python` in the root directory
    ```
    poetry init
    poetry add pandas # add any dependencies
    ```
1. Update main to use the dependencies.
    ```py
    import pandas as pd

    if __name__ == '__main__':
        df = pd.DataFrame()
        print(f"hello, {df.shape}")
    ```
1. Run without bazel
    ```
    poetry run python python/main.py
    hello, (0, 0)
    ```

## Bazel configuration
1. WORKSPACE

    ```
    # Poetry rules for managing Python dependencies

    http_archive(
        name = "com_sonia_rules_poetry",
        sha256 = "8a7a6a5d2ef859ba4309929f3b4d61031f2a4bfed6f450f04ab09443246a4b5c",
        strip_prefix = "rules_poetry-ecd0d9c66b89403667304b11da3bd99764797a63",
        urls = ["https://github.com/soniaai/rules_poetry/archive/ecd0d9c66b89403667304b11da3bd99764797a63.tar.gz"],
    )

    load("@com_sonia_rules_poetry//rules_poetry:defs.bzl", "poetry_deps")

    poetry_deps()

    load("@com_sonia_rules_poetry//rules_poetry:poetry.bzl", "poetry")

    poetry(
        name = "poetry",
        lockfile = "//:poetry.lock",
        pyproject = "//:pyproject.toml",
        # optional, if you would like to pull from pip instead of a Bazel cache
        tags = ["no-remote-cache"],
    )
    ```


1. Update `python/BUILD.bazel`

    ```
    load("@poetry//:dependencies.bzl", "dependency")
    load("@rules_python//python:defs.bzl", "py_binary")

    py_binary(
      name = "main",
      srcs = ["main.py"],
      deps = [
        dependency("pandas")
      ],
    )
    ```

1. Run
    ```
    bazel run //python:main
    hello, (0, 0)
    ```

    Successfully read from poetry.lock

## Error

```
ERROR: An error occurred during the fetch of repository 'poetry':
   Traceback (most recent call last):
        File "/private/var/tmp/_bazel_m.naka/687932582dc396e76af9f4754f6b0686/external/com_sonia_rules_poetry/rules_poetry/poetry.bzl", line 119, column 13, in _impl
                fail("Did not find file hashes in poetry.lock file")
```

- https://github.com/soniaai/rules_poetry/issues/22
- https://github.com/soniaai/rules_poetry/pull/23
