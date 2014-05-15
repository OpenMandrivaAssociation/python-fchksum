Summary:	Python C extension to (quickly) find the checksum of files
Name:		python-fchksum
Version: 1.7.1
Release: 10
Source0:	http://www.dakotacom.net/~donut/programs/fchksum/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
URL:		http://www.dakotacom.net/~donut/programs/fchksum.html
BuildRequires:  python-devel
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
%doc README COPYING Changelog PKG-INFO
%{py_platsitedir}/*

%files devel
%doc test
%{_includedir}/python%{py_ver}/*.h
