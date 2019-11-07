# Changelog

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2-beta] - 2019-11-07

### Added

-   Added error handling.
    -   Failed DB writes will be cached until they are successfuly written.
    -   Failed API calls are retried after a time interval

## [1.0.1-beta] - 2019-10-31

### Fixed

-   Issue in Makefile with incorrect flag has been resolved.

-   Add SSL libraries to address an [issue](https://tiny.cc/4e0hfz) with
    https connections.

## [1.0.0-beta] - 2019-10-31

### Added

-   The ability to specify the endpoint URL to be used through an env
    variable.

-   A Makefile with basic build, test and push commands for Docker.

### Fixed

-   `.sample_env` MySQL configuration now points to `127.0.0.1` instead of
    `localhost`, as using `localhost` fails due to MySQL trying to create a
    Unix socket.
-   Added a missing dependency.

## [0.1.1-beta] - 2019-10-26

### Fixed

-   Re-added the ability to load `.env` files locally

-   Fixed the endpoint link parameters. TODO: Must review this
    choice of endpoint in the future.

## [0.1.0-beta] - 2019-10-26

### Added

-   First beta version of the project.

-   Added basic documentation, dependencies and working version of the server
    that keeps checking for new data.

-   Compatibility with MySQL and PostgreSQL as destinations to store data,
    along with relevant configuration files.

-   Dockerfile (beta) to containerise for easier deployment.
