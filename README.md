# bazel training

## Prerequisite

[bazel installed](https://docs.bazel.build/versions/main/install-os-x.html#install-on-mac-os-x-homebrew)

```
bazel --version
bazel 5.1.1-homebrew
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

1. [Build Go with Bazel & Gazelle](docs/01-build-go-with-bazel-and-gazelle.md) ([v0.1.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.1.0))
1. [Build Protobuf with Bazel](docs/02-build-protobuf-with-bazel.md) ([v0.2.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.2.0))

## Cheatsheet

1. `bazel run //:gazelle`: Generate build file.
1. `bazel run //:gazelle -- update-repos -from_file=go.mod`: Update `go_repository` in `WORKSPACE` from `go.mod`.
1. `bazel build //cmd`: Build a package `cmd`.
1. `bazel run //cmd`: Run a package `cmd`.
1. `bazel clean`: clean up the cache.

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
