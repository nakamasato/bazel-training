load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "6b65cb7917b4d1709f9410ffe00ecf3e160edf674b78c54a894471320862184f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "727f3e4edd96ea20c29e8c2ca9e8d2af724d8c7778e7923a854b2c80952bc405",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.30.0/bazel-gazelle-v0.30.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.30.0/bazel-gazelle-v0.30.0.tar.gz",
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
    sha256 = "930c2c3b5ecc6c9c12615cf5ad93f1cd6e12d0aba862b572e076259970ac3a53",
    strip_prefix = "protobuf-3.21.12",
    urls = [
        "https://mirror.bazel.build/github.com/protocolbuffers/protobuf/archive/v3.21.12.tar.gz",
        "https://github.com/protocolbuffers/protobuf/archive/v3.21.12.tar.gz",
    ],
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "a644da969b6824cc87f8fe7b18101a8a6c57da5db39caa6566ec6109f37d2141",
    strip_prefix = "rules_python-0.20.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.20.0.tar.gz",
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
    sha256 = "9717ffc52120861136e478155c2ff3a9c21740e2244de52fa966f376d7471adf",
    strip_prefix = "grpc-1.53.0",
    urls = [
        "https://github.com/grpc/grpc/archive/refs/tags/v1.53.0.tar.gz",
    ],
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()
