Summary:	Python C extension to (quickly) find the checksum of files
Name:		python-fchksum
Version: 1.7.1
Release: %mkrel 4
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
URL:		http://www.dakotacom.net/~donut/programs/fchksum.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	python
BuildRequires:	python-devel zlib-devel

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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}/%{_includedir}/python%{pyver}
install *.h %{buildroot}/%{_includedir}/python%{pyver}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING Changelog PKG-INFO
%{_libdir}/python*/site-packages

%files devel
%defattr(-, root, root)
%doc test
%{_includedir}/python%{pyver}/*.h

