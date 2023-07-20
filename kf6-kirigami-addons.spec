%define git 20230720

Name:		kf6-kirigami-addons
Version:	0.8.0
Release:	%{?git:0.%{git}.}1
Summary:	Add-on widgets for the Kirigami library
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2#/kirigami-addons-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz
%endif
Patch0:		kirigami-addons-qt-6.6.patch
License:	LGPLv2+
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)

%description
Add-on widgets for the Kirigami library.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description devel
This package contains header files needed if you wish to build
applications based on %{name}.

%prep
%autosetup -p1 -n kirigami-addons-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kirigami-addons

%files -f kirigami-addons.lang
%{_qtdir}/qml/org/kde/kirigamiaddons

%files devel
%{_libdir}/cmake/KF6KirigamiAddons
