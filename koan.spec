%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Network provisioning tool for Xen and Bare Metal Machines 
Name: koan
Version: 1.2.6
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GPLv2+
Group: Applications/System
Requires: mkinitrd
Requires: syslinux
Requires: python >= 2.2
BuildRequires: python-devel
%if 0%{?fedora} >= 8
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
ExcludeArch: ppc
ExcludeArch: ppc64
Url: http://cobbler.et.redhat.com/

%description

Koan stands for kickstart-over-a-network and allows for both
network provisioning of new virtualized guests and destructive re-provisioning 
of any existing system.  For use with a boot-server configured with
'cobbler'

%prep
%setup -q

%build
%{__python} setup.py build

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --optimize=1 --root=$RPM_BUILD_ROOT

%clean
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%if 0%{?fedora} > 8
%{python_sitelib}/koan*.egg-info
%endif
%dir /var/spool/koan
%{_bindir}/koan
%dir %{python_sitelib}/koan
%{python_sitelib}/koan/*.py*
%{_mandir}/man1/koan.1.gz

%doc AUTHORS COPYING CHANGELOG README

%changelog

* Thu Oct 02 2008 Michael DeHaan <mdehaan@redhat.com> - 1.2.6-1
- Upstream changes (see CHANGELOG)

* Fri Sep 26 2008 Michael DeHaan <mdehaan@redhat.com> - 1.2.5-1
- Upstream changes (see CHANGELOG)

* Wed Aug 29 2008 Michael DeHaan <mdehaan@redhat.com> - 1.2.0-1
- Upstream changes (see CHANGELOG)

* Mon Jun 16 2008 Michael DeHaan <mdehaan@redhat.com> - 1.0.2-1
- Upstream changes (see CHANGELOG)

* Fri Jun 06 2008 Michael DeHaan <mdehaan@redhat.com> - 1.0.1-1
- Upstream changes (see CHANGELOG)

