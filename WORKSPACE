load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "6b65cb7917b4d1709f9410ffe00ecf3e160edf674b78c54a894471320862184f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.50.1/rules_go-v0.39.0.zip",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "a80893292ae1d78eaeedd50d1cab98f242a17e3d5741b1b9fb58b5fd9d2d57bc",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.40.0/bazel-gazelle-v0.40.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.40.0/bazel-gazelle-v0.40.0.tar.gz",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies", "go_repository")

############################################################
# Define your own dependencies here using go_repository.
# Else, dependencies declared by rules_go/gazelle will be used.
# The first declaration of an external repository "wins".
############################################################

go_repository(
    name = "com_github_google_uuid",
    importpath = "github.com/google/uuid",
    sum = "h1:t6JiXgmwXMjEs8VusXIJk2BXHsn+wx8BZdTaoZ5fu7I=",
    version = "v1.3.0",
)

load("//:deps.bzl", "go_dependencies")

# gazelle:repository_macro deps.bzl%go_dependencies
go_dependencies()

go_rules_dependencies()

go_register_toolchains(version = "1.18")

gazelle_dependencies()

# Protocol Buffers

http_archive(
    name = "com_google_protobuf",
    sha256 = "3cf7d5b17c4ff04fe9f038104e9d0cae6da09b8ce271c13e44f8ac69f51e4e0f",
    strip_prefix = "protobuf-25.5",
    urls = [
        "https://mirror.bazel.build/github.com/protocolbuffers/protobuf/archive/v25.5.tar.gz",
        "https://github.com/protocolbuffers/protobuf/archive/v25.5.tar.gz",
    ],
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "62ddebb766b4d6ddf1712f753dac5740bea072646f630eb9982caa09ad8a7687",
    strip_prefix = "rules_python-0.39.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.39.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_9",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.9",
)

load("@python3_9//:defs.bzl", "interpreter")

# Poetry rules for managing Python dependencies

http_archive(
    name = "com_sonia_rules_poetry",
    sha256 = "6dcb6ee86a9d507ef356097c5f2e16cb5e01c32021ff13cd28c0bb17bf5d8266",
    strip_prefix = "rules_poetry-d7a852ae69d22fe4670e34822cd376a69db0485e",
    urls = ["https://github.com/soniaai/rules_poetry/archive/d7a852ae69d22fe4670e34822cd376a69db0485e.tar.gz"],
)

load("@com_sonia_rules_poetry//rules_poetry:defs.bzl", "poetry_deps")

poetry_deps()

load("@com_sonia_rules_poetry//rules_poetry:poetry.bzl", "poetry")

poetry(
    name = "poetry",
    lockfile = "//:poetry.lock",
    pyproject = "//:pyproject.toml",
)

# gRPC
http_archive(
    name = "com_github_grpc_grpc",
    sha256 = "86f0f28b75b1562c82b7fc5d436b4f5f5da6cb8d67f59e9fec5f8aa1fe924037",
    strip_prefix = "grpc-1.68.0",
    urls = [
        "https://github.com/grpc/grpc/archive/refs/tags/v1.68.0.tar.gz",
    ],
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()
