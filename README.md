# updateinfo-on-update

This small plugin provides functionality similar to that of an old YUM plugin
which displayed information about available updates when `yum update` was run.
It does so by invoking `dnf updateinfo info updates` (which displays the same
information yum was using) when `dnf update` is run.

## Installation

Copy the python file to wherever the DNF installation stores its plugins. This
is determined by the `pluginpath` configuration option.

The plugin should run on both python 2.7 and any version of python 3.
