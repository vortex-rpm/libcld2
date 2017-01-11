Name:      libcld2
Summary:   Compact Language Detector 2
Version:   git20170111
Release:   1%{?dist}
License:   APL2
Group:     System Environment/Libraries
Vendor:    Vortex RPM
URL:       https://github.com/CLD2Owners/cld2

Source0:   %{name}-%{version}.tar.gz


%description
CLD2 probabilistically detects over 80 languages in Unicode UTF-8 text,
either plain text or HTML/XML.


%prep
%setup -q -n %{name}-%{version}


%build
cd internal
./compile_libs.sh


%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 internal/%{name}.so $RPM_BUILD_ROOT/%{_libdir}/%{name}.so
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/%{name}/internal
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/%{name}/public
cp internal/*.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/internal/
cp public/*.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/public/


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc LICENSE README.md docs
%{_libdir}/%{name}.so
%{_includedir}/%{name}


%changelog
* Wed Jan 11 2017 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - git20170111-1.vortex
- Add missing headers

* Wed Jan 11 2017 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - git20170111-0.vortex
- Initial packaging
