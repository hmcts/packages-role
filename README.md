packages
=========

Used for deploying applications from an rpm

Example Playbook
----------------

install.yml
```yaml
- hosts: all
  tasks:
    - name: Include environment specific vars
      include_vars: "vars.yml"

- hosts: all
  become: yes
  roles:
    - devops.packages
```

vars.yml:
```yaml
myproject_username: "myproject"
myproject_password: "password"

packages:
  - project: "myproject"
    version: "{{ versions.myapp }}"
    name: "frontend"
    rpm_location: "/vagrant/node-rpm-packaging/myproject-frontend-*.rpm"
    env_file_template: "prototype.env.j2"
```

prototype.env.j2:
```bash
PORT="3005"
USERNAME="{{ myproject_username }}"
PASSWORD="{{ myproject_password }}"
```

Environment Variables
---------------------

A number of environment variables are made available to the application giving information
about the build.

Environment variable | Description
-------------------- | -----------
`PACKAGES_ENVIRONMENT` | The environment that the app is running in
`PACKAGES_PROJECT` | The project or team name of the app
`PACKAGES_NAME` | The app name in the packages role
`PACKAGES_VERSION` | The package version that this came from


License
-------

MIT

Author Information
------------------

HMCTS Reform Programme
