#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.4
%define		qtver		5.15.2
%define		kfname		kservice

Summary:	Plugin framework for desktop services
Name:		kf6-%{kfname}
Version:	6.4.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	3590cca35784654f8b80c18ca13cbe8a
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	bison >= 3.0
BuildRequires:	cmake >= 3.16
BuildRequires:	flex
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-kdbusaddons-devel >= %{version}
BuildRequires:	kf6-kdoctools-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
Requires:	kf6-dirs
Requires:	kf6-kconfig >= %{version}
Requires:	kf6-kcoreaddons >= %{version}
Requires:	kf6-kdbusaddons >= %{version}
Requires:	kf6-ki18n >= %{version}
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KService provides a plugin framework for handling desktop services.
Services can be applications or libraries. They can be bound to MIME
types or handled by application specific code.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.16
Requires:	kf6-kconfig-devel >= %{version}
Requires:	kf6-kcoreaddons-devel >= %{version}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF6Service.so.6
%attr(755,root,root) %{_libdir}/libKF6Service.so.*.*
%{_datadir}/qlogging-categories6/kservice.categories
%{_datadir}/qlogging-categories6/kservice.renamecategories
%attr(755,root,root) %{_bindir}/kbuildsycoca6
%{_mandir}/ca/man8/kbuildsycoca6.8*
%{_mandir}/es/man8/kbuildsycoca6.8*
%{_mandir}/fr/man8/kbuildsycoca6.8*
%{_mandir}/it/man8/kbuildsycoca6.8*
%{_mandir}/man8/kbuildsycoca6.8*
%{_mandir}/nl/man8/kbuildsycoca6.8*
%{_mandir}/pt_BR/man8/kbuildsycoca6.8*
%{_mandir}/tr/man8/kbuildsycoca6.8*
%{_mandir}/uk/man8/kbuildsycoca6.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KService
%{_libdir}/cmake/KF6Service
%{_libdir}/libKF6Service.so
