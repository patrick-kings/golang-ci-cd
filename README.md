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
  rpmbuild -ba rpm/gorpm.spec
  ```

- install

  ```!/bin/bash
  sudo dnf install ./dist/RPMS/x86_64/gorpm-1.0-1.fc34.x86_64.rpm
  sudo systemctl start gorpm
  curl -L http://localhost:8081
  ```

## MSI

using [go-msi](https://mh-cbon.github.io/go-msi/) package

- install **go-msi** and **wix**

```!/bin/bash
choco install go-msi

choco install wixtoolset
```

- add wix to your PATH variable

- create a **wix.json** file like [this one](https://github.com/patrick-kings/golang-ci-cd/blob/main/wix.json)

- Apply guids to the **wix.json** file with <code>go-msi set-guid</code>
- add a wix templates folder like [this one](https://github.com/patrick-kings/golang-ci-cd/blob/main/wix-templates)
- build your code <code> go build -o dist/build/gomsi.exe ./src/</code>
- finally run <code>go-msi make --msi dist/msi/gomsi.msi --version 1.0.0 -s ./wix-templates/ </code>
