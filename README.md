# simple-github-announcements-client
This project is the official client of the [simple-github-announcements](https://github.com/A223D/simple-github-announcements) repository.

The idea is to create an extremely lightweight and modern client for RSS feeds and tightly integrated with the aforementioned system.

## Theory of Operation 🚧
Not confirmed yet, but the idea is to poll the raw GitHub link for each RSS/XML file (or topic in case of the official server system). The idea is to use GitHub's infrastructure as the server infrastructure. The client should be able to function on the following systems:
* Windows 10/11
* Linux (Ubuntu)
* macOS

It is preferred to use the native operating system SDKs to send notifications. Python was chosen as the langugae for development since it's cross platform.