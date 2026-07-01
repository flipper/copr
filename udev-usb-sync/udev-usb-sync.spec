Name:           udev-usb-sync
Version:        1.1
Release:        1%{?dist}
Summary:        Disables write-cache for USB Storage Devices

License:        MIT
URL:            https://gitlab.manjaro.org/applications/udev-usb-sync
Source0:        https://gitlab.manjaro.org/applications/udev-usb-sync/-/archive/%{version}/udev-usb-sync-%{version}.tar.gz

BuildArch:      noarch

Requires:       bash hdparm bc
AutoReqProv:    no

%description
Disables write-cache for USB Storage Devices

%prep
%autosetup -n udev-usb-sync-%{version}

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_prefix}/lib/udev/rules.d

# Install executable
install -m 0755 %{name} \
    %{buildroot}%{_bindir}/%{name}

# Install default config
install -m 0644 %{name}.conf \
    %{buildroot}%{_sysconfdir}/%{name}.conf

# Install udev rule
install -m 0644 99-usb-sync.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/99-%{name}.rules


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/udev/rules.d/99-%{name}.rules