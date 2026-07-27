Summary:  Simple and lightweight desktop-agnostic Qt file archiver for LXQT desktop.
Name: lxqt-archiver
Version: 1.4.0
Release: 2
License: GPLv2
Group: Graphical desktop/Other
Url: https://github.com/lxqt/lxqt-archiver
Source0: https://github.com/lxqt/lxqt-archiver/releases/download/%{version}/lxqt-archiver-%{version}.tar.xz
BuildSystem: cmake
BuildOption: -DUSE_7Z=ON
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: 7zip
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(libfm-qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
Requires: 7zip

%description
This is only a front-end (a graphical interface) to archiving programs
like tar and zip.

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
