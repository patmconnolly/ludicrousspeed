Name: ludicrousspeed
Version: 0.1.0
Release: 1%{?dist}
Summary: LudicrousSpeed to conflict with LightSpeed Command Line Assistant

Conflicts: command-line-assistant

License: MIT

Requires: python3

Source0: c

%description
A command line assistant specifically to conflict with LightSpeed Command Line Assistant

%install
install -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/c

%files
%{_bindir}/c

%changelog
* Sun May 24 2026 Developer Patrick - 0.1.0
- Initial package