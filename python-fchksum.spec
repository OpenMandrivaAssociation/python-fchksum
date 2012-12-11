Summary:	Python C extension to (quickly) find the checksum of files
Name:		python-fchksum
Version: 1.7.1
Release: 10
Source0:	http://www.dakotacom.net/~donut/programs/fchksum/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
URL:		http://www.dakotacom.net/~donut/programs/fchksum.html
%py_requires -d
BuildRequires:	zlib-devel

%description
This module provides quick and easy functions to find checksums of files.
It supports md5, crc32, cksum, bsd-style sum, and sysv-style sum.
The advantage of using fchksum over the python md5 and zlib(.crc32)
modules is both ease of use and speed.  You only need to tell it the
filename and the actual work is done by C code.  Compared to the
implementing a read loop in python with the standard python modules,
fchksum is up to 2.0x faster in md5 and 1.1x faster in crc32.

All checksum functions take a filename as a string, and optional callback
function, and callback delay (in seconds), and return a tuple (checksum,
size).  An empty string may be substituted for filename to read from
stdin.  The returned size is always a python Long, and the checksum
return type varies depending on the function.

%package	devel
Group:		Development/Python
Summary:	Python C extension to (quickly) find the checksum of files

%description	devel
Development files for Python fast checksum

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}/%{_includedir}/python%{py_ver}
install *.h %{buildroot}/%{_includedir}/python%{py_ver}/

%files
%defattr(-,root,root)
%doc README COPYING Changelog PKG-INFO
%{python_sitearch}/*

%files devel
%defattr(-, root, root)
%doc test
%{_includedir}/python%{py_ver}/*.h



%changelog
* Wed Nov 03 2010 Michael Scherer <misc@mandriva.org> 1.7.1-9mdv2011.0
+ Revision: 592734
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7.1-8mdv2010.0
+ Revision: 442109
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.7.1-7mdv2009.0
+ Revision: 242396
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 1.7.1-5mdv2008.0
+ Revision: 71752
- add egg-info
- Rebuild for python 2.5


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 17:35:13 (56229)
- rebuild
- quiet setup

* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 17:33:37 (56228)
Import python-fchksum

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.7.1-3mdk
- Rebuild for new python

* Tue Nov 02 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.7.1-2mdk
- add BuildRequires: zlib-devel

* Fri Dec 12 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.7.1-1mdk
- First MandrakeLinux package

