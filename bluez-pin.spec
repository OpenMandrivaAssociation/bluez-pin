%define _disable_rebuild_configure 1

Summary:	Bluetooth PIN GUI
Name:		bluez-pin
Version:	0.30
Release:	25
License:	GPLv2+
Group:		Communications
Source0: 	ftp://gpe.handhelds.org/projects/gpe/source/%{name}-%{version}.tar.bz2
Url:		https://www.bluez.org/

BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	perl-XML-Parser

%description
A GTK+ helper app for entering a Bluetooth PIN.

%prep
%setup -q

%build
%configure2_5x
make

%install
%makeinstall_std

%post
update-alternatives --install /bin/bluepin bluepin /usr/bin/bluez-pin 10

%postun
[ $1 != 0 ] && exit 0
update-alternatives --remove bluepin /usr/bin/bluez-pin

%files
%doc ChangeLog 
%{_bindir}/%{name}
%config %{_sysconfdir}/dbus*/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.30-12mdv2011.0
+ Revision: 663327
- mass rebuild
