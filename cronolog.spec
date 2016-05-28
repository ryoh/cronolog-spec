Name:            cronolog
Version:         1.6.2
Release:         14%{?dist}
Summary:         Web log rotation program for Apache

Group:           Applications/System
License:         ASL 1.0
URL:             http://cronolog.org/
Source0:         http://cronolog.org/download/%{name}-%{version}.tar.gz
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
Patch1:          cronolog-largefile.patch

%description
cronolog is a simple filter program that reads log file entries from
standard input and writes each entry to the output file specified
by a filename template and the current date and time. When the
expanded filename changes, the current file is closed and a new one
opened. cronolog is intended to be used in conjunction with a Web server,
such as Apache, to split the access log into daily or monthly logs.

%prep
%setup -q
%patch1

%build
%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
sed -i 's|/www/sbin|/usr/sbin|g' %{buildroot}/%{_mandir}/man1/*
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{_sbindir}/cronosplit %{buildroot}/%{_bindir}
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%changelog
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.2-8
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.2-7
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.6.2-6
- Rebuild for selinux ppc32 issue.

* Thu Jul 05 2007 Sean Reifschneider <jafo@tummy.com> 1.6.2-5
- Included patch for LARGEFILE support, fix provided by Arenas Belon, Carlo
  Marcelo.

* Sat Jan 27 2007 Sean Reifschneider <jafo@tummy.com> 1.6.2-4
- Updating based on feedback from ville.skytta.
- Moved cronosplit to /usr/bin
- Added info pages.
- Removed INSTALL file.
- Updated path to cronolog in man page.

* Fri Jan 26 2007 Sean Reifschneider <jafo@tummy.com> 1.6.2-3
- Packaging for Fedora Extras.

* Tue Mar  8 2005 Douglas E. Warner <silfreed@silfreed.net> 1.6.2-1
- Initial RPM release.
