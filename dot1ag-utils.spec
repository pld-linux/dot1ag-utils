Summary:	IEEE 802.1ag (Ethernet OAM) protocol implementation
Summary(pl.UTF-8):	Implementacja protokołu IEEE 802.1ag (Ethernet OAM)
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
The IEEE 802.1ag standard is a set of protocols for Ethernet OAM
(Operations, Administration, and Management). The dot1ag-utils
software package is an Open Source (new BSD License) implementation of
the IEEE 802.1ag protocol. It provides several debugging tools that
interact with IEEE 802.1ag enabled routers and switches. The package
implements the MEP Down functionality with a loopback message
initiator (ethping), a link trace message initiator (ethtrace) and a
daemon (dot1agd) that responds to loopback messages and link trace
messages. Sending and receiving of continuity check messages is done
by dot1ag_ccd.

%description -l pl.UTF-8
Standard IEEE 802.1ag to zbiór protokołów do operowania,
administrowania i zarządzania siecią Ethernet (Ethernet OAM:
Operations, Administration and Management). Pakiet dot1ag-utils to
mająca otwarte źródła (na nowej licencji BSD) implementacja protokołu
IEEE 802.1ag. Udostępnia kilka narzędzi diagnostycznych
współpracujących z routerami i przełącznikami obsługującymi
IEEE 802.1ag. Pakiet zawiera implementację MEP Down z inicjatorem
komunikatów zwrotnych (ethping), inicjator komunikatów śledzenia
połączenia (ethtrace) oraz demona dot1agd odpowiadającego na
komunikaty zwrotne oraz śledzenia połączenia. Wysyłanie i odbieranie
komunikatów sprawdzania ciągłości jest wykonywane przez dot1ag_ccd.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/dot1ag-utils

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALLATION LICENSE README doc/{CREDITS,IMPLEMENTATION,RELNOTES,TODO}
%attr(755,root,root) %{_bindir}/dot1ag_ccd
%attr(755,root,root) %{_bindir}/dot1agd
%attr(755,root,root) %{_bindir}/ethping
%attr(755,root,root) %{_bindir}/ethtrace
%{_mandir}/man1/dot1ag_ccd.1*
%{_mandir}/man1/dot1agd.1*
%{_mandir}/man1/ethping.1*
%{_mandir}/man1/ethtrace.1*
