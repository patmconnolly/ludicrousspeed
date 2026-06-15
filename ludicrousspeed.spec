Name: ludicrousspeed
Version: 0.1.2
Release: 1%{?dist}
Summary: Ludicrousspeed to conflict with OpenShift Lightspeed Command Line Assistant
License: MIT
URL: https://github.com/patmconnolly/ludicrousspeed
Source0: c
Conflicts: command-line-assistant
Requires: python3

%description
A command line assistant specifically to conflict with LightSpeed Command Line Assistant

%prep
%setup -c -T
%patchShebangs %{SOURCE0}

%install
install -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/c

%files
%{_bindir}/c

%changelog
* Fri May 29 2026 Developer Patrick - 0.1.2
- Documentation updates
- Specfile updates.
- Update source file to reflect standards in guide (shebang).
* Thu May 28 2026 Developer Patrick - 0.1.1
- Add better usage
- Enable yogurt to be used with no query
- Increment version
* Sun May 24 2026 Developer Patrick - 0.1.0
- Initial package