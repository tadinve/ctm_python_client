<!--
 
-->
# ctm_python_client

[BMC ctm_python_client] (or simply ctm_python_client) is a library to programmatically author and schedule workflows in Control-M.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use ctm_python_client to author workflows as directed acyclic graphs (DAGs) of tasks. The BMC Control-M scheduler executes your tasks on an array of agents while following the specified dependencies. Control-M's user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.



## Project Focus

Control-M simplifies application and data workflow orchestration on premises or as a service. It makes it easy to build, define, schedule, manage, and monitor production workflows, ensuring visibility, reliability, and improving SLAs.

ctm_python_client is a library to programmatically author and schedule these workflows in Control-M using Python.

Control-M is not a streaming solution, but it is often used to process real-time data, pulling data off streams in batches.

## Principles

- **Dynamic**:  Control-M pipelines are configuration as code (Python), allowing for dynamic pipeline generation. This allows for writing code that instantiates pipelines dynamically.
- **Extensible**:  Easily define your own job and jobtypes using Application Integrator and extend the library so that it fits the level of abstraction that suits your environment.
- **Elegant**:  ctm_python_client pipelines are lean and explicit. Parameterizing your scripts is built into the core of ctm_python_client using the powerful **Jinja** templating engine (Part of a future release).

## Requirements

Control-M's ctm_python_client is tested with:

|                      | Main version (dev)        | 
| -------------------- | ------------------------- | 
| Python               | 3.6, 3.7, 3.8, 3.9        | 
| Kubernetes           | 1.20, 1.19, 1.18          | 
| Docker               | 9.6, 10, 11, 12, 13       | 


## Getting started

Visit the official ctm_python_client website documentation (latest **stable** release) for help with
[installing ctm_python_client], [getting started], or walking through a more complete [tutorial]


## Installing from PyPI

We publish ctm_python_client as `ctm_python_client` package in PyPI. Installing it as simple at "pip install ctm_python_client"

> Note: Only `pip` installation is currently officially supported. While they are some successes with using other tools like [poetry](https://python-poetry.org) or
[pip-tools](https://pypi.org/project/pip-tools), they do not share the same workflow as
`pip` - especially when it comes to constraint vs. requirements management. Installing via `Poetry` or `pip-tools` is not currently supported.

If you wish to install ctm_python_client using those tools you should use the constraint files and convert
them to appropriate format and workflow that your tool requires.


```bash
pip install ctm_python_client
```


## Official source code

ctm_python_client is an Open Souce project and our official source code releases will be available through git-hub at https://github.com/controlm/ctm_python_client:

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## User Interface

ctm_python_client does not have any user interface of itself. Use Contorl-M scheduler and Monitor Web interface or the desktop version to interact with Control-M. ctm_python_client is used for designing, and submitting workflows to Control-M. Once submitted by ctm_python_client, head over to Control-M to review the workflow, order it for exection and monitor the execution and its logs.





## Support for Python and Kubernetes versions

As of ctm_python_client 0.1.0 we agreed to certain rules we follow for Python and Kubernetes support.
They are based on the official release schedule of Python and Kubernetes, nicely summarized in the
[Python Developer's Guide](https://devguide.python.org/#status-of-python-branches) and
[Kubernetes version skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).

1. We drop support for Python and Kubernetes versions when they reach EOL. We drop support for those
   EOL versions in main right after EOL date, and it is effectively removed when we release the
   first new MINOR (Or MAJOR if there is no new MINOR version) of ctm_python_client
   For example for Python 3.6 it means that we drop support in main right after 23.12.2021, and the first
   MAJOR or MINOR version of ctm_python_client released after will not have it.

2. The "oldest" supported version of Python/Kubernetes is the default one. "Default" is only meaningful
   in terms of "smoke tests" in CI PRs which are run using this default version and default reference
   image available in DockerHub. Currently ``Control-M/ctm_python_client:latest`` and ``Control-M/ctm_python_client:2.1.1`` images
   are both Python 3.6 images, however the first MINOR/MAJOR release of ctm_python_client release after 23.12.2021 will
   become Python 3.7 images.

3. We support a new version of Python/Kubernetes in main after they are officially released, as soon as we
   make them work in our CI pipeline (which might not be immediate due to dependencies catching up with
   new versions of Python mostly) we release a new images/support in ctm_python_client based on the working CI setup.

### Additional notes on Python version requirements

* Previous version [requires](https://github.com/Control-M/ctm_python_client/issues/8162) at least Python 3.5.3
  when using Python 3

## Contributing

Want to help build ctm_python_client? Check out our [contributing documentation](https://github.com/Control-M/ctm_python_client/CONTRIBUTING.rst).

## Who uses ctm_python_client?

More than 150 organizations are using ctm_python_client

## Who Maintains Control-M ctm_python_client?

ctm_python_client is the work of the Control-M user community. BMC ctm_python_client Review Commitee are respnsible for maintaining and administering this library. They are are responsible for reviewing and merging PRs as well as steering conversation around new feature requests.
If you would like to become a maintainer, please contact the BMC team.
## Links

- [Documentation](Link here)

## Sponsors

BMC is the main sponsor for ctm_python_client library.
