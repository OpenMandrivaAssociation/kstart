%define name    kstart
%define version 4.1
%define release 1

Name:		%{name}
Version:	%{version}
Release: 	%{release}
Summary: 	Kinit daemon that uses srvtabs or keytabs
License: 	GPL
Group: 		Networking/Other
URL: 		http://www.eyrie.org/~eagle/software/kstart/
Source0:	http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
Source1:	kstart.init
BuildRequires:	krb5-devel

%description
k4start, k5start, and krenew are modified versions of kinit which add support
for running as a daemon to maintain a ticket cache, running a command with
credentials from a keytab and maintaining a ticket cache until that command
completes, obtaining AFS tokens (via an external aklog) after obtaining
tickets, and creating an AFS PAG for a command. They are primarily useful in
conjunction with long-running jobs; for moving ticket handling code out of
servers, cron jobs, or daemons; and to obtain tickets and AFS tokens with a
single command. 

%prep
%setup -q

%build
%configure2_5x --disable-k4start
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_initrddir}
install -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/kstart
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
cat > %{buildroot}%{_sysconfdir}/sysconfig/kstart <<'EOF'
# kstart service configuration file
USER=apache
PRINCIPAL=HTTP/$(hostname)
KEYTAB=/etc/krb5.keytab
PERIOD=10
OPTIONS=
EOF

%files
%doc README TODO
%{_bindir}/k5start
%{_bindir}/krenew
%{_mandir}/man1/k5start.1*
%{_mandir}/man1/krenew.1*
%{_initrddir}/kstart
%config(noreplace) %{_sysconfdir}/sysconfig/kstart


%changelog
* Mon Jan 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.1-1
+ Revision: 759164
- version update 4.1

* Wed Jan 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0-1
+ Revision: 753466
- version update 4.0
- version update 4.0

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.16-3mdv2011.0
+ Revision: 612674
- the mass rebuild of 2010.1 packages

* Tue Jan 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.16-2mdv2010.1
+ Revision: 496742
- add a service script for running automatically

* Tue Jan 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.16-1mdv2010.1
+ Revision: 493844
- update to new version 3.16

* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 3.15-1mdv2010.0
+ Revision: 417384
- update to new version 3.15

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.14-1mdv2010.0
+ Revision: 383879
- import kstart

