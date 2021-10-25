# golang-ci-cd

## RPM

- install rpm dev tools

  ```!/bin/bash
  sudo dnf groupinstall "RPM Development Tools"
  ```

- Generate a spec file

  ```!/bin/bash
  rpmdev-newspec gorpm.spec
  ```

- Build the RPM

  ```!/bin/bash
  rpmbuild -ba gorpm.spec
  ```

- install

  ```!/bin/bash
  sudo dnf install ./dist/RPMS/x86_64/gorpm-1.0-1.fc34.x86_64.rpm
  sudo systemctl start gorpm
  curl -L http://localhost:8081
  ```
