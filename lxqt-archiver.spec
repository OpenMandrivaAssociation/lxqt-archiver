Summary:  Simple and lightweight desktop-agnostic Qt file archiver for LXQT desktop.
Name: lxqt-archiver
Version: 1.2.0
Release: 1
License: GPLv2
Group: Graphical desktop/Other
Url: https://github.com/lxqt/lxqt-archiver
Source0: https://github.com/lxqt/lxqt-archiver/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: ninja
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
like tar and zip. The supported file types are:

  * 7-Zip Compressed File (.7z)
  * WinAce Compressed File (.ace)
  * ALZip Compressed File (.alz)
  * AIX Small Indexed Archive  (.ar)
  * ARJ Compressed Archive (.arj)
  * Cabinet File (.cab)
  * UNIX CPIO Archive (.cpio)
  * Debian Linux Package (.deb) [Read-only mode]
  * ISO-9660 CD Disc Image (.iso) [Read-only mode]
  * Java Archive (.jar)
  * Java Enterprise archive (.ear)
  * Java Web Archive (.war)
  * LHA Archive (.lzh, .lha)
  * WinRAR Compressed Archive (.rar)
  * RAR Archived Comic Book (.cbr)
  * RPM Linux Package (.rpm) [Read-only mode]
  * Tape Archive File:
    + uncompressed (.tar) or compressed with:
      o gzip (.tar.gz , .tgz)
      o bzip (.tar.bz , .tbz)
      o bzip2 (.tar.bz2 , .tbz2)
      o compress (.tar.Z , .taz)
      o lrzip (.tar.lrz , .tlrz)
      o lzip (.tar.lz , .tlz)
      o lzop (.tar.lzo , .tzo)
      o 7zip (.tar.7z)
      o xz (.tar.xz)
  * Stuffit Archives (.bin, .sit)
  * ZIP Archive (.zip)
  * ZIP Archived Comic Book (.cbz)
  * ZOO Compressed Archive File (.zoo)
  * Single files compressed with gzip, bzip, bzip2, compress, lrzip, lzip,
    lzop, rzip, xz.

%prep
%autosetup -p1
%cmake \
       -DUSE_7Z=ON \
       -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
