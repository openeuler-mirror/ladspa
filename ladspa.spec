Name:           ladspa
Version:        1.13
Release:        22
Summary:        Linux Audio Developer's Simple Plugin API (LADSPA)
License:        LGPLv2+
URL:            http://www.ladspa.org/
Source:         http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
Patch0001:      ladspa-1.13-plugindir.patch
BuildRequires:  perl-interpreter gcc-c++

%description
LADSPA is a standard that allows software audio processors and effects to
be plugged into a wide range of audio synthesis and recording packages.

%package        devel
Summary:        Linux Audio Developer's Simple Plug-in API
Requires:       %{name} = %{version}-%{release}

%description    devel
Thie package contains develop files and ladspa.h header file.

%prep
%autosetup -n ladspa_sdk -p1
perl -pi -e 's/^(CFLAGS.*)-O3(.*)/$1\$\(RPM_OPT_FLAGS\)$2 -DPLUGINDIR=\$\(PLUGINDIR\)/' src/makefile
perl -pi -e 's/-mkdirhier/-mkdir -p/' src/makefile
cd doc|perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
cd src
%make_build PLUGINDIR=\\\"%{_libdir}/ladspa\\\" targets LD="ld --build-id"

%install
cd src
%make_install INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
              INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
              INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf

%files
%doc doc/COPYING
%{_datadir}/ladspa
%{_libdir}/ladspa/*.so
%{_bindir}/analyseplugin
%{_bindir}/applyplugin
%{_bindir}/listplugins

%files devel
%doc doc/*.html
%{_includedir}/ladspa.h


%changelog
* Fri Nov 8 2019 Yiru Wang <wangyiru1@huawei.com> - 1.13-22
- Pakcage init
