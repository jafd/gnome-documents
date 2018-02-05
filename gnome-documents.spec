%define evince_version 3.13.3
%define gettext_version 0.19.8
%define gjs_version 1.48.0
%define gtk3_version 3.22.15
%define tracker_version 0.17.0

Name:           gnome-documents
Version:        3.26.2
Release:        1%{?dist}
Summary:        A document manager application for GNOME

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Documents
Source0:        https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(evince-document-3.0) >= %{evince_version}
BuildRequires:  pkgconfig(evince-view-3.0) >= %{evince_version}
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:  pkgconfig(tracker-control-2.0) >= %{tracker_version}
BuildRequires:  pkgconfig(tracker-sparql-2.0) >= %{tracker_version}
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libgepub)
BuildRequires:  pkgconfig(zapojit-0.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  liboauth-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext >= %{gettext_version}
BuildRequires:  itstool
BuildRequires:  inkscape
BuildRequires:  poppler-utils
BuildRequires:  docbook-style-xsl

Requires:       evince-libs%{?_isa} >= %{evince_version}
Requires:       gettext%{?isa} >= %{gettext_version}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       gnome-online-miners
Requires:       libgepub%{?_isa}
Requires:       libreofficekit
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       tracker-miners

%description
gnome-documents is a document manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%package libs
Summary: Common libraries and data files for %{name}
%description libs
%{summary}.

%package -n gnome-books
Summary:        A e-books manager application for GNOME
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       evince-libs%{?_isa} >= %{evince_version}
Requires:       gettext%{?isa} >= %{gettext_version}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       gnome-epub-thumbnailer
Requires:       libgepub%{?_isa}

%description -n gnome-books
gnome-books is an e-books manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%prep
%setup -q

%build
%configure --disable-static --enable-getting-started
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/org.gnome.Documents.desktop
%find_lang %{name} --with-gnome

%ldconfig_scriptlets libs

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO
%{_bindir}/%{name}
%{_datadir}/appdata/org.gnome.Documents.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/applications/org.gnome.Documents.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Documents.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Documents-symbolic.svg
%{_mandir}/man1/gnome-documents.1*
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini

%files libs
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_libdir}/gnome-documents/

%files -n gnome-books
%license COPYING
%doc README AUTHORS NEWS TODO
%{_bindir}/gnome-books
%{_datadir}/dbus-1/services/org.gnome.Books.service
%{_datadir}/glib-2.0/schemas/org.gnome.books.gschema.xml
%{_datadir}/applications/org.gnome.Books.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Books.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Books-symbolic.svg
%{_mandir}/man1/gnome-books.1*
%{_datadir}/appdata/org.gnome.Books.appdata.xml

%changelog
* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-3
- Switch to %%ldconfig_scriptlets

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 20 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.26.0-2
- Add run-time dependency on tracker-miners

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Wed Aug 23 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.91-1
- Update to 3.25.91

* Wed Aug 16 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 09 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.4-1
- Update to 3.25.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.3-1
- Update to 3.25.3
- Update the gtk3 requirement

* Mon May 01 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.1-1
- Update to 3.25.1
- Update the gjs and gtk3 requirements

* Wed Apr 12 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Fri Mar 31 2017 Bastien Nocera <bnocera@redhat.com> - 3.24.0-3
+ gnome-documents-3.24.0-3
- Fix possible crash handling alternatively ePubs and Comics

* Thu Mar 30 2017 Bastien Nocera <bnocera@redhat.com> - 3.24.0-2
+ gnome-documents-3.24.0-2
- Fix comics display

* Wed Mar 22 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Tue Sep 06 2016 Kalev Lember <klember@redhat.com> - 3.21.90-2
- Add missing libgepub runtime dep

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1
- Add missing gnome-books postun script

* Tue Mar 29 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.0-2
- Add 'Requires: libreofficekit' (RH #1321380)

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.4-2
- Use upstreamed screenshots

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Thu Dec 17 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Nov 11 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Tue Oct 13 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0.1-1
- Update to 3.18.0.1
- Update URL

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro
- Mark gnome-books COPYING file as %%license
- Tighten -libs deps with the _isa macro

* Wed Jul 22 2015 David King <amigadave@amigadave.com> - 3.17.2-3
- Bump for new gnome-desktop3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-3
- Rebuilt for libgdata soname bump

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Mar 07 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 23 2015 Debarshi Ray <rishi@fedoraproject.org> 3.15.90-2
- Backport patch to fix books mode

* Fri Feb 20 2015 Matthias Clasen <mclasen@redhat.com> 3.15.90-1
- Update to 3.15.90

* Wed Jan 28 2015 Bastien Nocera <bnocera@redhat.com> 3.15.2-2
- Require gnome-epub-thumbnailer to go with the Books app

* Wed Jan 28 2015 Bastien Nocera <bnocera@redhat.com> 3.15.2-1
- Update to 3.15.2

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Thu Nov 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Nov 10 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.14.1-3
- Revert unoconv dependency because it pulls in other LO applications. We will
  rely on comps for the time being.

* Fri Oct 24 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.14.1-2
- Require unoconv.

* Fri Oct 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Wed Sep 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-3
- Update to 3.13.91
- Set minimum required evince and gtk3 versions

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Apr 16 2014 Adam Williamson <awilliam@redhat.com> - 3.12.0-2
- rebuild for new libgdata

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-2
- Rebuilt for gnome-desktop soname bump

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Thu Feb 06 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Thu Dec 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Nov 13 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4
- Fix %%files because the miners were split out.
- Add Requires: gnome-online-miners.

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Mon Jun 10 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.8.3-1
- Update to 3.8.3

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2.1-1
- Update to 3.8.2.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Thu Mar 28 2013 Cosimo Cecchi <cosimoc@gnome.org> - 3.8.0-2
- Enable generation of getting-started tutorial PDF

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-3
- Rebuilt for cogl soname bump

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for libgnome-desktop soname bump

* Thu Feb 07 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4-2
- Rebuild for new cogl

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Mon Oct 15 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Sep 18 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Sun Sep 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.91-2
- Rebuild against new cogl/clutter

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

