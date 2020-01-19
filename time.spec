Summary: A GNU utility for monitoring a program's use of system resources
Name: time
Version: 1.7
Release: 45%{?dist}
License: GPLv2+
Group: Applications/System
Url: http://www.gnu.org/software/time/
Source: ftp://prep.ai.mit.edu/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0: time-1.7-destdir.patch
Patch1: time-1.7-verbose.patch
# Bug #702826
Patch2: time-1.7-ru_maxrss-is-in-kilobytes-on-Linux.patch
# Bug #527276
Patch3: time-1.7-Recompute-CPU-usage-at-microsecond-level.patch
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
The GNU time utility runs another program, collects information about
the resources used by that program while it is running, and displays
the results.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .ru_maxrss
%patch3 -p1 -b .recompute_cpu

%build
echo "ac_cv_func_wait3=\${ac_cv_func_wait3='yes'}" >> config.cache
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/time.info.gz %{_infodir}/dir \
    --entry="* time: (time).        GNU time Utility" >/dev/null 2>&1 || :

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_infodir}/time.info.gz %{_infodir}/dir \
    --entry="* time: (time).        GNU time Utility" >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS ChangeLog COPYING NEWS README 
%{_bindir}/time
%{_infodir}/time.info*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.7-45
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.7-44
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 06 2012 Petr Pisar <ppisar@redhat.com> - 1.7-42
- Package AUTHORS and ChangeLog

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 11 2011 Petr Pisar <ppisar@redhat.com> - 1.7-39
- Fix maximal RSS report (bug #702826)
- Clean spec file
- Recompute CPU usage at finer level (bug #527276)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Roman Rakus <rrakus@redhat.com> - 1.7-37
- Don't print errors in post and preun sections (#515936)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.7-34
- Fix Patch:/%%patch0 mismatch.
  Resolves: #463067

* Tue Mar  4 2008 Roman Rakus <rrakus@redhat.cz> - 1.7-33
- Added patch from JW (redhat@zacglen.com), less nonverbose output

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7-32
- Autorebuild for GCC 4.3

* Tue Jan 08 2008 Florian La Roche <laroche@redhat.com> - 1.7-31
- update url/license tags

* Tue Aug 21 2007 Florian La Roche <laroche@redhat.com> - 1.7-30
- rebuild

* Tue Feb 27 2007 Karsten Hopp <karsten@redhat.com> 1.7-29
- remove trailing dot from summary
- replace tabs with spaces
- replace PreReq with Requires(post)/Requires(preun)
- include license file in %%doc
- add smp flags
- use make install DESTDIR=

* Mon Jan 22 2007 Florian La Roche <laroche@redhat.com>
- add dist tag
- fix rhbz#223720

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.7-27.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.7-27.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.7-27.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.7-27
- build with gcc-4

* Wed Feb 09 2005 Karsten Hopp <karsten@redhat.de> 1.7-26
- update source URL
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not strip apps, do not compress info page

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Elliot Lee <sopwith@redhat.com>
- Remove HAVE_WAIT3 hack, tried to replace it with a requirement for an 
autoconf with the fixed test, didn't work, put in another less-bad hack 
instead.

* Wed Dec 05 2001 Tom Tromey <tromey@redhat.com>
- Bump release, force HAVE_WAIT3 to be defined at build time

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jan 31 2001 Preston Brown <pbrown@redhat.com>
- prereq install-info (#24715)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Preston Brown <pbrown@redhat.com>
- using / as the file manifesto has weird results.

* Sun Jun  4 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- buildrooted and defattr'd

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 27 1997 Cristian Gafton <gafton@redhat.com>
- fixed info handling

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file; added info file handling

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
