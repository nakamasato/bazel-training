# Java

## Project setup

```
gradle init
```

<details>

```
Starting a Gradle Daemon, 4 incompatible and 1 stopped Daemons could not be reused, use --status for details

Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Scala
  6: Swift
Enter selection (default: Java) [1..6] 3

Split functionality across multiple subprojects?:
  1: no - only one application project
  2: yes - application and library projects
Enter selection (default: no - only one application project) [1..2] no
Please enter a value between 1 and 2: 1

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2] 2

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]
Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit Jupiter) [1..4] 4

Project name (default: java): sample
Source package (default: sample):

> Task :init
Get more help with your project: https://docs.gradle.org/7.5.1/samples/sample_building_java_applications.html

BUILD SUCCESSFUL in 1m 34s
2 actionable tasks: 2 executed
```

</details>

## Run

```
./gradlew run

Hello World!

BUILD SUCCESSFUL in 666ms
2 actionable tasks: 1 executed, 1 up-to-date
```

## Test

```
./gradlew test
```

## Bazel

### Basic

1. Add `BUILD.bazel`
    ```
    java_binary(
        name = "App",
        srcs = glob(["app/src/main/java/sample/*.java"]),
    )
    ```
1. Build
    ```
    bazel build //java:App
    ```
1. Run
    ```
    bazel run //java:App
    ```
1. Deps
    ```
    bazel query  --notool_deps --noimplicit_deps "deps(//java:App)" --output graph
    digraph mygraph {
      node [shape=box];
      "//java:App"
      "//java:App" -> "//java:app/src/main/java/sample/App.java"
      "//java:app/src/main/java/sample/App.java"
    }
    ```

1. test (todo)

    https://bazel.build/reference/be/java#java_test

### (Optional) you can specify multiple build targets

 1. Add dependency.
 1. Update `BUILD` like the following:
    ```
    java_binary(
        name = "ProjectRunner",
        srcs = ["src/main/java/com/example/ProjectRunner.java"],
        main_class = "com.example.ProjectRunner",
        deps = [":greeter"],
    )

    java_library(
        name = "greeter",
        srcs = ["src/main/java/com/example/Greeting.java"],
    )
    ```

### More

1. https://github.com/bazelbuild/rules_jvm_external
