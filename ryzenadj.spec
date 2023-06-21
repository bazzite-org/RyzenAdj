Name:           ryzenadj
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Power management settings for Ryzen APU
License:        LGPL
URL:            https://github.com/KyleGospo/RyzenAdj

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  pciutils-devel
BuildRequires:  cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++

%global debug_package %{nil}

%description
Adjust power management settings for Ryzen Mobile Processors.

%package devel
Summary:	Power management settings for Ryzen APU
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains necessary header files for RyzenAdj Development.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
install -Dsm 755 %{_builddir}/RyzenAdj/%__cmake_builddir/ryzenadj %{buildroot}/%{_sbindir}/ryzenadj
install -Dsm 744 %{_builddir}/RyzenAdj/%__cmake_builddir/libryzenadj.so %{buildroot}/%{_libdir}/libryzenadj.so
install -Dm 744 %{_builddir}/RyzenAdj/lib/ryzenadj.h %{buildroot}/%{_includedir}/ryzenadj.h

%files
%{_sbindir}/ryzenadj
%{_libdir}/libryzenadj.so

%files devel
%{_includedir}/ryzenadj.h

%changelog
{{{ git_dir_changelog }}}
