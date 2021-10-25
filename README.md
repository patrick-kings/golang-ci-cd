# golang-ci-cd

## RPM

- install rpm dev tools

  > sudo dnf groupinstall "RPM Development Tools"

- Generate a spec file
  > rpmdev-newspec gorpm.spec
- Build the RPM
  > rpmbuild -ba gorpm.spec
- install

  ```!/bin/bash
    sudo dnf install ./dist/RPMS/x86_64/gorpm-1.0-1.fc34.x86_64.rpm
    sudo systemctl start gorpm
    curl -L http://localhost:8081
  ```
