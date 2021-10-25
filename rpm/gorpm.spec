
Name:           gorpm
Version:        1.0
Release:        1%{?dist}
Summary:        golang rpm

License:        MIT
        
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros

%define _topdir dist

   

%description
golang rpm

%global debug_package %{nil}

%prep
rm -drf %{_topdir}/BUILD/
cd ../../
cp -rf go.mod src/ rpm/  %{_topdir}/BUILD


%build
go build -v -o %{name} ./src


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 rpm/config.json %{buildroot}%{_sysconfdir}/%{name}/config.json
install -Dpm 644 rpm/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%check
# go test should be here... :)

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%dir %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}/config.json



%changelog
* Mon Oct 25 2021 kings <patrick_kings@live.com>
- First release%changelog
