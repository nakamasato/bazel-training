# Build protobuf with Bazel

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

