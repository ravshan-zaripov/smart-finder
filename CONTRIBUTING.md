# Contributing

## Specific build instructions

SmartFinder uses the [meson](http://mesonbuild.com/) build system. Use the following commands to build SmartFinder from the source directory:

```sh
$ meson setup builddir --reconfigure
$ cd builddir
$ ninja
```

Then you can either run in the build dir by running:

```sh
$ ./local-project
```

You can also install SmartFinder system-wide by running:

```sh
$ ninja install
```

## VS Code Setup

If you're using Visual Studio Code, you may want to install the following Python dependencies in a virtual environment:

```sh
$ pip install pygobject
$ pip install pycairo
```

Optional, but recommended for better autocompletion and static analysis:

```sh
$ pip install pygobject-stubs
```