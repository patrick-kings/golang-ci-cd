Name:           gorpm
Version:        1.0
Release:        1%{?dist}
Summary:        golang rpm

License:        GPLv3
        
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
   

%description
golang rpm

%prep
%autosetup


%build
go build -v -o %{name}

%configure
%make_build


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 config.json %{buildroot}%{_sysconfdir}/%{name}/config.json
install -Dpm 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%dir %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}/config.json
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon Oct 25 2021 kings <patrick_kings@live.com>
- First release%changelog
