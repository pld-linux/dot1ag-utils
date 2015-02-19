Summary:	IEEE 802.1ag (Ethernet OAM) protocol implementation
Name:		dot1ag-utils
Version:	1.0.1
Release:	1
License:	BSD-like
Group:		Networking/Admin
Source0:	https://svn.surfnet.nl/trac/dot1ag-utils/export/121/tags/1.0.1/%{name}-%{version}.tar.gz
# Source0-md5:	de3c6b8d6d36ed938f7bbbb95b2c77e2
URL:		https://svn.surfnet.nl/trac/dot1ag-utils/wiki
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IEEE 802.1ag standard is a set of protocols for Ethernet OAM (Operations,
Administration, and Management). The dot1ag-utils software package is an Open
Source (new BSD License) implementation of the IEEE 802.1ag protocol. It provides
several debugging tools that interact with IEEE 802.1ag enabled routers and
switches. The package implements the MEP Down functionality with a loopback
message initiator (ethping), a link trace message initiator (ethtrace) and a
daemon (dot1agd) that responds to loopback messages and link trace messages.
Sending and receiving of continuity check messages is done by dot1ag_ccd.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CREDITS doc/IMPLEMENTATION INSTALLATION LICENSE README doc/RELNOTES doc/TODO
%attr(755,root,root) %{_bindir}/dot1ag*
%attr(755,root,root) %{_bindir}/eth*
%{_mandir}/man1/*.1*
