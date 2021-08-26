<!--
 
-->
# ctm_python_client

[BMC Control-M ctm_python_client] (or simply ctm_python_client) is a library to programmatically author and schedule workflows in Control-M.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use ctm_python_client to author workflows as directed acyclic graphs (DAGs) of tasks. The BMC Control-M scheduler executes your tasks on an array of agents while following the specified dependencies. Control-M's user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.


**Table of contents**

  - [Project Focus](#project-focus)
  - [Principles](#principles)
  - [Requirements](#requirements)
  - [Getting started](#getting-started)
  - [Installing from PyPI](#installing-from-pypi)
  - [Official source code](#official-source-code)
  - [Convenience packages](#convenience-packages)
  - [User Interface](#user-interface)
  - [Semantic versioning](#semantic-versioning)
  - [Version Life Cycle](#version-life-cycle)
  - [Support for Python and Kubernetes versions](#support-for-python-and-kubernetes-versions)
    - [Additional notes on Python version requirements](#additional-notes-on-python-version-requirements)
  - [Contributing](#contributing)
  - [Who uses Control-M ctm_python_client?](#who-uses-Control-M-ctm_python_client)
  - [Who Maintains Control-M ctm_python_client?](#who-maintains-Control-M-ctm_python_client)
  - [Can I use the Control-M ctm_python_client logo in my presentation?](#can-i-use-the-Control-M-ctm_python_client-logo-in-my-presentation)
  - [ctm_python_client merchandise](#ctm_python_client-merchandise)
  - [Links](#links)
  - [Sponsors](#sponsors)


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

We publish Control-M ctm_python_client as `Control-M-ctm_python_client` package in PyPI. Installing it as simple at "pip install Control-M-ctm_python_client"

> Note: Only `pip` installation is currently officially supported. While they are some successes with using other tools like [poetry](https://python-poetry.org) or
[pip-tools](https://pypi.org/project/pip-tools), they do not share the same workflow as
`pip` - especially when it comes to constraint vs. requirements management. Installing via `Poetry` or `pip-tools` is not currently supported.

If you wish to install ctm_python_client using those tools you should use the constraint files and convert
them to appropriate format and workflow that your tool requires.


```bash
pip install Control-M-ctm_python_client
```


## Official source code

Control-M ctm_python_client is an [Open Software Foundation](https://www.apache.org) (ASF) project,
and our official source code releases:

- Follow the [ASF Release Policy](https://www.Control-M.org/legal/release-policy.html)
- Can be downloaded from [the ASF Distribution Directory](https://downloads.Control-M.org/ctm_python_client)
- Are cryptographically signed by the release manager
- Are officially voted on by the PMC members during the
 [Release Approval Process](https://www.Control-M.org/legal/release-policy.html#release-approval)

Following the ASF rules, the source packages released must be sufficient for a user to build and test the release provided they have access to the appropriate platform and tools.

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

Want to help build Control-M ctm_python_client? Check out our [contributing documentation](https://github.com/Control-M/ctm_python_client/blob/main/CONTRIBUTING.rst).

Official Docker (container) images for Control-M ctm_python_client are described in [IMAGES.rst](https://github.com/Control-M/ctm_python_client/blob/main/IMAGES.rst).

## Who uses Control-M ctm_python_client?

More than 150 organizations are using Control-M ctm_python_client
[in the wild](https://github.com/Control-M/ctm_python_client/blob/main/INTHEWILD.md).

## Who Maintains Control-M ctm_python_client?

ctm_python_client is the work of the Control-M user community. BMC ctm_python_client Review Commitee are respnsible for maintaining and administering this library. They are are responsible for reviewing and merging PRs as well as steering conversation around new feature requests.
If you would like to become a maintainer, please review the Control-M ctm_python_client
[committer requirements](https://github.com/Control-M/ctm_python_client/blob/main/COMMITTERS.rst#guidelines-to-become-an-ctm_python_client-committer).

## Links

- [Documentation](https://ctm_python_client.Control-M.org/docs/Control-M-ctm_python_client/stable/)
- [Chat](https://s.Control-M.org/ctm_python_client-slack)

## Sponsors

BMC is the main sponsor for ctm_python_client library.
