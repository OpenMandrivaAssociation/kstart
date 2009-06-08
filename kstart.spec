%define name    kstart
%define version 3.14
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release: 	%{release}
Summary: 	Kinit daemon that uses srvtabs or keytabs
License: 	GPL
Group: 		Networking/Other
URL: 		http://www.eyrie.org/~eagle/software/kstart/
Source0: 	http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
BuildRequires: 	krb5-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/k5start
%{_bindir}/krenew
%{_mandir}/man1/k5start.1*
%{_mandir}/man1/krenew.1*

