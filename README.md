# Bazel Training

## Prerequisite

[bazel installed](https://docs.bazel.build/versions/main/install-os-x.html#install-on-mac-os-x-homebrew)

```
bazel --version
bazel 6.0.0
```
## Basics

1. [`bazel` concept and terminology](https://docs.bazel.build/versions/main/build-ref.html#intro)

    1. `Workspace`: a directory on your filesystem that contains the source files for the software you want to build. Each workspace directory has a text file named `WORKSPACE`.
    1. `Repository`: The directory containing the `WORKSPACE` file is the root of the main repository, also called `@`.
    1. `Package`: The primary unit of code organization in a repository. A package is defined as a directory containing a file named `BUILD` or `BUILD.bazel`.
    1. `Target`: A package is a container. The elements of a package are called *targets*.
    1. `Labels`:
        - `@myrepo//my/app/main:app_binary` = `//my/app/main:app_binary` inside `@myrepo`
        - `my/app/main`: un-qualified package name
        - `@myrepo//my/app/main`: full-qualified package name
        - `app_binary` or `:app_binary` inside `@myrepo//my/app/main`
1. Repository rules (`WORKSPACE`):
    1. Git `git_repository`
    1. Http `http_archive`
    1. util `maybe`

## Contents

1. [Build Go with Gazelle](docs/01-build-go-with-gazelle.md) ([v0.1.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.1.0))
1. [Build Protobuf](docs/02-build-protobuf.md) ([v0.2.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.2.0))
1. [Build Python](docs/03-build-python.md) ([v0.3.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.3.0))
1. [Build Java](docs/04-build-java.md) ([v0.4.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.4.0))
1. [Build Python with Poetry](docs/05-build-python-with-poetry.md) ([v0.5.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.5.0))

## Cheatsheet

1. Bazel
    1. `bazel clean`: clean up the cache.
1. Java:
    1. build: `bazel build //java:App`
    1. run: `bazel run //java:App`
    1. check dep: `bazel query  --notool_deps --noimplicit_deps "deps(//java:App)" --output graph`
1. Python: `bazel run //python:main`
1. Go:
    1. build: `bazel build //cmd`: Build a package `cmd`.
    1. run: `bazel run //cmd`: Run a package `cmd`.
    1. `bazel run //:gazelle`: Generate build file.
    1. `bazel run //:gazelle -- update-repos -from_file=go.mod`: Update `go_repository` in `WORKSPACE` from `go.mod`.
## FAQ
1. How to upgrade `http_archive` version?

## References
- https://www.youtube.com/watch?v=8P3m1-U7v0k
- https://christina04.hatenablog.com/entry/using-bazel-to-build-go
- https://christina04.hatenablog.com/entry/using-bazel-to-build-protobuf
- https://christina04.hatenablog.com/entry/using-bazel-to-build-docker-image
- https://christina04.hatenablog.com/entry/using-bazel-to-build-grpc
- https://christina04.hatenablog.com/entry/bazel-remote-cache
- https://christina04.hatenablog.com/entry/test-with-bazel
- https://christina04.hatenablog.com/entry/bazel-tips
- https://note.crohaco.net/2020/bazel-golang/
- https://github.com/bazelbuild/bazel/issues/10134
- https://github.com/bazelbuild/bazel/issues/15673
