Name:		kstart
Version:	4.3
Release:	1
Summary: 	Kinit daemon that uses srvtabs or keytabs
License: 	GPL
Group: 		Networking/Other
URL: 		https://www.eyrie.org/~eagle/software/kstart/
Source0:	http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
Source1:	kstart.service
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

install -d -m 755 %{buildroot}%{_unitdir}
install -m 755 %{SOURCE1} %{buildroot}%{_unitdir}/kstart.service
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
cat > %{buildroot}%{_sysconfdir}/sysconfig/kstart <<'EOF'
# kstart service configuration file
USER=apache
PRINCIPAL=HTTP/$(hostname)
KEYTAB=/etc/krb5.keytab
PERIOD=10
OPTIONS=
EOF

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README TODO
%{_bindir}/k5start
%{_bindir}/krenew
%{_mandir}/man1/k5start.1*
%{_mandir}/man1/krenew.1*
%{_unitdir}/kstart.service
%config(noreplace) %{_sysconfdir}/sysconfig/kstart
