%define name 	bluez-pin
%define version 0.30
%define release %mkrel 8

Summary: 	Bluetooth PIN GUI
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://www.bluez.org/
License: 	GPLv2+
Group: 		Communications
Source0: 	ftp://gpe.handhelds.org/projects/gpe/source/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	imagemagick gtk2-devel libglade2.0-devel libGConf2-devel
BuildRequires:	libbluez-devel
BuildRequires:  dbus-glib-devel >= 0.50
BuildRequires:	perl-XML-Parser

%description
A GTK+ helper app for entering a Bluetooth PIN.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%post
update-alternatives --install /bin/bluepin bluepin /usr/bin/bluez-pin 10

%postun
[ $1 != 0 ] && exit 0
update-alternatives --remove bluepin /usr/bin/bluez-pin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog 
%_bindir/%name
%config %_sysconfdir/dbus*/*
%_datadir/pixmaps/*
%_datadir/%name

