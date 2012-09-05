%define evince_version 3.3.92

Name:           gnome-documents
Version:        3.5.91
Release:        1%{?dist}
Summary:        A document manager application for GNOME

License:        GPLv2+
URL:            https://live.gnome.org/Design/Apps/Documents
Source0:        http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/3.5/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  libgdata-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  liboauth-devel
BuildRequires:  evince-devel >= %{evince_version}
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  tracker-devel
BuildRequires:  desktop-file-utils
BuildRequires:  clutter-gtk-devel
BuildRequires:  gjs-devel
BuildRequires:  libzapojit-devel

%description
gnome-documents is a document manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

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
%{_libexecdir}/*
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/gnome-documents.png
%{_libdir}/gnome-documents/
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/gnome-documents-search-provider.ini

%changelog
* Tue Sep 04 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-2
- Rebuild against new cogl/clutter

* Tue Aug 21 2012 Elad Alfassa <elad@fedoraproject.org> - 3.5.90-1
- Update to latest upstream release

* Fri Aug 10 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.5.5-1
- Update to 0.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 0.5.4-1
- Update to 0.5.4

* Wed Jun 27 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Thu Jun 07 2012 Matthias Clasen <mclasen@redhat.com> - 0.5.2.1-2
- Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 0.5.2.1-1
- Update to 0.5.2.1

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.4.0.1-1
- Update to 0.4.0.1

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.4.0-2
- Rebuild against current libevdocument3 soname

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.92-4
- Rebuild for libevdocument3 soname bump

* Tue Mar 20 2012 Adam Williamson <awilliam@redhat.com> - 0.3.92-3
- revert unoconv requirement, it pulls LO into the live image

* Tue Mar 20 2012 Adam Williamson <awilliam@redhat.com> - 0.3.92-2
- requires: unoconv (RHBZ #754516)

* Tue Mar 20 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.3.92-1
- Update to 0.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-2
- Rebuild against new cogl

* Tue Mar 06 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.90-1
- Update to 0.3.90

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.4-2
- Rebuild against new cogl

* Tue Jan 17 2012 Cosimo Cecchi <cosimoc@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.3.3-1
- Update to 0.3.3

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

