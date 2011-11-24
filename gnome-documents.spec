Name:           gnome-documents
Version:        0.3.2
Release:        1%{?dist}
Summary:        A document manager application for GNOME

License:        GPLv2+
URL:            https://live.gnome.org/Design/Apps/Documents
Source0:        http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/0.3/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  libgdata-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  liboauth-devel
BuildRequires:  evince-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  tracker-devel
BuildRequires:  desktop-file-utils
BuildRequires:  clutter-gtk-devel

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

%build
%configure --disable-static
#FIXME: Build fails with  %{?_smp_mflags}.
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :


%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc README AUTHORS NEWS TODO COPYING
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/dbus-1/services/*
%{_libdir}/girepository-1.0
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/gnome-documents.png

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0

%changelog
* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Tue Oct 18 2011 Elad Alfassa <elad@fedoraproject.org> - 0.2.1-1
- New upstream release

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.1.92-2
- Rebuild against newer clutter

* Tue Sep 20 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.92-1
- Update to 0.1.92

* Wed Sep  7 2011 Matthias Clasen <mclasen@redhat.com> - 0.1.91-1
- Update to 0.1.91

* Sat Sep 03 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-2
- Fix #735341

* Fri Sep 02 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-1
- Initial packaging.

