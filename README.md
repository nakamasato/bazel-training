# bazel training

## Prerequisite

[bazel installed](https://docs.bazel.build/versions/main/install-os-x.html#install-on-mac-os-x-homebrew)

```
bazel --version
bazel 5.1.1-homebrew
```

## Go

### 1. [Build Go with Bazel & Gazelle](https://christina04.hatenablog.com/entry/using-bazel-to-build-go)

To build Go with Bazel, we use [gazelle](https://github.com/bazelbuild/bazel-gazelle) as **a build file generator** for a Bazel project.

1. Prepare codes
    1. init mod: `go mod init github.com/nakamasato/bazel-training`
    1. `cmd/main.go`
        ```go
        package main

        import (
            "github.com/nakamasato/bazel-training/uuid"
            "log"
        )

        func main() {
            id, err := uuid.Generate()
            if err != nil {
                log.Fatal(err)
            }
            log.Println(id)
        }
        ```
    1. `uuid/uuid.go`
        ```go
        package uuid

        import (
            "github.com/google/uuid"
        )

        func Generate() (string, error) {
            u, err := uuid.NewUUID()
            if err != nil {
                return "", err
            }
            return u.String(), nil
        }
        ```
    1. `go mod tidy`
1. Create `WORKSPACE` <- Just copy from [running-gazelle-with-bazel](https://github.com/bazelbuild/bazel-gazelle#running-gazelle-with-bazel).

1. Create `BUILD.bazel`.

    ```
    load("@bazel_gazelle//:def.bzl", "gazelle")

    # gazelle:prefix github.com/nakamasato/bazel-training
    gazelle(name = "gazelle")
    ```

    The important point is `# gazelle:prefix github.com/nakamasato/bazel-training`. This prefix is used for the generated `BUILD.bazel`

1. Generate build file with `gazelle`.

    ```
    bazel run //:gazelle
    ```

    <details><summary>Error</summary>

    ```
    INFO: Analyzed target //:gazelle (1 packages loaded, 2 targets configured).
    INFO: Found 1 target...
    ERROR: /private/var/tmp/_bazel_m.naka/687932582dc396e76af9f4754f6b0686/external/org_golang_x_mod/module/BUILD.bazel:3:11: GoCompilePkg external/org_golang_x_mod/module/module.a [for host] failed: (Exit 1): builder failed: error executing command bazel-out/host/bin/external/go_sdk/builder compilepkg -sdk external/go_sdk -installsuffix darwin_arm64 -src external/org_golang_x_mod/module/module.go -src external/org_golang_x_mod/module/pseudo.go ... (remaining 18 arguments skipped)

    Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
    compilepkg: missing strict dependencies:
            /private/var/tmp/_bazel_m.naka/687932582dc396e76af9f4754f6b0686/sandbox/darwin-sandbox/20/execroot/__main__/external/org_golang_x_mod/module/module.go: import of "golang.org/x/xerrors"
    No dependencies were provided.
    Check that imports in Go sources match importpath attributes in deps.
    Target //:gazelle failed to build
    Use --verbose_failures to see the command lines of failed build steps.
    INFO: Elapsed time: 0.339s, Critical Path: 0.14s
    INFO: 9 processes: 9 internal.
    FAILED: Build did NOT complete successfully
    FAILED: Build did NOT complete successfully
    ```

    Solution: add the following to the `WORKSPACE` from ([bazelbuild/bazel-gazelle#1217#issuecomment-1121223764](https://github.com/bazelbuild/bazel-gazelle/issues/1217#issuecomment-1121223764)):

    ```
    go_repository(
        name = "org_golang_x_mod",
        importpath = "golang.org/x/mod",
        sum = "h1:kQgndtyPBW/JIYERgdxfwMYh3AVStj88WQTlNDi2a+o=",
        version = "v0.6.0-dev.0.20220106191415-9b9b3d81d5e3",
        build_external = "external",
    )
    ```

    </details>

    Check files:

    - `cmd/BUILD.bazel`
        - `go_library`: function to build a package.
            - `deps = ["//uuid"]` <- as we specified `gazelle:prefix`
        - `go_binary`: function to generate a binary.
    - `uuid/BUILD.bazel`
        - `go_library`
            - `deps` has an external dependency.

1. Generate dependency in `WORKSPACE` from `go.mod` with `gazelle`, which is required by `bazel`.

    ```
    bazel run //:gazelle -- update-repos -from_file=go.mod
    ```

    Check `WORKSPACE`: `go_repository` is added.

    ```
    go_repository(
        name = "com_github_google_uuid",
        importpath = "github.com/google/uuid",
        sum = "h1:t6JiXgmwXMjEs8VusXIJk2BXHsn+wx8BZdTaoZ5fu7I=",
        version = "v1.3.0",
    )
    ```

1. Define a `gazelle-update-repos` command (Optional)

    Add the following lines to `BUILD.bazel`:

    ```
    gazelle(
        name = "gazelle-update-repos",
        args = [
            "-from_file=go.mod",
            "-to_macro=deps.bzl%go_dependencies",
            "-prune",
        ],
        command = "update-repos",
    )
    ```

    Run the new command:

    ```
    bazel run //:gazelle-update-repos # same as bazel run //:gazelle update-repos -from_file=go.mod -to_macro=deps.bzl%go_dependencies -prune
    ```

    This command will update `WORKSPACE`:

    ```
    load("//:deps.bzl", "go_dependencies")

    # gazelle:repository_macro deps.bzl%go_dependencies
    go_dependencies()
    ```

    `deps.bzl` is created:

    ```python
    def go_dependencies():
        pass
    ```


1. Build `cmd`.

    ```
    bazel build //cmd
    ```

1. Run `cmd`.

    ```
    bazel run //cmd
    ```

    Result:
    ```
    INFO: Analyzed target //cmd:cmd (0 packages loaded, 0 targets     configured).
    INFO: Found 1 target...
    Target //cmd:cmd up-to-date:
      bazel-bin/cmd/cmd_/cmd
    INFO: Elapsed time: 0.274s, Critical Path: 0.00s
    INFO: 1 process: 1 internal.
    INFO: Build completed successfully, 1 total action
    INFO: Build completed successfully, 1 total action
    2022/06/21 18:17:36 fdc3fc88-f142-11ec-b4be-467a6a605f22
    ```

Notes:

1. Symlink.
    - bazel-bazel-training
    - bazel-bin
    - bazel-out
    - bazel-testlogs

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

1. [Running Gazelle with Go](https://github.com/bazelbuild/bazel-gazelle#running-gazelle-with-go)

(skip)

[v0.1.0](https://github.com/nakamasato/bazel-training/releases/tag/v0.1.0)

## Build Protobuf

1. Prepare proto files.

    <details><summary>proto/address.proto</summary>

    ```proto
    syntax = "proto3";

    option go_package = "github.com/nakamasato/bazel-training/proto;user";

    package user;

    import "proto/zipcode.proto";

    message Address {
      string  city     = 1;
      ZipCode zip_code = 2;
    }
    ```

    </details>

    <details><summary>proto/user.proto</summary>

    ```proto
    syntax = "proto3";

    option go_package = "github.com/nakamasato/bazel-training/proto;user";

    package user;

    import "proto/address.proto";
    import "google/protobuf/any.proto";

    message User {
      string              id      = 1;
      string              name    = 2;
      Address             address = 3;
      google.protobuf.Any tags    = 4;
    }
    ```

    </details>

    <details><summary>proto/zipcode.proto</summary>

    ```proto
    syntax = "proto3";

    option go_package = "github.com/nakamasato/bazel-training/proto;user";

    package user;

    message ZipCode {
      string code = 1;
    }
    ```

    </details>

1. Add the following lines to `WORKSPACE`.
    ```
    http_archive(
        name = "com_google_protobuf",
        sha256 = "d0f5f605d0d656007ce6c8b5a82df3037e1d8fe8b121ed42e536f569dec16113",
        strip_prefix = "protobuf-3.14.0",
        urls = [
            "https://mirror.bazel.build/github.com/protocolbuffers/protobuf/archive/v3.14.0.tar.gz",
            "https://github.com/protocolbuffers/protobuf/archive/v3.14.0.tar.gz",
        ],
    )

    load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
    protobuf_deps()
    ```

1. Run gazelle.
    ```
    bazel run //:gazelle
    ```

    -> `proto/BUILD.bazel` will be created.

1. Build proto.

    ```
    bazel build //proto
    ```

    -> `xx.pb.go` will be generated under `bazel-bin/proto/user_go_proto_/github.com/nakamasato/bazel-training/proto/`:

    ```bash
    ls bazel-bin/proto/user_go_proto_/github.com/nakamasato/bazel-training/proto/
    address.pb.go user.pb.go    zipcode.pb.go
    ```

1. The results are same as `protoc --go_out`

    Install if not installed:
    ```
    brew install protobuf
    ```

    Check version:
    ```
    protoc --version
    libprotoc 3.19.4
    ```

    ```
    protoc --go_out=paths=source_relative:. proto/address.proto proto/user.proto proto/zipcode.proto
    ```

    This will generate:
    - address.pb.go
    - user.pb.go
    - zipcode.pb.go


## Cheatsheet

1. `bazel run //:gazelle`: Generate build file.
1. `bazel run //:gazelle -- update-repos -from_file=go.mod`: Update `go_repository` in `WORKSPACE` from `go.mod`.
1. `bazel build //cmd`: Build a package `cmd`.
1. `bazel run //cmd`: Run the package `cmd`.
1. `bazel clean`: clean up the cache.
