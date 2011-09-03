Name:           gnome-documents
Version:        0.1.90
Release:        2%{?dist}
Summary:        A document manager application for GNOME

License:        GPLv2+
URL:            https://live.gnome.org/Design/Apps/Documents
Source0:        http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/0.1/%{name}-%{version}.tar.xz
Patch0:         gnome-documents-0.1.90-fix_account_props.patch

BuildRequires:  intltool
BuildRequires:  libgdata-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  liboauth-devel
BuildRequires:  evince-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  tracker-devel
BuildRequires:  desktop-file-utils

%description
gnome-documents is a document manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
#FIXME: Build fails with  %{?_smp_mflags}.
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc README AUTHORS NEWS TODO
#FIXME: Upstream doesn't have a copy of the GPL in their tarball.
# https://bugzilla.gnome.org/show_bug.cgi?id=658042
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/dbus-1/services/*
%{_libdir}/girepository-1.0
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0

%changelog
* Sat Sep 03 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-2
- Fix #735341

* Fri Sep 02 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-1
- Initial packaging.

