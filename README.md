# bazel training

## Prerequisite

[bazel installed](https://docs.bazel.build/versions/main/install-os-x.html#install-on-mac-os-x-homebrew)

```
bazel --version
bazel 5.1.1-homebrew
```

## Go

### 1. [Build Go with Bazel](https://christina04.hatenablog.com/entry/using-bazel-to-build-go)

1. Prepare codes
    1. init mod: `go mod init github.com/nakamasato/bazel-training`
    1. `cmd/main.go`
    1. `uuid/uuid.go`
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
1. Build `cmd`

    ```
    bazel build //cmd
    ```

1. Symlink.

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
